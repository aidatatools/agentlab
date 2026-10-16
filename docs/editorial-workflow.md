# Editorial and audit workflow

## Selection criteria

- Novelty/breakthrough 30%, interestingness 25%, technical depth 20%, reproducibility 15%, credibility 10%.
- `score >=80` is necessary but not sufficient: sources must be credible, dated and verified; no claim can be upgraded from speculation to fact.
- Candidate record includes rank, reject reason, canonical source URL and original timestamp if available.
- Use both an official claim and at least one independent source for extraordinary physical-world claims when possible. If unavailable, report it as unverified or don't publish.

## When to write code snippets

- Python or TypeScript excerpts should link to original commits, record origin (`original`, `adapted`, `quoted`) and check license/attribution before republication.
- Execute safe, isolated tests only when feasible; code not executed must be marked `not_run`. Do not execute unfamiliar repositories directly on a privileged agent VM.

## Images and YouTube

- Every asset must record `origin`, credit, alt text and copyright permission.
- AI-generated concept art must be visibly labeled illustration, particularly for product announcements.
- YouTube third-party embeds only for valid publicly embeddable URLs; self-upload is **disabled by default**, only with OAuth, rights review and account owner approval.

## Auditing

- Mission record always captures goal, agent/model, candidates, selected score, actual skill versions, timeline, evidence pointers, CI checks, outcomes, run costs if measured, human interventions and lessons.
- Preserve failure missions and no-publish decisions.
- Never include prompt injection, raw tokens, unredacted internal logs, or PII in public artifacts.

## Example outcomes

1. Verified paper + runnable repository → report technical method, commit pin, limitations, original links.
2. Breaking news / high-impact company announcement → verify who claims what, actual date/status and distinguish concept from release.
3. No sufficiently credible candidate → publish mission report with `status=failed` or `awaiting_review`, explain rejection and retry next day; don't invent a breaking event.
