---
description: ARTIFICER · Trivial and small work in one command (intent, examples, map, build, verify) without a full work item
argument-hint: '[change]'
model: sonnet
effort: medium
---
Use the artificer skill. Read the Learning level (`STATUS.md`, else `{{ARTIFICER_HOME}}/data/projects.json`, else the profile) and follow `learning-levels.md` for it.

Change: $ARGUMENTS

1. Size it: **trivial** (no behavior change: a text, a value, a line) or **small** (one behavior, one slice, at most 3 files, no data model change). Anything bigger: recommend `/artificer-spec` and stop.
2. Present, and wait for approval:
   - Intent (1-2 lines).
   - Decisions: any decision point (artificer skill, Decisions belong to the human), asked and decided by the user before the map; options only on request, in no order of preference, no recommendation. None: say "sin decisiones" in one line.
   - Small only: 1 to 3 Given/When/Then examples.
   - Active map (`learning-levels.md`): per file, the current code where the change goes (at `assist`+: ask the user's prediction first, then one question about one file). Ask the level of any tool missing from the tech profile.
   - Knowledge gate if the code is unknown to the user.
3. Git proposal for the branch `fix/short-name` or `feat/short-name` from an up to date `main` (artificer skill, Git proposals). Do not write code on `main`: wait until the user (or an express order at `automatic`) has created the branch.
4. Small: scenario tests first (red), then code, per level. Trivial: the change and the existing tests.
5. Gate through `test-runner`, then the two-pass review (artificer skill) per level, then show the diff and wait for its approval.
6. If the change alters a behavior described in a work item's examples, update those examples (living spec).
7. Note it in `STATUS.md` (projects with the method). Git proposal: commit `fix:` or `feat:`, push and PR against `main`. Update codemap, Review queue and XP.
