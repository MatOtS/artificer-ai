# Artificer backlog

Ideas for the framework itself (not for projects). v0.2 (Artificer Method) absorbed B-008, B-012, B-013, B-015 and B-021; B-007 (cold start) is partly covered by predicting the map before seeing it. Add freely; nothing here is approved until it becomes a plan.

Format: `ID | title | impact (high/medium/low) | effort (S/M/L) | status (idea / exploring / planned / done / dropped)`, then notes.

## 1. Visual RPG (pixel art)
Inspiration: [agents-pixel-dungeon](https://github.com/JoseValencia125/agents-pixel-dungeon) (MIT, Rust + egui). Live coding agents as heroes in a pixel-art dungeon: each status is a room (workshop = working, sealed door = blocked, infirmary = session limit, reading room = idle, treasure room = done), each tool is a hero (wizard = Claude, alchemist = Codex), subagents are small heroes, plan usage shown as guild HP. Needs Herdr (a terminal agent host) as data source; has a `--demo` mode. Credits "Claude Dungeon" as its own inspiration.

- **B-001 | Pixel-art character sheet | high | M | idea**
  Replace or extend `sheet.html` with a pixel hero whose look changes with the overall rank (Trainee rags → Mid armor), the nine attributes as equipment slots or stat bars, achievements as pixel badges. Static HTML/CSS, sprites as inline PNG/SVG. No new dependencies. Natural first step.
- **B-002 | Dungeon map of the project | high | L | idea**
  SDD as a dungeon: each spec is a dungeon floor, each task a room (locked / in progress / cleared), validate is the boss door, trials are boss fights. Rendered from `specs/*/tasks.md` and `STATUS.md`. Could live in the same HTML page as the sheet.
- **B-003 | Codemap as explored map | medium | M | idea**
  Fog of war over the project's folders: areas the user has `seen` / `explained` / `written` (codemap) get revealed; unknown code stays dark. Makes "knowledge of the code" visible.
- **B-004 | Live agent view à la agents-pixel-dungeon | low | L | idea**
  Fork or adapt it with an Artificer adapter (Learning level per agent, XP events). Heavy: Rust app plus Herdr. Only if B-001/B-002 prove the visual layer is worth it.
- **B-005 | Pixel art source | medium | S | idea**
  Decide where sprites come from: free packs with a compatible license, commissioned, or drawn (Aseprite). Keep NOTICE/credits like agents-pixel-dungeon does.

## 2. Skill atrophy: staying sharp without losing speed
Evidence so far: Shen & Tamkin 2026 (Anthropic RCT, 52 mostly junior devs): AI group 17% lower comprehension, biggest drop in debugging, no significant speedup; engaged use (asking explanations, conceptual questions) preserved learning. Atrophy pattern described in the literature: speed drops first, then accuracy, then ability; recovery needs deliberate practice. Common advice: short scheduled no-AI practice, no AI for the first hour of new work, only delegate what you could explain yourself.

- **B-006 | Research note on skill atrophy | high | M | exploring**
  Deeper review (studies, not blogs): what decays first, how fast, what restores it. Output: `docs/research-skill-atrophy.md` with sources and what it changes in the framework.
- **B-007 | Cold start rule | high | S | idea**
  For new or hard work, the user writes a first attempt (approach, pseudocode or first function) before the AI writes anything. Could be an option of `assist` or a per-task flag ("cold").
- **B-008 | "Could I explain it?" delegation check | medium | S | done (v0.2: knowledge gate in Explore)**
  Before an `off` or `assist` task, one question: "¿Podrías explicar cómo se hace esto?". If no, suggest `core` for that task. Based on "only delegate what you understand".
- **B-009 | Weekly gym quota | high | S | idea**
  A small weekly target (e.g. 30 to 60 min of `core`/`full` or `/learn-*`), tracked in the sheet as a fitness bar. Keeps practice regular without slowing daily work.
- **B-010 | Atrophy early warning | high | M | idea**
  Detect decline from data already logged: share of tasks at `off`/`assist` per week, Review queue misses per attribute, calibration drifting to overconfidence, rusty flags. Warn and suggest the exercise that targets it.
- **B-011 | Katas from your own code | medium | M | idea**
  Short no-AI exercises built from the user's real projects (re-implement a function from its tests, predict outputs), instead of LeetCode-style problems.

## 3. Human code review: the new bottleneck
Context: generation got cheap, verification did not. Reports in 2026: more hours reviewing AI code than writing code, many AI pull requests merged with no real review, larger PRs. Common strategies: automate routine checks so humans review intent and design, keep the author accountable for AI output, small PRs, explicit rules for AI-authored changes, track review metrics.

- **B-012 | Review map before the diff | high | M | done (v0.2: risk map in Verify)**
  Before the user reviews, the AI ranks hunks by risk (logic changed, data, security, untested paths) and marks what is mechanical. The human reviews in that order and skips nothing, but spends attention where it matters.
- **B-013 | Two-pass review | high | S | done (v0.2: two-pass review)**
  Pass 1 automated (linter, tests, `/code-review` for nits and bugs). Pass 2 human, focused only on intent vs spec, design and risks. The human pass is never skipped.
- **B-014 | Intent-first PR description | medium | S | idea**
  PR template that starts from the spec: FRs covered, what to verify by hand, known risks, what the AI wrote vs what the user wrote (by level).
- **B-015 | Review budget per task | medium | S | done (v0.2: 200-line slices)**
  Hard cap on diff size per task (e.g. ~100-200 lines) so every diff stays reviewable; bigger tasks must be split in `/sdd-tasks`.
- **B-016 | Reviewing XP from real PRs | medium | M | idea**
  `learn-review-pr` on real pull requests (own or teammates' via `gh`), so daily review work trains the Reviewing attribute.
- **B-017 | Review metrics | low | M | idea**
  Track time to review, PR size, findings caught by human vs automated pass. Shown in the sheet.
- **B-027 | Task time tracking and estimates per Learning level | high | M | exploring**
  Goal: measure how long work takes and compare Learning levels (`off` / `assist` / `core` / `full`) with data instead of feel (e.g. whether `core` is really slower, and by how much). Idea: each cycle step logs start and end (Intent, Map, Build per slice, Verify) into `~/.claude/learning/` with project, work item, size, level and changed lines; the sheet shows time per level and per size, and estimate vs actual.
  Inspiration: [lidr-it-estimator-demo](https://github.com/MatOtS/lidr-it-estimator-demo) (MIT, fork of LIDR.co; Rails + FastAPI + pgvector + OpenAI). It does **not** track time: it estimates hours for tasks by vector search over a corpus of past budgets (weighted consensus of similar tasks; tasks with no close precedent are flagged instead of guessed), with two human review checkpoints. Reusable ideas, without its stack: (1) estimate a slice from **our own** logged slices with similar size and level, (2) flag "no precedent" honestly, (3) estimate vs actual as a calibration signal, like the confidence calibration.
  Decided (2026-11-02): timing is the user's responsibility. The user marks it in chat with four exact phrases: **"empiezo el cronometro"** (start), **"pauso el cronometro"**, **"sigo el cronometro"** (resume after a pause) and **"termino la tarea, fin del cronometro"**; paused time is excluded so idle time does not pollute the data. Capture with a Claude Code `UserPromptSubmit` hook that matches those words and appends a timestamped line to a local JSON lines file (exact time, independent of the model remembering), tagged with project, active work item and level from `STATUS.md`. Nothing is timed without an explicit "empiezo el cronometro".
  Open questions: matching tolerance (accents, case, punctuation: "cronómetro" vs "cronometro"); what happens with an "empiezo" never closed (ask at the next session); whether time per level is a fair comparison (different tasks); privacy (local only). No new dependencies: a small hook script, JSON lines and `learn-sheet`.

## 4. Framework
- **B-018 | Real run at every level | high | S | planned**
  Verify `off`, `assist`, `core`, `full` on a real task; fix what does not work.
- **B-019 | Upgrade existing projects | high | S | planned**
  Run `/artificer-upgrade` on projects that already use an earlier version; in-progress work items are finished as legacy or converted.
- **B-020 | Package as a Claude Code plugin | high | L | idea**
  Repo with `.claude-plugin/plugin.json`, `commands/`, `skills/`, `agents/`, `hooks/`, `output-styles/`, `bin/`; installed with `/plugin marketplace add` + `/plugin install`, removed and updated the same way. Notes: plugin commands get the plugin name as prefix (check: `/artificer:spec`); a plugin cannot write the user's `CLAUDE.md`, so `ARTIFICER-RULES.md` would be loaded by a SessionStart hook or the Artificer output style (B-023); user data stays in `~/.claude/learning/` (never inside the plugin folder, which is replaced on update). Needs B-025.

- **B-021 | Command prefix | medium | M | done (v0.2: `/artificer-*`, no aliases)**
  Decide whether `/sdd-*` and `/learn-*` become `/artificer-*` (or keep both as aliases).
- **B-022 | Sheet language from profile | low | S | idea**
  `learn-sheet` UI text is Spanish only; read `language` from the profile.
- **B-023 | Artificer output style | medium | M | idea**
  Custom output style in `output-styles/` with the level rules built in (`keep-coding-instructions: true`), reading the level itself instead of mapping to Default / Explanatory / Learning. Keep it short: how to talk and work; level detail stays in `learning-levels.md`. Best shipped with the plugin (B-020), which can force it with `force-for-plugin`. Caveats: an instruction, not a guarantee; does not reach subagents; adds tokens per response.
- **B-024 | Integrations for other AI tools | low | M | idea**
  Codex CLI, Gemini CLI, Cursor, Copilot: generate their command/rules formats from `~/.claude` like `sync-opencode` does, only for tools listed in the profile's `integrations`. Build each one when someone actually uses it.
- **B-025 | Manifest, install and uninstall | high | M | idea**
  A manifest listing every Artificer file and the version; `install.sh` (copies files, adds the `@~/.claude/ARTIFICER-RULES.md` line to `CLAUDE.md` without touching the rest, onboarding on first session); `uninstall.sh` (backup first, shows the list and asks, keeps `learning/` unless asked, never deletes project files: lists what Artificer left in each project and what is safe to remove vs the user's work in `docs/` and `work/`). Superseded by the plugin for plugin users.
- **B-026 | Artificer files under git | high | S | idea**
  A private repository with only the Artificer files (commands, skills, agents, `bin/`, `ARTIFICER-RULES.md`, README, BACKLOG, ROADMAP, MIGRATIONS), never `learning/` (personal data) nor the rest of `~/.claude` (sessions, caches, settings). Gives history and easy rollback of framework changes, replaces the `.tar.gz` backups, and is the base of the plugin (B-020) and the manifest (B-025). Either a repo outside `~/.claude` that the files are copied or linked from, or a repo in `~/.claude` with a strict allowlist `.gitignore`. Repo creation, commits and pushes only as git proposals run on the user's order.
- **B-028 | Review and explain confidence calibration | medium | S | idea**
  What calibration measures and how to read it in the sheet is not clear enough. Two parts: (1) explain it well: a short plain explanation in the sheet (what is asked, what the four counters mean, what "calibrado", "sobreestimarte" and "subestimarte" mean, and what to do about each); (2) review the mechanics in `learn` (Confidence calibration) and `learn-sheet` `calibration()`: thresholds (30% wrong at high confidence, 70% right at low) are arbitrary; the verdict is global, not per attribute; confidence 3 is discarded; small samples flip the verdict with a single answer; max 2 questions per session makes it slow to fill. Consider per-attribute calibration, a range instead of a verdict while data is small, and linking it to B-027 (estimate vs actual time as a second calibration signal).
