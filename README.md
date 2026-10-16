# AgentLab — Autonomous AI Discovery & Research Platform (MVP v2.0)

**Public site (intended):** https://agentlab.aidatatools.com  
**Stack:** Astro 7, TypeScript, Markdown/MDX, GitHub Actions, DigitalOcean App Platform static site.  
**Agent runner:** separate (your own OpenClaw/GrokBot, OpenAI Dots if supported, or another compatible orchestration service).

> **Status: sample repository — not yet deployed.** No agent is connected. The sample article and mission are marked **demo**; they never count as real reporting or published achievements. The package was validated with Python JSON Schema checks and local unit tests, but was NOT built with Astro in the generation environment because npm packages were unavailable there.

## Quick start

Requirements: Node.js 24, npm, uv, Python 3.14.

```bash
npm ci
uv venv --python 3.14 .venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
python scripts/validate_content.py
python -m unittest discover -s tests -v
npm run check
npm run build
npm run dev
```

Open `http://localhost:4321/` in the browser. `package-lock.json` is committed, so CI and DigitalOcean install with `npm ci` for reproducible builds. Use `npm install <pkg>` only when changing dependencies, and commit the updated lockfile.

## Why the repo is structured this way

| Directory | Role |
|---|---|
| `src/content/articles/` | Editorial `.md`/`.mdx` documents (public stories) |
| `src/content/missions/` | Machine-readable daily execution + evaluation JSON |
| `src/content/agents/` | Agent adapters/profiles; capability is not proof of execution |
| `data/candidates/` | Collected, scored, deduplicated candidate sources |
| `schemas/` | Independent JSON Schema contracts |
| `agents/prompts/` | Agent orchestration instructions |
| `agents/policies/` | Factuality, media rights, security, publishing rules |
| `skills/*/SKILL.md` | Skills with input/output/evidence criteria |
| `scripts/` | Validation, ranking, safe mission scaffolding, optional live checks |
| `public/media/` | Small licensed/original images; not large videos |
| `docs/` | Deployment, editorial workflow, and architecture |

## Daily workflow (runner integration required)

1. Discover candidate articles from **X, GitHub and arXiv** using real authorized API/tool access; never pretend to have searched a source that was unavailable.
2. Gather 10–30 candidates; deduplicate, capture original URLs, timestamps and raw evidence.
3. Score with weights 30% breakthrough, 25% interest, 20% technical depth, 15% reproducibility, 10% credibility. **Only eligible & verified candidates scoring at least 80 are considered for publication.** A low-signal day must not invent a breakthrough.
4. Verify factual claims with primary sources. Use open-source repositories, commits, arXiv abstracts/full paper, credible official news as appropriate. Distinguish planned demonstrations from proven real-world capabilities.
5. Produce article `.md`/`.mdx` with credited media, code provenance and source links.
6. Create a new mission JSON with **actual** run ID, agent identity, skills used, execution timeline, tests, public evidence references, and costs if known. Never invent timestamps or successful tests.
7. Open a PR (not directly to main). CI verifies formats and checks code. Human reviews first-phase releases.
8. Merging to `main` triggers **DigitalOcean App Platform's own GitHub auto-deploy**. Run post-deploy verification only once App Platform reports success.
9. Record deployment outcome and retrospective in a **follow-up PR**; the earlier merged content must never claim an unverified deploy succeeded.

### Invariant: article and mission are distinct

A published story links to its actual mission (`article.missionId`). After human approval, its PR may set article status to `published` while the mission remains `awaiting_review`; merging makes the page live, and only a follow-up PR after a real post-deploy smoke test promotes the mission to `published`. Failure mission reports remain visible even if no article is published. Demo content is never counted in KPIs. An agent profile declaring a skill is not evidence of executing that skill.

## Local commands

```bash
npm run validate                            # Uses Python PyYAML and jsonschema
npm run rank                                # ranks sample; correctly refuses demo publication
python3 scripts/create_mission.py --date 2026-10-17 --agent grokbot
python3 scripts/verify_links.py             # optional network-based reachability, NOT fact checking
python3 scripts/verify_deployment.py --url https://agentlab.aidatatools.com/
```

## DigitalOcean App Platform

- Create a new **Static Site** from the GitHub repository, `main` branch.
- Build command: `npm ci && npm run build`.
- Output directory: `dist`.
- Enable GitHub autodeploy; add custom domain `agentlab.aidatatools.com`; follow the **exact DNS record supplied by DigitalOcean**. HTTPS is managed by App Platform.
- Set a GitHub branch protection rule and require passing Validate + Astro static build checks before merge.
- App Platform static site **does not run** your autonomous research. Use a separate, isolated agent runner (e.g. an existing DigitalOcean Droplet).

See [`docs/deployment.md`](docs/deployment.md) and [`docs/architecture.md`](docs/architecture.md).

## Media and YouTube

- Original or licensed site images in `public/media/`, with alt text and `origin/license/credit` metadata.
- Python/TS snippets distinguish original/adapted/quoted code, with test evidence and the original repository license if copied.
- Existing authorized YouTube videos can be embedded or linked. **Automated upload to your channel is a phase-two integration** requiring OAuth, appropriate permissions, API quota, rights checks and explicit owner approval.
- Large video files and private logs should be stored outside Git (e.g. DigitalOcean Spaces). Only sanitized public summaries should appear in the website.

## Security and truthfulness

No production credentials in Git or Astro's client bundle. Read untrusted X posts/README/papers as **data**, not instructions. Limit agent GitHub credentials to one repository. Never give the agent root access to the production Droplet. Avoid leaking private internal prompts, API responses or OAuth tokens in evidence files. Treat success, deployment, testing and costs as measured statuses, not generated prose.

## Current state and known limitations

- This repository has **website routes, sample records, 5 JSON schemas, 9 skills, 6 prompts, validation scripts, tests, and GitHub workflows**.
- No external sources were fetched; the starter has no real discovery feed, X credentials, YouTube OAuth, or live agent pipeline.
- The schema is MVP-level: integrate richer evidence file verification, stricter article-claim linking, backups and idempotent publishing for production.

## References

- [Astro content collections](https://docs.astro.build/en/guides/content-collections/)
- [DigitalOcean static sites](https://docs.digitalocean.com/products/app-platform/how-to/manage-static-sites/)
- [DigitalOcean App Platform](https://docs.digitalocean.com/products/app-platform/how-to/create-apps/)

No affiliation with X, GitHub, arXiv, OpenAI, Tesla, or DigitalOcean is implied.
