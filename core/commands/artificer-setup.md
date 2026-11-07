---
description: ARTIFICER · Initializes the Artificer Method in a new or existing project
argument-hint: '[project name]'
model: sonnet
effort: low
---
Use the artificer skill. Project: $ARGUMENTS

1. If `STATUS.md` already exists: if it has `specs/` or `docs/constitution.md` (legacy), suggest `/artificer-upgrade` and stop; otherwise don't overwrite anything and do the same as `/artificer-status`.
2. Check whether the project already has code (sources, dependency manifest, git history). State in one line whether you treat it as **new** or **existing**.
3. Before creating anything, ask these three questions in a single block, with options and a recommendation for each. Wait for the answers.
   1. **Ownership:** yours (`own`) or somebody else's (`external`)?
   2. **Mode:** `manual` (the AI proposes branch, commit message and PR description; you run them) or `automatic` (the AI proposes them and runs each one when you expressly order it). In both, nothing git-related happens on its own. Recommend `manual` for learning.
   3. **Learning** (who writes the code, see `{{SKILLS_DIR}}/learn/learning-levels.md`): `off` (AI writes; fastest), `assist` (AI writes; you approve the change map, explain the key step and review with a risk map; recommended for day-to-day work), `core` (you write the logic and the scenario tests, AI writes the scaffolding; recommended to learn on a real project) or `full` (you write everything, AI navigates). Default: `default_level` in `{{ARTIFICER_HOME}}/data/profile.json`.

   Derive **Artificer files**: `tracked` if `own`, `local-only` if `external` (say it in one line; the user may override).
4. If `local-only`: add to `.git/info/exclude` BEFORE creating any file: `STATUS.md`, `docs/product.md`, `docs/principles.md`, `docs/design.md`, `docs/architecture.md`, `docs/deploy.md`, `docs/metrics.md`, `docs/backlog.md`, `work/`, and `{{PROJECT_RULES}}` if the project doesn't already track one. Check with `git status --short` that none appears.
5. Create `docs/` (product, principles, design, architecture, deploy, metrics, backlog, title only) and `work/`. Create `tests/` only if the project has no other test convention.
6. Create `STATUS.md` from `templates/status.md`. Phase: setup. Next step: `/artificer-product`. Fill `## Workflow` with the four settings and `- Framework: Artificer v<VERSION from {{ARTIFICER_HOME}}/VERSION>`. Existing project: add under "Key decisions": `Existing project: project docs document what is built`.
6b. Tech profile: detect the project's stack (manifest, lockfile, config). For tools missing from `profile.json` → `tech`, ask their level (none / basic / medium / advanced, with the one-line meanings; each tool can be skipped) in a single block. Skip if none are missing.
7. Output style: set `outputStyle` in `.claude/settings.local.json` for the chosen level (table in `learning-levels.md`; `off`: leave unset). Show the change in one line first.
8. Project `{{PROJECT_RULES}}`: new → from `templates/project-rules.md`, technical fields `[PENDING]`; existing → don't replace, add only the missing sections (Verification, Rules); if it is tracked and the files are `local-only`, list the sections and ask.
9. Git (artificer skill, Git proposals): `local-only` → no git at all; `tracked` without a repository → git proposal for `git init`, a basic `.gitignore` and the initial commit `chore: initial Artificer structure` on `main`; `tracked` with a repository → git proposal for the branch `chore/artificer-setup` from an up to date `main`, the commit, push and PR. Run nothing unless the mode is `automatic` and the user expressly orders each action.
10. Confirm in 2 lines what was created and the next command.
