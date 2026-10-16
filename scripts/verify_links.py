#!/usr/bin/env python3
"""Optional live reachability probe; 2xx/3xx is NOT proof that a claim is factual."""
from pathlib import Path
import json,sys,urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parent))
from validate_content import ROOT,parse_frontmatter

def main():
    issues=[]
    for p in (ROOT/'src/content/articles').rglob('*.md'):
        data=parse_frontmatter(p)
        if data['status']!='published':continue
        for source in data['sources']:
            try:
                req=urllib.request.Request(source['url'],headers={'User-Agent':'AgentLab LinkChecker/1.0'})
                with urllib.request.urlopen(req,timeout=10) as resp:
                    print(f'{resp.status} {source["url"]}')
            except Exception as ex:issues.append((source['url'],str(ex)))
    if issues:
        for url,err in issues:print('Unreachable:',url,err)
        raise SystemExit(1)
    print('All checked published source links responded. This does not validate their factual claims.')
if __name__=='__main__':main()
