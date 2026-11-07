---
description: ARTIFICER · Shows where we are and the next command
argument-hint: '[work item] (optional)'
model: haiku
---
Do NOT modify any file.

Work item: $1

If a work item was given, read `work/<it>/spec.md`, `map.md` and `STATUS.md`, and reply with:
- Step of the cycle and spec status
- Slices done and pending (x of y)
- Blockers or open questions
- Exact next command

If not, read `STATUS.md` and `work/`, and reply with:
- Project phase and Learning level
- Active work item
- Table of work items with size, status and slices
- Blockers
- Exact next command

If the project still has `specs/` or `docs/constitution.md`, or no `Framework` line, add one line suggesting `/artificer-upgrade`.
