---
description: ARTIFICER · Cycle steps 3-4. Explores the code (knowledge gate) and writes the change map split into slices of at most 200 lines
argument-hint: '[work item]'
model: opus
effort: high
---
Use the artificer skill. Do NOT write code.

Work item: $1

1. Read `spec.md` (must be `approved`, no `[NEEDS CLARIFICATION]`; else stop), `docs/principles.md`, `docs/architecture.md`, `docs/design.md` and the project `{{PROJECT_RULES}}`.
2. **Explore** without touching anything: find the code involved (codebase-memory MCP if indexed, else grep/read; delegate wide searches to `Explore` or `codebase-memory-scout`). If Context7 MCP is available, check the docs of the libraries involved.
3. **Knowledge gate** (artificer skill): compare the involved files and symbols with the user's codemap and, if needed, explain why and offer: guided read/trace, `core`, `full`, or continue. Respect the choice.
4. **Decisions** (every level; artificer skill, Decisions belong to the human): from what Explore found, list the decision points of this work item as open questions (context, `one-way` or `reversible`, max about 5, one-way first) and cite the existing decisions that already apply (principles, architecture, earlier maps). If the work clashes with one of them, add it as a decision point to revisit (artificer skill): keep it or change it, the user decides. Never answer them; options only on request (in no order of preference, no recommendation); a data-based suggestion only if the user asks or says they are stuck. After each answer, flag only real risks. Record each one with the user's reason. Do not draw the map until every decision point is decided.
5. At `assist`, `core` and `full`: before showing the map, ask the user which files and functions they think must change (1-2 lines). Then compare. At `full` the user writes the map from their decisions; you review it.
6. If the work touches a tool missing from the tech profile (`learn` skill), ask its level (one question). Write `work/NNN-name/map.md` from `templates/map.md`, following the user's decisions only: explored context, change map (file, action, functions and signatures, scenarios), slices of at most 200 changed lines in dependency order, each with its scenarios and a verifiable "Done when", data changes, decisions (decided by, the user's reason), risks. Every scenario covered by at least one slice. More than 6 slices: propose splitting the work item.
7. Present it as the **active map** (`learning-levels.md`, Active map format): per file, the current code where the change goes and what will change; then the slices and the user's decisions it follows; at `assist`/`core`/`full`, one question about one file. At `core`, state the ramp in one line. Wait for approval.
8. Once approved: git proposal for the `feat/NNN-name` branch from an up to date `main` (artificer skill, Git proposals). Update `STATUS.md`. Next step: `/artificer-build NNN S1` (once the branch exists).
