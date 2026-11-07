---
name: artificer-onboard
description: ARTIFICER · Onboarding. Shows the short guide to the framework (criterion, method, Learning levels, sheet) and creates or edits the user profile; also sets the Learning level of a project without STATUS.md. Use on first use (no {{ARTIFICER_HOME}}/data/profile.json), when the user asks how the system works or wants to change their profile, and when starting work in a project with no STATUS.md that is not in {{ARTIFICER_HOME}}/data/projects.json.
argument-hint: '[project] (empty = profile; "project" = level for the current project)'
model: sonnet
effort: low
---
Reply in the profile's `language`; if there is no profile yet, reply in the language the user is writing in.

## A. First use or "how does this work" (no profile, or no argument)
1. Show this guide, translated to the reply language, in about 10 lines:

   **Artificer** · In fantasy worlds, the artificer builds their own mechanical creatures, knows every piece and is never turned on by them. Here the AI is your creation and you direct it.
   - **Criterion**: program with AI without losing control of the code. Never vibecoding.
   - **Method** (`/artificer-*`): you define what gets built (intent and Given/When/Then examples), approve the change map, and approve every diff after a focused review.
   - **Learning level**: how much of the code you write.
     - `off`: the AI writes everything; you approve the result.
     - `assist`: the AI writes; you approve a change map first, walk the exact code and answer short questions.
     - `core`: you write the logic and test assertions; the AI writes the scaffolding.
     - `full`: you write everything; the AI navigates and reviews.
   - **Learning inside the work**: guided reads when you touch unknown code, reviews you do yourself, `/artificer-debug` for bugs, `/artificer-explain` for concepts.
   - **Character sheet** (`/artificer-stats`): levels that only go up by passing trials. Optional.

2. Ask in a single block, with a recommendation for each:
   1. Reply language.
   2. Your current level: junior, mid or senior (sets the starting difficulty; levels still need trials).
   3. Default Learning level for projects (recommended: `assist`).
   4. Character sheet with XP and levels: yes or no (recommended: yes).
   5. **Tech survey** (in the reply language): "Do you want to tell me now which technologies you use and how well you know them? It takes 1-2 minutes and tells me where to start. If you prefer, I will ask about each one when it first appears in a project or a task." Options: now, or later (just in time). Recommend now.
3. If the user chose the survey now: ask in one block for their usual languages, frameworks, databases and test tools, each with a level (none / basic / medium / advanced, showing the one-line meanings from the `learn` skill's Tech profile). Accept a free list. If later: skip; tools will be asked when they first appear.
4. Write `{{ARTIFICER_HOME}}/data/profile.json`:
   `{"version": 2, "name": "Artificer", "language": "<lang>", "seniority": "junior|mid|senior", "default_level": "off|assist|core|full", "rpg": true|false, "created": "<YYYY-MM-DD>", "inline_explain_off_level": true, "tech": {"<tool>": {"self": "none|basic|medium|advanced", "since": "<date>", "evidence": "", "evidence_sessions": 0, "suggested": null}}}`
5. If `{{ARTIFICER_HOME}}/data/progress.md` or `character.json` are missing, create them from the templates in `{{SKILLS_DIR}}/learn/`. For `seniority: mid`, start every attribute at level 3; `senior` at level 5 (trials still gate every later level). Never touch existing ones.
6. Confirm in 2 lines and point to `{{ARTIFICER_HOME}}/README.md`. (AI tools are chosen when installing: `install.py`.)

If a profile already exists and the user only wants to change something, show the current values and edit only what they ask. A profile without `tech` (version 1): offer the tech survey once (now or later), and add `"tech": {}` either way.

## B. Project without STATUS.md (argument "project", or triggered automatically)
1. Explain in 3 or 4 lines: this project does not use the Artificer Method; the method gives control over what gets built (approved intent, examples and change map) and a focused review of every diff; the current default Learning level and what it means in one line.
2. Ask: set up the method now (`/artificer-setup`, recommended for anything that will grow) or work without it (code requests then use `/artificer-quick` sizes without project docs); and at which Learning level (default from the profile).
3. If set up: hand over to `/artificer-setup`. If not: set the output style for that level in the project's `.claude/settings.local.json` (table in `learning-levels.md`) and store the choice in `{{ARTIFICER_HOME}}/data/projects.json` as `{"<absolute project path>": {"level": "<level>", "since": "<YYYY-MM-DD>"}}` (merge with existing entries) so it is asked only once.
