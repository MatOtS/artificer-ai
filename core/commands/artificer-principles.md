---
description: ARTIFICER · Project. The user decides the non-negotiable engineering principles (docs/principles.md)
argument-hint: '[additional context]'
model: sonnet
effort: medium
---
Use the artificer skill. Do NOT write code.

Context: $ARGUMENTS

1. Read `docs/product.md`, `STATUS.md` and the code if it exists (existing project: principles come from conventions the code already follows).
2. If information is missing, ask in a single block (max 4): who maintains the code and their level, simplicity or scalability, type of data handled, UI language.
3. Principles are decisions of the user (artificer skill, Decisions belong to the human). Go through the topics of `templates/principles.md` one at a time and ask what the rule is. Existing project: list the conventions the code already follows, as data with `file:line`, and ask which ones become principles. Options only on request (in no order of preference, no recommendation). Write them short and verifiable (about 6, 15 lines max) in the user's terms. The test command can stay `[PENDING: architecture]`.
4. Don't write the file yet: show it and wait for approval. Then write `docs/principles.md` and update `STATUS.md`. Next step: `/artificer-design` (UI) or `/artificer-architecture`.
