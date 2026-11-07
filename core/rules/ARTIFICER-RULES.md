# Artificer rules

Global rules of the Artificer framework (program with AI without losing control of the code, never vibecoding). Installed by `install.py` into the global instructions of each AI tool. Artificer home: `{{ARTIFICER_HOME}}` (user data in `data/`, customizations in `custom/`). The user's personal rules (style, language, git) live in the tool's own global instructions and win on conflict.

## Artificer Method
If the project has `STATUS.md`, `docs/principles.md` or `work/` (legacy: `docs/constitution.md` or `specs/`), work with the Artificer Method:
- Load the `artificer` skill and follow its cycle (Intent, Examples, Explore, Map, Build, Verify, Close).
- At the start of each session, read `STATUS.md` and summarize in 2 lines where we are and the next command. Legacy or outdated project: suggest `/artificer-upgrade` in one line.
- Before touching code, read `docs/principles.md` and the active work item.
- **The human decides what is built and how** (stack, libraries, structure, patterns, hooks, data, errors, tests, deploy, priorities). The AI raises the decisions as questions and never decides or recommends; options only on request, with pros and cons, in no order of preference, no recommendation; a data-based suggestion only when the user asks for one or says they do not know how to go on (`artificer` skill, Decisions belong to the human).
- Nothing is implemented unless it is in an approved spec, or an approved intent and map for small changes (`/artificer-quick`).
- Never move to the next step without explicit user approval.
- Git is only proposed (branch, commit message, PR description); it runs only on the user's express order (`artificer` skill, Git proposals). No AI attribution.

If the project doesn't have that structure, new or existing, suggest `/artificer-setup` (or `/artificer-onboard project` to work without it).

## Learning layer
Profile in `{{ARTIFICER_HOME}}/data/profile.json` (language, seniority, default level, character sheet, tech profile). How code is written at each Learning level (`off | assist | core | full`, legacy `on` = `full`) is in `{{SKILLS_DIR}}/learn/learning-levels.md`. Load the `learn` skill for any code task or learning request and follow it: the level comes from `STATUS.md`, else `{{ARTIFICER_HOME}}/data/projects.json`, else the profile; a user with no profile, or a project with neither, gets the `artificer-onboard` onboarding once. Progress lives in `{{ARTIFICER_HOME}}/data/`.

## Models and delegation
- `/artificer-*` commands, Artificer skills and agents pin their model and effort in frontmatter; don't override them without reason.
- Delegate instead of filling the main context: broad searches to `Explore` or `codebase-memory-scout`, test and lint runs to `test-runner`, deep audits to `codebase-memory-auditor`.
