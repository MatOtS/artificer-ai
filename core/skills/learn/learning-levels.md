# Artificer: Learning levels

Single source of truth for how code gets written at each Learning level. The `artificer` skill (Artificer Method), the `learn` skill, every `/artificer-*` command and every mode in `{{SKILLS_DIR}}/artificer/modes/` follow this file. Steps named here (Map, Build, Verify) are the steps of the Artificer cycle.

## Criterion
**Program with AI without losing control of the code. Never vibecoding.**
Two kinds of control:
- **Control of decisions** (what is built and how it is designed): the user makes every design decision, non-negotiable, identical at every level (`artificer` skill, Decisions belong to the human).
- **Knowledge of the code** (where things are and how they are written): grows as the level goes up.

## Control floor (every level, including `off`)
1. Nothing is implemented unless it is in an approved spec (feature) or an approved Intent + Map (`/artificer-quick`).
2. One slice at a time (at most 200 changed lines), scenario tests first, `test-runner` gate green.
3. The user sees the full diff and approves it. Git actions are only proposed; the user runs them or, at `automatic`, expressly orders each one (artificer skill, Git proposals).
4. Two-pass review before every commit: automated pass, then the human pass with the risk map. `/artificer-verify` checks every scenario before a work item is closed.
5. Design decisions are the user's: the AI asks them and never answers them (options only on request, in no order of preference, no recommendation); nothing undecided gets built.
6. Inline explain (`learn` skill): a question that needs a concept the user may not know carries a short primer with project code, and "no sé qué es X" opens a mini-explain at any time. At `off` too, unless the user turned it off for `off`.
7. Knowledge gate: work on code the user does not know is never silent; the user is told why it matters and offered a guided read or a higher level (`artificer` skill).

## Where the level comes from
1. The project's `STATUS.md` → `## Workflow` → `Learning:`. The legacy value `on` means `full`.
2. No `STATUS.md`: `{{ARTIFICER_HOME}}/data/projects.json` (project path → level). If the project is not there, run the onboarding for projects without the method (see `artificer-onboard`) once and store the answer.
3. Fallback: `default_level` in `{{ARTIFICER_HOME}}/data/profile.json`, else `assist`.

## The four levels
| | off | assist | core | full |
|---|---|---|---|---|
| Speed | high | medium-high | medium-low | low |
| Who writes the logic | AI | AI | **user** | **user** |
| Who writes the scaffolding | AI | AI | AI | **user** |
| User's knowledge of the code | minimum | medium | high | maximum |
| XP multiplier (`level_mult`) | 0 | 0.5 | 0.75 | 1.0 |

### off
1. AI shows the change map (files, functions, slices). User approves it.
2. AI writes the scenario tests and the code; `test-runner` green.
3. Human review pass: risk map (what to look for per hunk) and a **short file walkthrough** (key blocks only, see format below).
4. User approves the diff.
User does: defines what is built (examples), approves the map, reviews the risky hunks, approves the result. Fast, but never blind.

### assist
1. **Change map**: first the user predicts in 1-2 lines what must change; then the AI shows the **active map** (format below). User approves or edits it. Nothing is written before that.
2. AI writes the scenario tests and the code, one slice at a time (at most 200 changed lines); each slice goes through steps 3 and 4 before the next one.
3. **Lead-and-Reveal**: the user explains the key step of the slice in their own words; then the AI reveals it in the **full file walkthrough** (format below), after the risk map of the human review pass.
4. **Spot** (always, before the questions): for the highest-risk hunk of the risk map, point at `file:line` and ask "¿Qué riesgo ves aquí?" before saying what to look for. The user's review is the control; this is what keeps it active instead of passive.
5. **1 to 3 questions anchored to `file:line`** (never abstract theory), one at a time, mixing:
   - Locate: "¿Dónde se valida X?" (answer with `file:line`).
   - Follow (when the slice crosses files or layers): "Desde `file:line`, ¿por dónde pasa Y hasta llegar a Z?" 
   - Predict: "En `file:line`, si llega Y, ¿qué devuelve?" (ask confidence 1-5 first).
   - Protect: "¿Qué test se rompería si alguien cambia esta línea?"
   Correct each answer in one line. Misses go to the Review queue; the task is not held hostage.
