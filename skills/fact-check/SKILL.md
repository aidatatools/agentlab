---
name: fact-check
version: 1.0.0
description: Validate claims and source provenance
category: research-and-publication
---

# fact-check

## Objective
Validate claims and source provenance.

## Tools / access
Primary sources / trusted official pages. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
Claim-level verifications with links, what was directly established, disputed claims and timestamps.

## Acceptance / safety
Never convert marketing promises or simulations into historical fact.
