# Review Prompt

Check schema, article-mission-candidate references, source verifiability, date, media rights, test evidence, privacy and secrets. Fail closed on uncertain critical claims.

For a qualifying candidate (eligible + verified + score ≥ 80), ensure the article frontmatter uses `status: published`, a real `publishedAt`, verified primary sources, `factualStatus: verified`, and `humanReviewed: true` so merge to `main` publishes `/discoveries/` immediately. Keep the mission at `awaiting_review` and never claim deployment is complete. Create the PR for human merge review; do not merge `main` yourself.

Output structured artifacts with absolute evidence references and explicit error states.