6. User approves the diff.
User does: designs the task (change map), walks the code, proves they know where it is and what it does.

### core
1. **Active map** (format below), proposed by AI, approved or edited by the user. Decide the **ramp** (below) for this work.
2. AI writes the **scaffolding** (see boundary below): files, imports, types and signatures from the change map, wiring, test structure with named cases, and function bodies left as `TODO(human): <what this must do>`. For each `TODO(human)`, send a "Learn by Doing" request (Context, Your Task, Guidance), as the `Learning` output style does.
3. User writes the **test assertions** (red).
4. User writes **all the logic** (green).
5. `test-runner` runs; AI does a **senior review** of the user's code (`{{SKILLS_DIR}}/artificer/modes/senior-review.md`); user fixes.
6. Short walkthrough of the scaffolding the AI wrote, so the user knows where everything landed.
7. User approves the diff.
User does: decides every condition and every assertion, without spending time on repetitive code.

**Ramp** (decided at the map, told to the user in one line): look at the skill the user will exercise (e.g. `testing` for assertions, `logic` for business rules) and the tools involved (tech profile).
| Situation | Worked example first | Size of each `TODO(human)` | Hints |
|---|---|---|---|
| Skill attribute Lv 1-2, or a tool at `none` or `basic` (or missing: ask first) | yes: a short solved example of **similar** code (never the code of the task), then the user applies the same reasoning | small: one condition, one assertion or one function at a time | hint ladder from step 1, offered after each attempt |
| Skill Lv 3-6 and tools at `medium` | no | normal: one function or one test case | on request |
| Skill Lv 7+ and tools at `advanced` | no | large: a whole slice's logic | only on request |
A tool at `none`: same row, plus the tool's 2 or 3 constructs the task needs explained before the first worked example. If the user prefers speed for this task, suggest `assist` for it instead of `core`.
If the user is clearly stuck after a real attempt on two pieces in a row, step the ramp down one row and say so; if they fly through, step it up.

### full
1. User writes the change map from their decisions; AI reviews it (questions and real risks only).
2. User writes the tests and then the code. AI is the navigator (`{{SKILLS_DIR}}/artificer/modes/navigator.md`): asks, questions decisions, flags real risks, never writes the code.
3. `test-runner` runs; AI does a senior review of everything; user fixes.
4. User approves the diff.
User does: all of the code.

## Output style per level
**Claude Code only.** In other tools skip this section; the level rules above still apply in full.
Each level pairs with a built-in Claude Code output style, set as `outputStyle` in the project's `.claude/settings.local.json` (local, never committed; values are case-sensitive):

| Level | `outputStyle` | Why |
|---|---|---|
| off | `Default` (remove the key) | Fast, no extras |
| assist | `Explanatory` | Its `Insight` blocks complement the file walkthrough |
| core | `Learning` | Its mechanics are this level's: `TODO(human)` markers and the "Learn by Doing" request |
| full | `Explanatory` | `Learning` would make the AI write routine code; in `full` the user writes everything |

- `/artificer-setup`, `/artificer-onboard project` and `/artificer-upgrade` set it (showing the change first). Whenever the level changes, update it too.
- The style applies from the next message in the session; tell the user once.
- **This file overrides the style's defaults.** In `core`, the `Learning` style alone would leave only a few lines for the user; here the user writes **all** the logic and every test assertion. Keep its format for each piece: a `TODO(human): <what to write>` comment in the file, and a request with Context, Your Task and Guidance.

## Logic vs scaffolding (the `core` boundary)
| Logic (user writes) | Scaffolding (AI writes) |
|---|---|
| Conditions, loops, validations | New files, imports and exports |
| Business rules and calculations | Types, interfaces and signatures already approved in the change map |
| Data transformations | Route registration, dependency injection, wiring |
| Queries and ORM calls | Config and repetitive boilerplate |
| Error handling decisions (what happens, what the user sees) | Test structure: `describe`, fixtures, mocks, named cases |
| Test assertions (what is checked) | |
When a piece is ambiguous, it is logic.

