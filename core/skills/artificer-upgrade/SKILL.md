---
name: artificer-upgrade
description: ARTIFICER · Updates a project's framework structure (STATUS.md workflow settings, project {{PROJECT_RULES}} sections) to the current Artificer version, applying MIGRATIONS.md step by step with the user's approval. Never touches code, specs, plans or tasks. Use when the user runs /artificer-upgrade, or suggest it when a project's STATUS.md has no Framework line or an older version.
argument-hint: '(no arguments: works on the current project)'
model: sonnet
effort: medium
---
Reply in the language of `{{ARTIFICER_HOME}}/data/profile.json`.

## Always start with this disclaimer (translated to the reply language)
> This command only updates the Artificer framework files of this project (`STATUS.md` settings, framework sections of the project `{{PROJECT_RULES}}`, and the local `outputStyle` setting). It never touches your code, specs, plans, tasks or decisions (the only exception, if a migration lists one, is renaming framework markers like `TODO(you)`, always shown and approved first). Nothing is written without your approval.

## Steps
1. Read `{{ARTIFICER_HOME}}/VERSION` and `MIGRATIONS.md` in this skill's folder, and the project's `STATUS.md`. If there is no `STATUS.md`, say the project does not use the Artificer Method, suggest `/artificer-setup` or `/artificer-onboard project`, and stop.
2. Find the project version in `## Workflow` (`- Framework: Artificer v<x>`). No line = unversioned. If it equals `VERSION`, say it is up to date and stop.
3. List every pending migration (newer than the project's version), one line per change, in plain words.
4. Go through the changes in order. When a change needs a decision (it says **Ask**), ask one question at a time with options and a recommendation. Never convert a setting whose meaning changed without asking.
5. Show the full proposed diff of `STATUS.md` and of the project `{{PROJECT_RULES}}` (if touched). Wait for explicit approval.
6. Apply. Update the `Framework` line to the current version.
7. Git (read `## Workflow` first; artificer skill, Git proposals): `local-only` → no git at all; otherwise a git proposal for the branch `chore/artificer-upgrade-v<version>` from an up to date `main`, the commit `chore: upgrade Artificer to v<version>`, push and PR. Run nothing unless the mode is `automatic` and the user expressly orders each action. Never commit to `main`.
8. Confirm in 2 lines: version now, settings that changed.
