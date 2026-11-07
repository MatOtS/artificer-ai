---
description: ARTIFICER · Adds an idea to the backlog or shows it prioritized
argument-hint: '[idea] (empty to view the backlog)'
model: haiku
---
Do NOT implement anything.

Idea: $ARGUMENTS

- If there is an idea: add it to `docs/backlog.md` with the format `- <date> | <idea> | Impact: high / medium / low | Spec: none`. Confirm in one line.
- If empty: show the backlog sorted by impact, with the data you have for each (impact, size, dependencies). The user chooses the next work item (a priority is a software decision: no recommendation unless they ask or say they are stuck; then a data-based suggestion). Then `/artificer-spec` (or `/artificer-quick` if it is small).
