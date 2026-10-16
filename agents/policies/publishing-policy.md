# Publishing Policy

All new articles and website code go through branches and PRs. Check schema and Astro build before merge.

**Daily articles:** when a candidate is eligible, verified, and scores ≥ 80, the daily PR must include the article with `status: published` (not `review`/`draft`). Merging the daily PR is the human review step; the designated reviewer (e.g. `chuangtc`) checks on a DEV computer before merge. Demo content stays `demo` and never counts as news.

**Missions:** stay `awaiting_review` in the daily PR. Do not claim DigitalOcean deploy success until a real post-deploy smoke test is recorded in a follow-up PR, which may then set the mission to `published`.

YouTube self-upload remains owner-approved only. Never invent timestamps, test passes, or deployment outcomes.
