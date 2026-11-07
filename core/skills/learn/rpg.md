# RPG progression rules

Principle: **XP measures effort and always grows (the reward). Level measures competence and only moves after a passed trial (the truth).** Never round up, never level up without a trial, never award XP without evidence.

Numbers live in `{{ARTIFICER_HOME}}/data/character.json`. Always read it before awarding, write it after, and never edit numbers by hand outside these rules.

## Attributes
All nine attributes are core: the overall rank is the lowest of them.

| Key | Name shown | Primary mode | Also trained inside |
|---|---|---|---|
| `reading` | Reading | guided read (`modes/guided-read.md`), assist checkpoints, Lead-and-Reveal | |
| `tracing` | Tracing | guided trace (`modes/guided-trace.md`), Follow questions in assist checkpoints | |
| `reviewing` | Reviewing | user review (`modes/user-review.md`), Spot question in every assist slice, risk-map findings at any level | |
| `debugging` | Debugging | `artificer-debug` | |
| `code_writing` | Code Writing | `navigator`, `senior-review` | |
| `knowledge` | Knowledge | `artificer-explain` | |
| `logic` | Logic | (no own mode) | `guided-read` (tricky predictions), `artificer-debug` (hypotheses), `artificer-explain` (exercises) |
| `testing` | Testing | (no own mode) | `navigator` (tests first), `senior-review` and `user-review` (test review), `artificer-debug` (prevention test) |
| `data` | Data | (no own mode) | `guided-trace` (DB hop), `guided-read` (schemas, queries, migrations), `user-review` (data changes) |

### Secondary blocks
Logic, Testing and Data have no mode of their own. Every learn-* mode that lists them above includes a **secondary block**: 2 to 4 questions or a short task focused on that attribute, inside the same session. Pick the block for the lowest of the three attributes the mode can train (ties: the one with the oldest `last_session`). Skip it only if the code at hand gives nothing real to ask.
- A secondary block earns its own XP entry with the full formula (its own hint step and result), its own evidence and `mode` set to `<mode>+block`. It does not take XP away from the primary attribute.
- Block types:
  - **logic**: predict the exact output for a tricky input (empty, null, boundary, negative); find the input that breaks a condition; simplify a condition without changing behavior; pseudocode for a tiny problem.
  - **testing**: list the cases a function needs (normal, edge, error); write or describe one test that checks behavior; **light mutation**: the AI proposes a one-line change to the code (`>` to `>=`, removed validation) and the user says whether the existing tests would catch it and why; read a failing test and explain what it says.
  - **data**: explain a schema (tables, relations, keys); predict the rows a query or ORM call returns (including joins with nulls); spot N+1, missing indexes or possible inconsistent data; sketch the tables for a small feature.

