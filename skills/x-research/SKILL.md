---
name: x-research
version: 1.0.0
description: Search and validate X posts
category: research-and-publication
---

# x-research

## Objective
Search and validate X posts.

## Tools / access
X API or an explicitly authorized search provider. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
Posts with post URLs, author handles, published time, retrieved time and any available engagement numbers; rate limits are recorded.

## Acceptance / safety
No claims based on undated reposts or unverifiable viral screenshots.
