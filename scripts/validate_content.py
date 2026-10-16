#!/usr/bin/env python3
"""Validate source records, cross-references, and publication safeguards."""
import json
from pathlib import Path
from datetime import date
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def load_json(path): return json.loads(path.read_text(encoding='utf-8'))

def check(schema_name, data, path):
    schema=load_json(ROOT/'schemas'/f'{schema_name}.schema.json')
    v=Draft202012Validator(schema,format_checker=FormatChecker())
    errors=sorted(v.iter_errors(data),key=lambda e: list(map(str,e.path)))
    if errors:
        raise ValueError(f'{path}: '+ '; '.join(f'{list(e.path)} {e.message}' for e in errors))

def parse_frontmatter(path):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'): raise ValueError(f'{path}: missing YAML frontmatter')
    parts=text.split('---\n',2)
    if len(parts)<3:raise ValueError(f'{path}: unterminated YAML frontmatter')
    result=yaml.safe_load(parts[1])
    if not isinstance(result,dict):raise ValueError(f'{path}: invalid metadata')
    return result

def main():
    articles={}; missions={}; agents={}; candidates=set(); errors=[]
    for path in (ROOT/'src/content/agents').rglob('*.json'):
        try:
            obj=load_json(path);check('agent',obj,path)
            if obj['id'] in agents:raise ValueError('Duplicate agent id')
            agents[obj['id']]=obj
        except Exception as exc:errors.append(str(exc))
    for path in (ROOT/'src/content/missions').rglob('*.json'):
        try:
            obj=load_json(path);check('mission',obj,path)
            date.fromisoformat(obj['date'])
            if obj['missionId'] in missions:raise ValueError('Duplicate mission ID')
            if obj['status']=='published' and (obj['outcome']['publicationStatus']!='published' or not obj['outcome']['deploymentUrl']):raise ValueError('Published mission missing deployed URL and matching outcome')
            missions[obj['missionId']]=obj
        except Exception as exc:errors.append(f'{path}: {exc}')
    for path in (ROOT/'data/candidates').rglob('*.json'):
        try:
            obj=load_json(path);check('candidate',obj,path)
            for c in obj['candidates']:
                if c['id'] in candidates: raise ValueError(f'Duplicate candidate id {c["id"]}')
                candidates.add(c['id'])
            if obj.get('demo') and obj.get('selectedCandidateId'):raise ValueError('Cannot select a demo as real discovery')
        except Exception as exc:errors.append(f'{path}: {exc}')
    for path in (ROOT/'src/content/articles').rglob('*'):
        if path.suffix not in ('.md','.mdx'):continue
        try:
            obj=parse_frontmatter(path);check('article',obj,path)
            if obj['articleId'] in articles:raise ValueError('Duplicate articleId')
            if obj['missionId'] not in missions:raise ValueError('Missing mission reference')
            if obj['author']['agentId'] not in agents:raise ValueError('Unknown agent reference')
            if obj['candidateId'] not in candidates:raise ValueError('Unknown candidate reference')
            if obj['status']=='published':
                if not obj['sources'] or not any(source['verified'] for source in obj['sources']):raise ValueError('Published articles require verified primary source')
                if obj['verification']['factualStatus']!='verified':raise ValueError('Published article factualStatus must be verified')
                if obj['verification']['humanReviewed'] is not True:raise ValueError('MVP requires human-reviewed publication')
                if missions[obj['missionId']]['status'] not in ('awaiting_review','published'):raise ValueError('Published article must link to reviewed/published mission; deployment outcome is finalized later')
                if any('example.org' in x['url'] for x in obj['sources']):raise ValueError('Example domain cannot substantiate published story')
            articles[obj['articleId']]=obj
        except Exception as exc:errors.append(f'{path}: {exc}')
    for mid,m in missions.items():
        aid=m['outcome']['articleId']
        if aid and aid not in articles:errors.append(f'{mid}: unknown article {aid}')
    if errors:
        for e in errors:print('ERROR:',e)
        raise SystemExit(1)
    print(f'Content OK: {len(articles)} article(s), {len(missions)} mission(s), {len(agents)} agent(s), {len(candidates)} candidate(s).')

if __name__=='__main__':main()
