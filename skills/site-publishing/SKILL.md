---
name: site-publishing
version: 1.0.0
description: Open a PR that publishes qualifying articles on merge via CI/CD
category: research-and-publication
---

# site-publishing

## Objective
Open a PR that publishes qualifying articles on merge via CI/CD.

## Tools / access
GitHub App + CI + DigitalOcean deploy webhook status. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Ensure qualifying articles already use `status: published` in the branch so merge makes `/discoveries/` live; keep mission `awaiting_review`.
3. Open the PR as the GitHub App, request the human reviewer, and retain the PR URL. Do not merge `main` yourself.
4. After App Platform reports a successful deploy, run a real smoke test in a **follow-up** change before promoting the mission to `published`.
5. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
PR URL, CI status, merge approval, DO deployment evidence and smoke test result (null until actually observed).

## Acceptance / safety
Cannot mark deploy/mission success until production checks actually pass. Never invent timestamps or URLs.
