# Artificer migrations

Current version: see `{{ARTIFICER_HOME}}/VERSION`. A project several versions behind gets every entry in order (oldest first). Every change to the framework that affects existing projects adds an entry here, newest first. `/artificer-upgrade` applies every entry newer than the project's version, in order.

Version line in a project: `STATUS.md` → `## Workflow` → `- Framework: Artificer v<version>`. No line means **unversioned**.

## v0.4 (alpha) · from v0.3
First public version: Artificer is installed from its own repository for Claude Code, Codex, GitHub Copilot (VS Code) and OpenCode. Nothing changes in projects.
1. Tell the user in 1 line that the framework is now installed from a repository and works with several AI tools; their project needs no change.
2. Update `- Framework: Artificer v0.4`.

## v0.3 (alpha) · from v0.2.2
The human decides what is built and how, at every level. Never touches code, specs or maps.
1. Tell the user in 3 lines what changes in their work: the AI now asks every design decision (stack, structure, patterns, hooks, data, contracts) and never answers it; options only on request, with pros and cons, in no order of preference and without a recommendation; a data-based suggestion only when they ask or say they are stuck. `/artificer-map` starts with the decisions, Build stops on anything undecided, Verify checks the diff against the decisions.
2. **Project `{{PROJECT_RULES}}`** → `## Rules`: add the line "The human decides what is built and how: the AI asks design decisions, never answers them (options only on request, in no order of preference, no recommendation) and stops on anything undecided." (show it first).
3. **Work items in progress**: list the ones with unchecked slices in one line each. Their maps keep their old Decisions table (not touched here); `/artificer-build` will ask the user to confirm or change their one-way decisions before the next slice.
4. Update `- Framework: Artificer v0.3`.

## v0.2.2 (alpha) · from v0.2.1
Active map, walkthrough in parts, `core` ramp, tech profile. Never touches code.
1. Tell the user in 3 lines what changes in their work: the change map now shows the current code of each file and asks one question; walkthroughs come one file at a time ("sigue"); `core` adapts the size of the user's pieces and adds a worked example when the skill or tool is new.
2. **Tech profile**: detect the project's stack (manifest, lockfile, config). For tools missing from `{{ARTIFICER_HOME}}/data/profile.json` → `tech`, ask their level in one block (none / basic / medium / advanced). The user may skip; they will be asked when the tools appear in a task.
3. Update `- Framework: Artificer v0.2.2`.

## v0.2.1 (alpha) · from v0.2
Git and review fixes. Never touches code.
1. **Mode meaning changed** (tell the user in 2 lines, keep the current value): `manual` now means the AI only proposes branch, commit message and PR description and the user runs them; `automatic` means the AI proposes and runs each action only on the user's express order. Nothing git-related happens on its own in either mode, and no AI attribution is ever added.
2. A project without a `## Workflow` section now defaults to `manual` (was `automatic`).
3. Update `- Framework: Artificer v0.2.1`.

## v0.2 (alpha) · from v0.1
The Artificer Method replaces SDD. Commands `/sdd-*` no longer exist; use `/artificer-*`. Never touches code.

Changes to apply, one at a time, each shown and approved:
1. **Folders**: `specs/` → `work/` (keep the `NNN-name` folders). `docs/discovery.md` → `docs/product.md`. `docs/constitution.md` → `docs/principles.md`. Use plain `mv` (git detects the renames; staging and committing are a git proposal, never automatic); when `Artificer files: local-only`, also update `.git/info/exclude` (replace the old paths with the new ones).
2. **Workflow**: rename `SDD files` → `Artificer files`. Rename the phases in `STATUS.md` (discovery → product, constitution → principles, development → building), `Active spec` → `Active work`, the `## Specs` table → `## Work items` (add the Size column: `feature` for existing specs).
3. **Specs in progress** (status `draft` or `approved` with unchecked tasks): **Ask** per spec: (a) finish it as is (its FRs and `tasks.md` keep being the contract; `/artificer-build` reads them as legacy) and convert it when done, or (b) convert it now. Recommend (a) when more than half of its tasks are done.
4. **Convert a spec** (done specs, and in-progress ones the user chose to convert), one spec at a time:
   - `spec.md`: keep Context as **Intent** (2-3 lines). Turn each FR into one or more Given/When/Then scenarios (EARS `WHEN x, THE SYSTEM SHALL y` → `When x / Then y`; add the Given from the edge cases). Non-functional, edge cases not covered by scenarios, out of scope and open questions keep their sections. `Status: implemented` → `done`.
   - `plan.md` + `tasks.md` → `map.md`: Files table → change map; Logic, Algorithm, UI and Data → explored context and data; Decisions and Risks kept; tasks → slices (`T3` → `S3`, checkbox state kept, FR references → scenario names).
   - Show the full converted spec and map; the user approves each before writing. Remove the old `plan.md` and `tasks.md` only after approval (they stay in git history).
   - Existing tests are not renamed; mention which scenarios have no matching test yet (they will be covered when touched).
5. **Project `{{PROJECT_RULES}}`**: replace references to the `sdd` skill, `docs/constitution.md` and `specs/` with the `artificer` skill, `docs/principles.md` and `work/`.
6. Update `- Framework: Artificer v0.2`.

## v0.1 (alpha) · from unversioned
First numbered version. Anything before it is treated as unversioned.

Changes to apply:
1. **Workflow settings**: `## Workflow` must contain Ownership, Mode, SDD files and Learning, plus the new `Framework` line. Add any missing setting by asking the user (same options and recommendations as `/sdd-setup`).
2. **Learning level** now has four values: `off | assist | core | full` (see `{{ARTIFICER_HOME}}/build/skills/learn/learning-levels.md`).
   - `on`: its meaning changed (before: the AI wrote the code and then explained it; now there is no `on`). **Ask** which of the four levels the user wants, explaining each in one line. Do not convert silently.
   - `assist`: keeps its name, but now includes the change map before writing, the file walkthrough with exact code, and questions anchored to `file:line`. Tell the user in one line and keep it unless they want another level.
   - `off`: unchanged in meaning; it now ends tasks with a short file walkthrough instead of a summary. Tell the user in one line.
   - Missing: ask (recommend the profile's `default_level`).
3. **Project `{{PROJECT_RULES}}`**: if it lacks the `## Verification` or `## Rules` sections of `{{ARTIFICER_HOME}}/build/skills/artificer/templates/project-rules.md`, propose adding them (respect `SDD files: local-only` + tracked `{{PROJECT_RULES}}`: then only list them and ask).
4. **Codemap**: nothing to change in the project. Mention that `{{ARTIFICER_HOME}}/data/codemap/<project>.md` will start filling with the next task.
5. **Output style**: set `outputStyle` in the project's `.claude/settings.local.json` for the (possibly new) Learning level, per the table in `learning-levels.md` (`off`: leave unset). This file is local and never committed.
6. **`TODO(human)`**: the convention for code the user must write is `TODO(human)` (Claude Code's Learning output style). If the project has leftover `TODO(you)` markers from earlier, list them (`grep -rn "TODO(you)"`) and offer to rename them; this is the only change that may touch code files, and only the marker text.
7. Add `- Framework: Artificer v0.1` to `## Workflow`.
