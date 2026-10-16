---
name: youtube-publishing
version: 1.0.0
description: Prepare an optional video upload
category: research-and-publication
---

# youtube-publishing

## Objective
Prepare an optional video upload.

## Tools / access
YouTube Data API OAuth; disabled by default. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
Draft metadata, rights checklist, privacy state, owner approval and eventual public URL.

## Acceptance / safety
Never upload without verified OAuth/rights and explicit account owner approval.
