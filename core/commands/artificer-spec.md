---
description: ARTIFICER · Cycle steps 1-2. Intent and Given/When/Then examples (the spec), hunting for missing scenarios until approved
argument-hint: '[short-name] [idea]'
model: opus
effort: high
---
Use the artificer skill. Do NOT write code at any point.

Short name: $1
Idea (the text after the name): $ARGUMENTS

1. Read `STATUS.md`, `docs/product.md`, `docs/principles.md` and `docs/backlog.md`. Read the Learning level.
2. Create `work/NNN-$1/spec.md` from `templates/spec.md` (next free number). Propose a size (trivial, small, feature); trivial or small → suggest `/artificer-quick` instead and stop if the user agrees.
3. **Intent**: write 2-3 lines from the idea; ask one question at a time (max 3) only if the problem or the user is unclear.
4. **Examples**: behavior is the user's decision (artificer skill, Decisions belong to the human). Write as scenarios only what the user stated; every outcome they did not state (an error, a boundary, a permission) becomes a question ("¿Qué pasa si el importe es 0?"), never an answer of yours. At `core` and `full`, before showing your draft, ask the user to write the one scenario they think matters most, then compare.
5. **Hunt for missing scenarios**, as a demanding QA, numbered: ambiguous outcomes (not observable), contradictions between scenarios, missing boundaries (empty, zero, limit, limit + 1), missing error paths, conflicts with principles. Ask them one at a time; the user decides each outcome; update the spec with their answer.
6. Only the WHAT and WHY: no stack, architecture or file names. Non-functional only if measurable. Unresolvable questions stay as `[NEEDS CLARIFICATION]`.
7. Show the final spec. When there is no `[NEEDS CLARIFICATION]` and the user approves, set `Status: approved`. If the idea was in the backlog, mark it.
8. Update `STATUS.md`: active work, next step `/artificer-map`.
