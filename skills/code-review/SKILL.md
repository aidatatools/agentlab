---
name: code-review
version: 1.0.0
description: Assess snippet provenance and safe reproducibility
category: research-and-publication
---

# code-review

## Objective
Assess snippet provenance and safe reproducibility.

## Tools / access
Static tools / restricted sandbox. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
Language, original repo URL, commit, origin/adaptation license, exact test results.

## Acceptance / safety
Never execute unknown project code with host privileges; nonexecuted code is marked not_run.
