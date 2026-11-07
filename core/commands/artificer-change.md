---
description: ARTIFICER · Changes the behavior of an existing work item, examples first, then map, then code
argument-hint: '[work item] [change]'
model: sonnet
effort: medium
---
Use the artificer skill. Do NOT touch code.

Work item: $1
Change (the text after it): $ARGUMENTS

1. If ambiguous, ask one question at a time (max 3).
2. Update `spec.md`: new or modified scenarios, out of scope. Set `Status: approved` only after approval (draft meanwhile).
3. Show the spec diff and which parts of `map.md` would change (new slices, changed files). If the change opens new decision points or touches an existing decision, ask them (artificer skill, Decisions belong to the human) before changing the map.
4. Wait for approval. Then add new unchecked slices to `map.md`.
5. If the work item's branch was merged, git proposal for `feat/NNN-name-change` from an up to date `main`; else keep working on it.
6. Update `STATUS.md`. Next step: `/artificer-build`.
