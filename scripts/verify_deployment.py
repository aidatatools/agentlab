#!/usr/bin/env python3
"""Post-deployment smoke test; run after DigitalOcean reports deployment complete."""
import argparse,urllib.request
p=argparse.ArgumentParser();p.add_argument('--url',default='https://agentlab.aidatatools.com/');a=p.parse_args()
req=urllib.request.Request(a.url,headers={'User-Agent':'AgentLab SmokeTest/1.0'})
with urllib.request.urlopen(req,timeout=20) as res:
    html=res.read(250000).decode('utf-8','replace')
    if res.status!=200 or 'AgentLab' not in html:raise SystemExit('Smoke test failed')
    print(f'Smoke test passed: HTTP {res.status} {a.url}')
