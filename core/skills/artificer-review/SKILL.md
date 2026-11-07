---
name: artificer-review
description: 'ARTIFICER · 5-minute spaced-review drill: asks the due items of the Review queue, oldest first, one short question each, and updates their intervals. Use when the user types /artificer-review, says "repaso" or "vaciar la cola", or when more than 5 review items are due.'
argument-hint: '[number of items, default 5]'
model: sonnet
effort: low
---
Follow the `learn` skill (profile language, Warm-up rules, calibration, progress protocol). Read-only on project files.

Items: $ARGUMENTS (default 5)

1. Read `{{ARTIFICER_HOME}}/data/progress.md` → `## Review queue`. Count the due items (`Next review` today or earlier). If none, say so in one line, show the next date, and stop.
2. Say in one line: how many are due, how many this drill covers. Ask the due items oldest first, one at a time:
   - One short question that makes the user **recall** the idea, never one that gives it away. Anchor it to the real code when the row has a `file:line` (open it to check the current code first; if the code changed, adapt the question).
   - For a prediction, ask confidence 1-5 first.
   - Correct or wrong, answer in one line. Correct: next interval (1 → 3 → 7 → 21; correct at 21 removes the row and updates the concept). Wrong: interval 1; if the miss shows the concept is not understood (not a slip), or the user says "no sé", a mini-explain (`learn` skill, Inline explain) before the next item.
3. Stop when the number is reached or the user says "basta". Rewrite the table (Warm-up table format) and update calibration.
4. XP: each correct answer is a tagged step of its attribute (`mode: warm-up`, `rpg.md`, session cap applies). Add a Session log line.
5. Close in 2 lines: done x of y due, the next due date, and the item that is coming back most often (suggest a guided read or `/artificer-explain` for it if it failed twice).
