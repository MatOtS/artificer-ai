---
description: ARTIFICER · Cycle steps 6-7. Verifies the whole work item scenario by scenario, gives a verdict and closes it
argument-hint: '[work item]'
model: opus
effort: high
---
Use the artificer skill. Do NOT modify any code file.

Work item: $1

1. Read `spec.md`, `map.md` and the branch changes (`git diff main...HEAD`). Every slice must be checked; else stop.
2. Full tests, linter and type check through `test-runner`.
3. Table, scenario by scenario: scenario, test that covers it, result. Manual checks: verify with Chrome DevTools MCP (desktop and 375 px) or give the user a checklist.
4. Also check: the **decisions** in `map.md` (and project ADRs): any hunk that departs from one is a finding with `file:line` and the decision it breaks; non-functional requirements, `docs/principles.md`, and for UI `docs/design.md` (tokens, states, accessibility; web-design-guidelines skill if installed).
5. Risk review of the whole work item: the riskiest hunks across slices, what to look for, and whether the slices fit together (contracts, data). At `core` and `full`, before the verdict, ask the user which scenario they think is weakest and why, then compare.
6. Reply with the verdict format (artificer skill).
7. APPROVED and the user confirms: `Status: done` in the spec, update `STATUS.md`, then a git proposal: commit `docs(NNN): work item done`, push and PR against `main` (artificer skill, Git proposals; PR description with How to verify). The user decides the merge. Update the codemap and XP.
8. CHANGES REQUESTED: propose fix slices (`F1`, `F2`...) for `map.md`; when a fix needs a design choice, ask it as a decision point instead of choosing; once approved, add them. Next step: `/artificer-build`.
9. Third verification in a row with changes: stop and analyze with the user whether the problem is in the examples or in the map.
