---
name: artificer-stats
description: ARTIFICER · Shows the user's character sheet (overall rank, attributes, XP, calibration, codemap coverage, achievements) and renders the visual HTML sheet. Use when the user asks for their level, stats, XP, progress or sheet ("mi nivel", "mis stats", "mi ficha").
argument-hint: '[--open] (also open the HTML sheet in the browser)'
allowed-tools: Read, Bash({{PYTHON}} {{ARTIFICER_HOME}}/core/bin/learn-sheet:*)
model: haiku
effort: low
---
Reply in the language set in `{{ARTIFICER_HOME}}/data/profile.json`. Do not modify any file yourself: the script writes the HTML.

1. Run `{{ARTIFICER_HOME}}/core/bin/learn-sheet --text` and show its output as is, inside a code block. It is computed from `{{ARTIFICER_HOME}}/data/character.json`, so never recompute or round numbers yourself.
2. Read the `## Learn path` and `## Gaps` sections of `{{ARTIFICER_HOME}}/data/progress.md` and add, in at most 3 lines: the next recommended mode and why, and the top open gap.
3. Run `{{PYTHON}} {{ARTIFICER_HOME}}/core/bin/learn-sheet` (add `--open` if the user passed it or asked to see it) and give the path of the generated `sheet.html`.
4. If more than 5 review items are due, suggest `/artificer-review`.
5. If a trial is available, end with the exact command to start it (`/artificer-trial <attribute>`).
