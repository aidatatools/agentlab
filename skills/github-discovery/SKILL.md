---
name: github-discovery
version: 1.0.0
description: Discover novel public Python and TypeScript repositories
category: research-and-publication
---

# github-discovery

## Objective
Discover novel public Python and TypeScript repositories.

## Tools / access
GitHub search / releases / commits API. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
Repo URL, commit SHA, language, license, release timestamp, README finding and confidence.

## Acceptance / safety
Inspect original repository and avoid star-count-only ranking.
