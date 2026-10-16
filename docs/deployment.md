# GitHub + DigitalOcean App Platform deployment

1. Verify `npm ci && npm run check && npm run build` locally. `package-lock.json` is committed and `build.yml` installs with `npm ci`.
2. Create GitHub repository `agentlab-aidatatools` and push these files to `main`.
3. Protect `main`. Require an approver and the `Validate records and run tests` and `Astro static build` checks before merge.
4. In DigitalOcean App Platform: **Create App → GitHub → Repository/Branch: main → Static Site**. Set build command `npm ci && npm run build`, output directory `dist`, and enable auto-deploy.
5. Add the **custom domain** `agentlab.aidatatools.com`; create the DNS target shown by DigitalOcean, not a guessed CNAME/A record. Ensure HTTPS is healthy.
6. Trigger the manually dispatched `Verify already-deployed site` workflow after DigitalOcean declares the deployment successful. It checks that the resulting HTML contains AgentLab, but does not prove content accuracy.
7. Run the agent runner on a **separate restricted account / container / VM**, preferably outside the public web stack. Schedule at a chosen time using `Asia/Taipei` and handle API rate limits, retries and task idempotency.
8. Give the agent only fine-grained GitHub PR/Contents permissions for this repo. Do not give it direct App Platform secrets, root SSH, or merge rights.

**Important:** App Platform deploys on `main`; the included `publish.yml` is a manual post-deploy smoke test, not an alternative deploy trigger. A reviewed article can have status `published` in the merged PR while its related mission remains `awaiting_review` / outcome `in_review`. Only after the first real deploy is verified should a follow-up PR set the mission deployment URL and `status=published`. This second PR triggers another harmless static-site deployment.

**Initial cost:** depends on the actual DigitalOcean static-site plan/usage, API access, external agent execution, and media storage. Confirm current pricing on DigitalOcean before production.
