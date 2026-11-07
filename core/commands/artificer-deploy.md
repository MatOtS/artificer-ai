---
description: ARTIFICER · Launch. Prepares and documents the production deployment
model: sonnet
effort: medium
---
Role: DevOps. Use the artificer skill.

1. Read `STATUS.md`, `docs/architecture.md` and the status of the work items. If any work item included in the release is not `done` or there are red tests, stop and say so.
2. Platform, environments, CI/CD and rollback strategy are the user's decisions (artificer skill, Decisions belong to the human): ask them; options only on request, in no order of preference, no recommendation. Then fill in `docs/deploy.md`:
   - Platform and environments
   - Environment variables (names only)
   - Reproducible deployment steps
   - CI/CD: what runs on every push and on every merge to main
   - Rollback plan
   - Pre-deploy checklist: build, tests, variables, domain, HTTPS
3. Prepare the required configuration files (CI, hosting).
4. NEVER deploy to production without explicit user confirmation at that moment.
5. Update `STATUS.md`. Phase: launched. Next step: `/artificer-metrics`.
