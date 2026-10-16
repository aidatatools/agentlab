#!/usr/bin/env python3
"""Create a safe PLANNED template. Does not research, publish or fabricate outcomes."""
import argparse,json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--date',default=datetime.now(ZoneInfo('Asia/Taipei')).strftime('%Y-%m-%d'));p.add_argument('--agent',default='grokbot');args=p.parse_args()
d=datetime.strptime(args.date,'%Y-%m-%d').date();mid=f'mission-{d.strftime("%Y%m%d")}-001'
path=ROOT/'src/content/missions'/d.strftime('%Y/%m')/f'{d.isoformat()}.json'
path.parent.mkdir(parents=True,exist_ok=True)
if path.exists():raise SystemExit(f'Not overwriting existing mission: {path}')
obj={
  'schemaVersion':'1.0','missionId':mid,'date':d.isoformat(),'timezone':'Asia/Taipei','status':'planned',
  'objective':{'goal':'Research, validate and propose one outstanding discovery.','sources':['x','github','arxiv'],'deliverables':['Verified candidate','Proposed article','Mission record']},
  'agent':{'id':args.agent,'framework':'unconfigured','model':'unconfigured','runId':None},
  'selection':{'candidatesEvaluated':0,'selectedCandidateId':None,'selectionScore':None,'rankingArtifact':None},
  'skillsUsed':[],'timeline':[],'tests':[{'name':'Article content validation','status':'not_run','artifact':None},{'name':'Site build','status':'not_run','artifact':None}], 'evidence':[],
  'outcome':{'articleId':None,'githubCommit':None,'githubPullRequest':None,'deploymentUrl':None,'publicationStatus':'not_published'},
  'metrics':{'durationSeconds':None,'tokens':None,'estimatedCostUsd':None,'humanInterventions':0},
  'retrospective':{'successes':[],'failures':[],'lessonsLearned':[],'nextActions':[]}}
path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(path)
