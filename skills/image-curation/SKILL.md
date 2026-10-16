---
name: image-curation
version: 1.0.0
description: Source or create compliant images
category: research-and-publication
---

# image-curation

## Objective
Source or create compliant images.

## Tools / access
Licensed originals, media library, permitted image generation. Access must be authorized and failures must be reported.

## Inputs
Daily mission ID, timezone-aware research window, source constraints, tool budget, and previously published URL index.

## Procedure
1. Validate required tools and access. If unavailable, record a failure; never fake a call.
2. Perform the defined operation and retain original source links and timestamps.
3. Return structured output with a success/failure status and public-safe evidence references.
4. Record the concrete skill version and executionId in the parent mission JSON.

## Output contract
File path, origin, license, attribution, alt text, editorial use rights.

## Acceptance / safety
AI-generated scenes must be labeled as illustrations, not real photographs.