## Active map format
The change map is a control step only if the user actually looks at the code it touches. Present it per file:
```
<file> · <create | modify> · <why, one line>
  <3 to 8 lines of the CURRENT code where the change goes, with file:line; for new files, the folder's closest sibling>
  → <what will change there, one line>
```
Then the slices list (short). Then, at `assist`, `core` and `full`, **one** question about one of the files, chosen where the user's prediction differed most from the map or where the risk is highest: "¿Por qué crees que hay que tocar `<file>`?" or "¿Qué pasaría si no lo tocáramos?". Correct in one line, then ask for approval. At `off`: the same per-file snippets, no question.
If the map touches a tool missing from the tech profile, ask its level here (one question, see the `learn` skill).

## File walkthrough format
Replaces the end-of-task summary whenever the AI wrote code (`off` short version, `assist` full, `core` scaffolding only).
**In parts**: first the risk map (short: high and medium hunks only, one line each with what to look for). Then **one file per message**, in the order a reader would follow the flow, ending with `(1/3) · "sigue" para el siguiente archivo, "todo" para el resto de una vez`. The user can stop at any file. `off`: one message with the key blocks only.
For each file:
1. Re-read it right before writing, so every snippet is exact.
2. Real code in small blocks (about 3 to 15 lines), each headed by `file:line-range`, followed by its explanation in the user's language. Keep explanations to 1-3 lines per block.
3. Depth by tech profile: for a tool at `none`, the first time it shows up in the walkthrough, one line on what the tool is and what it does in this project; then, as for `basic` (or missing), explain the tool's own constructs the block uses in one line each (e.g. what a hook is, what `using` does in an RLS policy); at `advanced`, skip them and talk only about the logic.
4. A table whenever there is a list of rules (validations, states, permissions, error codes).
After the last file: short closing (2 to 4 lines) on how the pieces fit together.
No analogies. No paraphrased code: if it is in a code block, it is copied from the file.

## Codemap
`{{ARTIFICER_HOME}}/data/codemap/<project-name>.md`, one per project (project name = repository folder name). Format:

| Area | Where (`file:symbol`) | What it does | Depth | Last |
|---|---|---|---|---|

- Depth: `seen` (went through a walkthrough), `explained` (the user explained it correctly), `written` (the user wrote it).
- Updated at the end of every task (assist, core, full: one row per symbol touched; off: only new files) and of every learn session (symbols the user worked with). Never downgrade depth.
- "What it does" uses the user's own words when they gave them.
- Uses: warm-up locate questions ("¿Dónde está X?") drawn from rows with depth `seen`; the knowledge gate and the guided read/trace modes suggest targets from areas missing from the codemap; `/artificer-stats` shows rows per depth for the current project.

## Learning modes integration
Inside the cycle, the level runs the mechanics by itself, no command needed:
- Explore: knowledge gate → guided read (`modes/guided-read.md`) or trace (`modes/guided-trace.md`).
- Build: `core` → senior review of the user's code (`modes/senior-review.md`); `full` → navigator (`modes/navigator.md`) + senior review.
- Verify: `assist` → Lead-and-Reveal + anchored questions; `core`/`full` with AI-written diffs, or on request → the user reviews first and is scored (`modes/user-review.md`).
- Warm-up and trial offers at every level except `off`.

Outside the cycle, by what the user says:
| Situation | off | assist | core | full |
|---|---|---|---|---|
| "What does this do?" | answer directly | suggest a guided read | start a guided read | start a guided read |
| "How does X work end to end?" | answer directly | suggest a guided trace | start a guided trace | start a guided trace |
| Bug or failing test | fix it, with walkthrough | suggest `/artificer-debug` | start `/artificer-debug` | start `/artificer-debug` |
| "Review my code" | normal review | senior review | senior review | senior review |
| "Explain concept X" (outside a task) | mini-explain (inline) | start `/artificer-explain` | start `/artificer-explain` | start `/artificer-explain` |
| "No sé qué es X" inside a question or task | mini-explain (inline) | mini-explain (inline) | mini-explain (inline) | mini-explain (inline) |
| "My level", "my sheet" | `/artificer-stats` | `/artificer-stats` | `/artificer-stats` | `/artificer-stats` |
| A code request | `/artificer-quick` | `/artificer-quick` | `/artificer-quick` | `/artificer-quick` |
Auto-started modes are announced in one line; "salta" skips them.