### Tagged steps
Every step of a mode is tagged with the attribute it trains (see each mode's `## XP map`). At close, award XP per attribute:
| Entry | XP |
|---|---|
| Primary attribute of the mode | full formula |
| Secondary block | full formula |
| Tagged steps of another attribute | formula with **half base** (L1 10, L2 20, L3 30), using that attribute's own highest hint step and result |

- A tagged-step entry needs **at least 2 answers from the user** on steps with that tag, each with evidence. One answer is not enough.
- Tagged steps of the primary attribute just feed the primary entry; tagged steps of the block's attribute feed the block entry.
- **Cap: at most 4 attributes earn XP in one session.** If more qualify, keep the primary, the block, and the tagged attributes with the most answers (ties: the lowest attribute level).
- Log each entry separately with `mode` set to `<mode>`, `<mode>+block` or `<mode>+steps`.

### assist checkpoints
- Each checkpoint answer inside a task at `assist` is tagged: change-map prediction → `code_writing` (or `logic` for the algorithm); Lead-and-Reveal and locate questions → `reading`; Follow questions → `tracing`; predict → `logic`; protect → `testing`; data questions → `data`; Spot question and any risk-map finding by the user → `reviewing`. Same formula with the `assist` level multiplier (0.5) for every entry.
- Max 3 attributes per slice, and `reviewing` (Spot) always counts within them; a tagged attribute needs only 1 answer here (checkpoints are short by design).
- At `off`, `core` and `full`, a finding the user raises during the human review pass also gives a `reviewing` entry (level multiplier applies).
- `mode: assist-checkpoints`. "rápido" or "salta" gives 0 XP.

### Mode names
Valid `mode` values in `xp_log`: `guided-read`, `guided-trace`, `user-review`, `senior-review`, `navigator`, `assist-checkpoints`, `core-build`, `full-build`, `verify-review`, `artificer-debug`, `artificer-explain`, `artificer-trial`, `warm-up`, optionally with `+block` or `+steps`. Never the retired `learn-*` names (they remain only in old history).

## XP formula
`xp = floor(base * hint_mult * result_mult * other_mult)`

- `base` by exercise level: L1 20, L2 40, L3 60.
- `hint_mult` by the highest hint ladder step used in the session: 1 → 1.0, 2 → 0.8, 3 → 0.5, 4 → 0.3, 5 → 0.1. No hints at all counts as step 1.
- `result_mult` from the closing summary or final answer: correct 1.0, partial 0.6, wrong 0.2.
- `other_mult` (multiply together when several apply, otherwise 1.0):
  - Same topic (same file, flow or concept) already logged for this attribute in the last 7 days: 0.5.
  - Inside a task (any `/artificer-*` build), the Learning level multiplier: `off` 0, `assist` 0.5, `core` 0.75, `full` 1.0 (see `learning-levels.md`).
- Zero XP when the user said "salta", or when the answer came from the AI rather than the user.
- `evidence`: one line with `file:line` (or the concept) and what the user actually did right or wrong. No evidence, no entry.

## Levels
- Attribute levels go from 1 to 10. XP needed to fill the bar from level n: `xp_to_next = 100 * n`.
- XP beyond `xp_to_next` is kept (the bar shows full).
- A full bar never raises the level. It sets `trial.status` to `available` (unless it is `failed` and waiting for practice, see Trials).
- Exercise difficulty follows the attribute level: Lv 1-3 → L1, Lv 4-6 → L2, Lv 7-10 → L3 (scopes in `levels.md`).

## Ranks
| Level | Rank |
|---|---|
| 1-2 | Trainee |
| 3-4 | Junior I |
| 5-6 | Junior II |
| 7-8 | Junior III |
| 9-10 | Mid |
| 11+ | Senior (locked: criteria to be defined on reaching Mid) |

**Overall rank** = rank of the lowest level among all attributes (every attribute is core).

Real-world meaning per attribute (always show it next to the rank, it is what keeps the title honest):

| Rank | Reading | Tracing | Reviewing | Debugging |
|---|---|---|---|---|
| Trainee | Explains a short function with help | Follows one call from caller to callee with help | Spots naming issues and obvious bugs with help | Reproduces a bug and describes it precisely |
| Junior I | Explains a function and predicts its outputs alone | Follows one hop alone, naming the data that flows | Finds obvious bugs and missing cases in a small diff | Isolates the failing function and proposes a testable hypothesis |
| Junior II | Explains a module: contract, side effects, error paths | Traces a feature within one layer, including the error path | Reviews a medium diff for correctness, edge cases and tests | Finds root causes inside one layer with a systematic method |
| Junior III | Explains a feature across layers and its trade-offs | Traces a full request UI → API → DB and back | Reviews for architecture, coupling and security | Debugs issues that cross layers (client, server, data) |
| Mid | Predicts the impact of a change across the codebase | Traces async, background and cross-service flows | Reviews design decisions and proposes alternatives | Debugs intermittent, timing or environment-dependent bugs |

Code Writing: Trainee writes with heavy guidance; Junior I small features with review; Junior II features with tests first; Junior III features across layers with clean boundaries; Mid designs a feature and its tests alone.
Knowledge: Trainee knows the vocabulary; Junior I explains core language concepts; Junior II explains framework internals used daily; Junior III compares approaches with trade-offs; Mid teaches concepts to others accurately.
Logic: Trainee follows simple conditions with help; Junior I predicts outputs including empty and boundary inputs; Junior II finds the input that breaks a condition and simplifies conditionals; Junior III reasons about state changes and loop invariants; Mid reasons about concurrency and ordering.
Testing: Trainee reads a test and says what it checks; Junior I lists normal, edge and error cases for a function; Junior II writes behavior tests that catch light mutations; Junior III chooses unit vs integration and designs fixtures and mocks; Mid defines the testing strategy of a feature.
Data: Trainee explains a table and its columns; Junior I explains relations and keys in a schema; Junior II predicts query and ORM results, including joins with nulls; Junior III spots N+1, missing indexes and consistency risks; Mid models data for a feature and plans migrations.

### Senior gate
When any attribute reaches Lv 8, say once at close: "Has llegado a Lv 8 en <attribute>: es momento de diseñar juntos los niveles 11-15 (Senior)." Those levels will need external evidence (real PRs reviewed by others, design docs, production post-mortems) besides trials. Do not invent their criteria before that conversation.

## Trials
- Offered at close when `trial.status` is `available`: "Prueba disponible: <Name> → Lv n+1 (/artificer-trial <key>)". The user may take it now or later. Run with the `artificer-trial` skill.
- One real exercise from the user's project at the **next** level's difficulty.
- Max hint step 2. Using step 3 or higher ends the trial as failed.
- Scored against the rubric below: each criterion met / not met, with evidence. Pass at 80% or more (4 of 5).
- Pass: level + 1, subtract the old `xp_to_next` from `xp`, compute the new `xp_to_next`, `trial.status = locked` (or `available` again if the remaining XP already fills the new bar).
- Fail: level unchanged, `trial.status = failed`, `failed_criteria` recorded and copied to Gaps in `progress.md`. It goes back to `available` only after at least one practice session in that attribute logged after `trial.last_attempt`.

### Rubrics (5 criteria each, adapted to the level's scope)
- **reading**: 1) purpose in one correct sentence; 2) inputs and outputs complete; 3) side effects identified; 4) correct prediction for a non-trivial input; 5) error or edge path explained.
- **tracing**: 1) entry point found alone; 2) every hop named as `file:function` in order; 3) data shape and transformations at each hop; 4) error path back to the user; 5) final sequence diagram matches the real path.
- **reviewing**: 1) every must-fix found; 2) at least half of the should-fix found; 3) at most one false positive; 4) each finding justified with a principle; 5) one-sentence summary of the change is correct.
- **debugging**: 1) reproduction steps precise; 2) failure isolated to the right area; 3) hypothesis testable and checked; 4) root cause explained (not just the symptom); 5) prevention proposed (test, validation or rule).
- **code_writing**: 1) approach explained before coding; 2) tests first for the business rules; 3) code correct for the spec; 4) readable names and structure; 5) decisions justified when questioned.
- **knowledge**: 1) concept explained in own words; 2) minimal correct example; 3) when to use it and when not; 4) a common pitfall named; 5) explained back correctly after a follow-up question.
- **logic**: 1) correct prediction for a tricky input; 2) breaking input found; 3) step-by-step reasoning stated; 4) equivalent simplification of a condition; 5) correct pseudocode for a tiny problem.
- **testing**: 1) case list complete (normal, edge, error); 2) test checks behavior, not implementation; 3) light mutation correctly judged (caught or not, and why); 4) failing test read and explained; 5) one missing test proposed for the mutation that slipped through.
- **data**: 1) schema explained (tables, relations, keys); 2) query result predicted exactly; 3) a performance or consistency risk spotted; 4) data flow to and from the DB explained; 5) small model sketched with keys and relations.

