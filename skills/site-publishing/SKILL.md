---
name: site-publishing
version: 1.0.0
description: Publish reviewed content via PR and CI
category: research-and-publication
---

# site-publishing

## Objective
Publish reviewed content via PR and CI.

## Tools / access
GitHub App + CI + DigitalOcean deploy webhook status. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
PR URL, CI status, merge approval, DO deployment evidence and smoke test result.

## Acceptance / safety
Cannot mark success until production checks actually pass.
