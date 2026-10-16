---
name: arxiv-research
version: 1.0.0
description: Find and read relevant arXiv papers
category: research-and-publication
---

# arxiv-research

## Objective
Find and read relevant arXiv papers.

## Tools / access
arXiv API / official arXiv pages. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
arXiv ID, v-number, title, authors, first submission and last revision timestamps, method, limitations.

## Acceptance / safety
Clearly distinguish preprint status from peer-reviewed publication.
