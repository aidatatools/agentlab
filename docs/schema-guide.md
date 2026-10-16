# Content schemas and sample references

## Articles

`src/content/articles/YYYY/MM/article-slug.md` frontmatter must match `schemas/article.schema.json` as well as `src/content.config.ts`. The body is Markdown/MDX; all source references belong in `sources`. `missionId` and `candidateId` join the run and discovery dataset. `status: demo` is visibly tagged and excluded from publication statistics. `status: published` requires factualStatus verified and humanReviewed true under this MVP policy.

## Missions

`src/content/missions/YYYY/MM/DATE.json` matches `schemas/mission.schema.json`. Records true tool steps and evidence rather than subjective prose. Keep states `planned`, `running`, `awaiting_review`, `failed`, `published` and exceptional `demo`. Costs use `null` if unknown, not `0`.

## Candidate batches

`data/candidates/DATE.json` matches `schemas/candidate.schema.json`. Individual candidate scores are raw 0–100 dimensions; `scripts/rank_candidates.py` computes a weighted total. The demo sample has deliberately invalid publication eligibility.

## Agents and Skills

`src/content/agents/*.json` describes configuration; `skills/*/SKILL.md` describes reusable instructions. The `skillsUsed` array in the *actual mission* records what ran, at what version and with which execution/evidence IDs. A declared skill is not proof it was executed.

## Sample assets

Sample article `/discoveries/agentlab-methodology-demo/` has an original SVG illustration and a unit-testable Python snippet; it is **not real news**. The example candidate uses `example.org` and has no actual fetch result. No Twitter/X, GitHub, arXiv, YouTube or DigitalOcean APIs are invoked in this ZIP.
