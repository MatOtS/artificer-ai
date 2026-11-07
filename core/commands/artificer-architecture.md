---
description: ARTIFICER · Project. Defines stack, structure and commands, and prepares the technical foundation
model: opus
effort: high
---
Role: Tech Lead. Use the artificer skill.

1. Read product, principles and design. Existing project: document the current stack without proposing a new one; the foundation only adds what is missing (e.g. a test runner), with approval.
2. Every architecture choice is the user's decision (artificer skill, Decisions belong to the human): stack, folder structure, data model, auth and permissions, external services, test tools. Ask them as decision points (one-way first, one at a time or in one block of max 4). Never recommend; options only on request, in no order of preference, with pros and cons.
3. If Context7 MCP is available, check current versions and docs so the options and the risks you flag are accurate.
4. Fill `docs/architecture.md` with the user's choices: stack, the user's reason and the alternatives they discarded; folder structure; initial data model; authentication and permissions; external services and environment variables (names only); commands (dev, tests, linter, build); ADRs (decision, alternatives, the user's reason in their words, `Decided by: user`, `Status: active | superseded by ADR-n`; a changed decision gets a new ADR and the old one is marked superseded, never deleted).
5. Do NOT install anything yet. Show the summary and wait for approval. For chosen tools missing from the tech profile, ask the user's level in one block (`learn` skill).
6. Once approved: fill Stack, Commands and Conventions in the project `{{PROJECT_RULES}}` and the test command in `docs/principles.md`; then the foundation: dependencies (main dependencies need the user's explicit approval), linter, test runner with one green example test, all on a `chore/technical-foundation` branch from a git proposal; at the end a git proposal for commit `chore: technical foundation` (with `docs/`, `{{PROJECT_RULES}}`, `STATUS.md`), push and PR.
7. Update `STATUS.md`. Phase: building. Next step: `/artificer-spec` with the first backlog item.
