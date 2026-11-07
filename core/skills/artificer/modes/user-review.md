# Mode: User review with scoring

Used by the Artificer cycle in: Verify (user reviews first and is scored), or any PR the user must review. Not a command: the `artificer` skill and the `/artificer-*` commands load this file when the step needs it. Log XP with `mode: user-review`.

Follow the `learn` skill: shared rules, hint ladder, levels and progress protocol.

Target: the target given by the cycle or the user (empty: the current `git diff`, staged and unstaged; if empty, the current branch against `main`)

## Setup
- Get the diff (`git diff`, `git diff main...HEAD` or `gh pr diff <n>`). Read it and the related `work/NNN-name/spec.md`, `map.md` and `docs/principles.md` if they exist.
- Prepare your own review silently, using the `senior-review.md` criteria: correctness, readability, efficiency, architecture, good practices, tests. Classify each finding as must fix, should fix or nice to have. Do NOT show it yet.
- Tell the user which files to review and in what order (smallest or most central first). At L1 point at the 1 or 2 hunks that matter most.

## The user's review
Ask the user to write their review in this format, all at once or file by file:
`file:line | must fix / should fix / nice to have | what and why`
Also ask for one sentence on what the change does overall. Do not hint at findings while they review, unless they ask for help; then use the hint ladder.

## Scoring
Show a table:
| Your finding | Verdict (correct / partially / false positive) | Comment |
Then:
- **Missed**: each finding from your review they did not catch, with `file:line`, severity and the principle behind it. For the most important miss, ask a guiding question first and reveal only if they do not see it.
- **Score**: caught must-fix x of y, should-fix x of y, false positives n.
- One thing they reviewed well.

If this review is part of a slice's commit approval, end by reminding the user that the decision to approve the diff and to run (or order) the commit is still theirs, and list the must-fix items that should be addressed first.

## XP map
Tag each of the user's answers with its attribute and award XP at close following `rpg.md` (Tagged steps, max 4 attributes):
- Primary: `reviewing` (findings, severities, scoring).
- `reading`: the one-sentence summary of the change.
- `logic`: findings about edge cases and conditions.
- `testing`: findings about tests.
- `debugging`: **How it would show up**: for one must-fix the user found (or after revealing one), ask "¿cómo se manifestaría este bug en producción y cómo lo detectarías?".
- Block: `testing` or `data`.

## Secondary block
Include one secondary block for testing or data as defined in the `learn` skill's `rpg.md` (Secondary blocks), placed where it fits naturally, and log its XP as a separate entry.

## Close
Run the progress protocol. Record missed categories (e.g. "edge cases with empty input", "missing tests") as gaps.
