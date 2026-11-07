---
description: ARTIFICER · Cycle steps 5-6. Builds ONE slice per the Learning level, tests from the examples first, then the two-pass review
argument-hint: '[work item] [slice, e.g. S2]'
model: sonnet
effort: medium
---
Use the artificer skill. Read the Learning level in `STATUS.md` (legacy `on` = `full`) and follow `{{ARTIFICER_HOME}}/build/skills/learn/learning-levels.md` for it.

Work item: $1
Slice: $2 (if empty, the first unchecked slice in `map.md`)

Legacy work item (a `specs/NNN/` folder the user chose to finish before converting): the task in `tasks.md` is the slice and its FRs are the scenarios; write `tasks.md` checkboxes instead of `map.md`.

1. Read the slice in `map.md`, its Decisions (the user's, binding), its scenarios in `spec.md`, `docs/principles.md` and the project `{{PROJECT_RULES}}`. Warm-up from the Review queue if the level is not `off` (max 1 item). Map written before v0.3: confirm its one-way decisions with the user first (artificer skill).
2. Announce in 2 lines: the slice, its scenarios, the files.
3. **Tests first**: one test per scenario of the slice, named after it, in the project's test framework; run them through `test-runner`: they must fail. Who writes them depends on the level (AI at `off`/`assist`; at `core` the AI writes the structure and the user the assertions; at `full` the user).
4. **Code** until they pass, per level (AI at `off`/`assist`; at `core` the user writes the logic in the `TODO(human)` bodies, following the ramp: worked example first and small pieces when the skill or tool is new; at `full` the user writes everything, AI navigates with `modes/navigator.md`).
5. Full tests, linter and type check through `test-runner`. Nothing is done with anything red. If the slice exceeds 200 changed lines, stop and propose splitting it.
6. Visual changes: Chrome DevTools MCP on desktop and 375 px, console checked.
7. **Verify, pass 1**: `/code-review` (or equivalent) on the slice's diff; fix what it finds (at `core`/`full`, the user fixes their code).
8. **Verify, pass 2 (human)**: at `assist`, Lead-and-Reveal first (the user explains the key step, then you reveal). Then the risk map (high / medium / mechanical, what to look for per hunk) with the Spot question on the riskiest hunk (`assist`), the file walkthrough per level **in parts** (one file per message, "sigue" for the next), and at `assist` 1-3 questions anchored to `file:line` (Follow when the slice crosses files). At `core`/`full`: senior review (`modes/senior-review.md`). At any level, a risk the user raises in this pass is logged as `reviewing` XP (`mode: verify-review`).
9. Check the slice `[x]` in `map.md`. Show the full diff and wait for the user's approval of the diff. Then a **git proposal** (artificer skill): commit message `feat(NNN): S<n> <description>`, files with Markdown marked tracked/excluded, exact commands. Run nothing unless the project is `automatic` and the user expressly orders it. Never push here.
10. Update `STATUS.md`, codemap, Review queue and XP (`learn` skill). Last slice: next step `/artificer-verify`.

Reply with: slice and scenarios covered, files, test and lint result. Then STOP. Anything the decisions do not cover (a new dependency, pattern, hook, file location, data change) is a missing decision: stop and ask before writing it, never improvise. Same if the slice cannot be built as decided: stop, quote the decision and what clashes, and ask whether to keep it or change it. If the slice or the map is wrong or impossible, stop and explain.
