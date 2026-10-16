---
name: article-writing
version: 1.0.0
description: Draft a factual Traditional Chinese story
category: research-and-publication
---

# article-writing

## Objective
Draft a factual Traditional Chinese story.

## Tools / access
Content collection authoring. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
MD/MDX and fully populated verified metadata, alt text, appropriately cited sources. For eligible+verified+score≥80 candidates, set `status: published` with real `publishedAt` and `humanReviewed: true` in the daily PR; otherwise write no article. Demo samples stay `demo`.

## Acceptance / safety
Do not invent quotations, timestamps, metrics or citations.
