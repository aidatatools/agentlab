# Architecture

```text
Daily schedule (Asia/Taipei) — hosted outside Static Site
  │
  ├─ Discover (X API / GitHub API / arXiv feed) -> evidence snapshots
  ├─ Deduplicate + rank -> data/candidates/YYYY-MM-DD.json
  ├─ Verify claims, license, source date, code provenance
  ├─ Build editorial article + licensed images + code snippets
  ├─ Write mission log with skills, tool calls, tests, cost and failures
  └─ GitHub PR (restricted token) -> Validate + Astro CI -> human approval
                                                    │
                                             merge protected main
                                                    │
                                     DigitalOcean App Platform Static Site
                                                    │
                                       agentlab.aidatatools.com
                                                    │
                          post-deploy check -> append outcome via next PR
```

**Agent-neutral contract.** A GrokBot/OpenClaw runner or a different provider can emit the same JSON/MDX files. Agent identity and actual model must be recorded from the execution adapter; do not equate a configured provider with the executor.

**Publication state.** `draft -> review -> published` for article, independent of `planned -> running -> awaiting_review -> published|failed` mission. `demo` is terminal demonstration data and excluded from KPIs. Publishing uses protected Git branch policies. A reviewed article may enter `main` as `published` while its mission remains `awaiting_review`, because success cannot be marked until actual DigitalOcean deployment and smoke test; finalize mission status in a second PR.

**Evidence separation.** Public evidence is a minimal sanitized pointer. Full logs, private prompts, OAuth secrets and uploaded videos should stay in private storage. Never ship an untrusted tool response directly to the Astro content tree without validation/sanitization.

**Daily guarantee.** Scheduled discovery/reporting does not guarantee there is a genuine breakthrough. If no credible candidate passes, record a transparent no-publication mission, or use a separately reviewed less sensational research digest with truthful labeling.

**First v2 milestone.** Integrate real source collectors and runner-side PR creation (NOT included in starter), lock dependencies, deploy app, then introduce opt-in YouTube upload.
