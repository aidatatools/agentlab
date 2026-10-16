#!/usr/bin/env python3
"""Pure, deterministic ranking; NEVER treats demo or unverified candidates as publishable."""
import argparse,json
from pathlib import Path
WEIGHTS={'breakthrough':.30,'interestingness':.25,'technicalDepth':.20,'reproducibility':.15,'credibility':.10}

def score(candidate):
    values=candidate['scores']
    for key in WEIGHTS:
        if key not in values or not 0<=values[key]<=100:raise ValueError(f'Invalid {key}')
    return round(sum(values[k]*weight for k,weight in WEIGHTS.items()),2)

def rank(doc):
    rows=[{'id':c['id'],'title':c['title'],'score':score(c),'eligibility':c['eligibility']} for c in doc['candidates']]
    rows.sort(key=lambda c:-c['score'])
    eligible=[] if doc.get('demo') else [r for r in rows if r['eligibility']=='eligible' and r['score']>=80]
    return {'date':doc['date'],'demo':doc.get('demo',False),'ranked':rows,'proposedCandidateId':eligible[0]['id'] if eligible else None,'publicationAllowed':bool(eligible)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output');a=p.parse_args()
    result=rank(json.loads(Path(a.input).read_text(encoding='utf-8')))
    output=json.dumps(result,ensure_ascii=False,indent=2)
    if a.output:Path(a.output).write_text(output+'\n',encoding='utf-8')
    else:print(output)