## Audit ("audita mi nivel")
- Surprise trial at the **current** level of the attribute the user names (or the highest attribute if none).
- Pass: clear `under_review`, reset `audit_fails` to 0, award normal XP.
- Fail: `flag = under_review`, `audit_fails + 1`. At 2 failed audits in a row, level - 1 (XP set to 0 for the new level), flag cleared, audit_fails reset. Say it plainly.

## Rust
At the start of every learn session, check dates:
- Attribute with `last_session` older than 45 days: `flag = rusty` (level kept). Cleared by the next session in that attribute.
- Concepts in `progress.md` not seen for 60 days: mark them `(rusty)`.

## Achievements
Award once, with date and evidence. Check at every close. Cumulative counts live in `counters` (e.g. `must_fix_caught`, incremented by user-review); streaks are computed from `xp_log` dates.
| id | Name | Condition |
|---|---|---|
| `first-steps` | Primeros pasos | First learn session logged |
| `first-trial` | Primera prueba | First trial passed |
| `rank-up` | Ascenso | Overall rank goes up for the first time |
| `clean-read` | Lectura limpia | A guided-read session with result correct and no hints |
| `full-trace` | Ida y vuelta | First L3 trace completed with result correct |
| `bug-hunter` | Cazador de bugs | Root cause found without going past hint step 2 |
| `sharp-eye` | Ojo crítico | 10 must-fix findings caught across reviews (cumulative) |
| `no-false-alarm` | Sin falsas alarmas | A review with every must-fix found and zero false positives |
| `streak-week` | Semana constante | 5 sessions within 7 days |
| `all-rounder` | Polivalente | Every attribute at Lv 3 or higher |
| `comeback` | Sin óxido | A rusty attribute cleared |
| `honest-check` | Examen sorpresa | An audit passed |
| `edge-finder` | Caza-límites | Logic block: found the breaking input with no hints |
| `mutant-killer` | Mutante cazado | Testing block: correctly judged 3 light mutations in one session |
| `query-oracle` | Oráculo SQL | Data block: predicted a join result with nulls exactly |

## Chat card
Print at the end of every session that awarded XP (profile language, monospace, one line per attribute that earned XP, then achievements and trials). Bar: 10 cells, filled = floor(10 * min(xp, xp_to_next) / xp_to_next).
```
+32 XP Reading   (L2 · hint 2 · correcto)   Junior I · Lv 4  ▰▰▰▰▰▰▱▱▱▱ 260/400
+20 XP Logic     (bloque · hint 1 · correcto)  Trainee · Lv 2   ▰▰▰▱▱▱▱▱▱▱  70/200
+10 XP Tracing   (pasos · hint 2 · parcial)    Trainee · Lv 1   ▰▰▰▰▰▱▱▱▱▱  55/100
Logro desbloqueado: Ida y vuelta
Prueba disponible: Lectura → Lv 5 (/artificer-trial reading)
```
