# Artificer

Version: **v0.3 (alpha)** · see `skills/artificer-upgrade/VERSION` and `MIGRATIONS.md`.

In fantasy worlds, the artificer builds their own mechanical creatures: designs them, assembles them piece by piece, and knows them so well they never turn against their maker. No improvised magic; blueprints, runes and rules.

This framework makes you that. The AI is your creation and you direct it. You write the blueprints (intent, examples and change maps), you decide how much you build with your own hands, and you stay someone who knows every piece, never a spectator of what the machine does on its own.

## What it is

### In one sentence
A method to program with AI without losing control of the code, that also makes you a better developer while you work.

### In one paragraph
It is a **framework for AI-assisted development** that runs inside Claude Code. It separates two kinds of control:
- **What gets built and how**: always decided by you. You define the intent and the Given/When/Then examples, and you make every design decision (stack, structure, patterns, hooks, data, contracts). Claude asks the decisions and never answers them: options only when you ask, with pros and cons, in no order of preference and without a recommendation; a data-based suggestion only when you ask for it or say you are stuck. Earlier decisions are cited, not asked again, but they can be revisited: when new work clashes with one, Claude says so and you decide whether to keep it or change it (the old one is marked superseded).
- **How the code gets written**: regulated by you with a level that goes from "the AI writes everything" to "I write everything".

At any level, the framework guarantees that you understand and approve every change, and it honestly measures how well you actually know the code.

### Its pieces
| Piece | What it is | Question it answers |
|---|---|---|
| Criterion | Control of the code, never vibecoding | Why does this exist? |
| Artificer Method | The working cycle: Intent, Examples, Explore, Map, Build, Verify, Close | What do I build and how do I organize it? |
| Learning (off, assist, core, full) | The level of control and speed | How much of the code do I write today? |
| Learning inside the work | Guided reads on unknown code, your own reviews, Lead-and-Reveal, debug and explain | How do I keep learning while I ship? |
| Character sheet | The honest measure of your level | How much do I really know? |
| Model routing | Which AI model does what | How do I make it efficient? |

### What it is NOT
- **Not vibecoding**: no code is accepted that you have not approved or that is not in a spec.
- **Not a course**: you learn on your real projects, not on made-up exercises.
- **Not just a game**: the sheet is a thermometer, not the goal. It can be turned off.
- **Not just a spec method**: specs alone give you control of the what, but not knowledge of the code, and they do not make reviews better.

### Who it is for
Developers who use AI every day and do not want to become spectators of their own code. Especially juniors, who run the highest risk of never really learning, as Anthropic's study showed. Also anyone who wants to keep command of code that AI writes more and more.

### What kind of thing it is, technically
Today it is a **Claude Code configuration**: commands, skills, agents and a script. In the future, an **installable plugin**. But that is the format, not the identity. The identity is the method.

### What sets it apart
**Adjustable control with measured knowledge.** There are spec-driven methods (such as GitHub's spec-kit) and there are systems to learn programming, but joining both with a level of control that you regulate is what makes this framework its own.

Ideas: `docs/BACKLOG.md` · Plan: `docs/ROADMAP.md` · Method: `skills/artificer/SKILL.md`.

## Quick start
1. `/artificer-onboard`: short guide and your profile (`learning/profile.json`: language, seniority, default level, character sheet on/off).
2. In a project: `/artificer-setup` (ownership, git mode, Learning level). Then `/artificer-product` → `/artificer-principles` → `/artificer-design` (UI) → `/artificer-architecture`.
3. Work: `/artificer-spec` → `/artificer-map` → `/artificer-build` (one slice at a time) → `/artificer-verify`. Small things: `/artificer-quick`.
4. Check yourself: `/artificer-stats`. Old project: `/artificer-upgrade`.

## The method
Built from pieces that already work: approvals per phase and project docs (spec-driven development), examples as the spec (behavior-driven development), red then green (test-driven development), explore before planning (Claude Code's recommended workflow), small batches and focused review (review research), plus the learning layer.

| Step | Command | What happens | Your control |
|---|---|---|---|
| 1 Intent | `/artificer-spec` | problem and who it is for, 2-3 lines | write or approve |
| 2 Examples | `/artificer-spec` | Given/When/Then scenarios = the spec | approve: it is the contract |
| 3 Explore | `/artificer-map` | AI reads the code; knowledge gate on code you don't know | choose: guided read, higher level, or continue |
| 4 Map | `/artificer-map` | first the decisions (Claude asks, you decide), then files, functions, signatures from them; slices of max 200 lines | decide, then approve |
| 5 Build | `/artificer-build` | scenario tests first, then code, per Learning level | per level |
| 6 Verify | `/artificer-build`, `/artificer-verify` | automated pass, then your pass with a risk map | approve the diff, always |
| 7 Close | `/artificer-verify` | all scenarios green, PR | approve |

Sizes: **trivial** and **small** go through `/artificer-quick`; **feature** uses the four cycle commands.
Project docs: `docs/product.md`, `docs/principles.md`, `docs/design.md`, `docs/architecture.md`, `docs/backlog.md`. Work items: `work/NNN-name/spec.md` and `map.md`. Status and settings: `STATUS.md` (Ownership, Mode, Artificer files, Learning, Framework).
Git: Claude never runs git on its own. Every git step is a **git proposal** (branch, commit message, PR description, exact commands). `manual`: you run them. `automatic`: Claude runs each one only when you expressly order it ("hacé el commit"). Approving a diff is not an order. No AI attribution, ever.
Other commands: `/artificer-change` (examples first), `/artificer-status`, `/artificer-backlog`, `/artificer-deploy`, `/artificer-metrics`.

## Learning levels
Full definition: `skills/learn/learning-levels.md` (single source of truth).

| What you do | off | assist | core | full |
|---|---|---|---|---|
| Make every design decision (what and how) | yes | yes | yes | yes |
| Approve intent, examples and the change map | yes | yes | yes | yes |
| Predict the map before seeing it | | yes | yes | you write it |
| Explain the key step before seeing the code (Lead-and-Reveal) | | yes | | |
| Answer questions anchored to `file:line` | | yes | | |
| Write the scenario test assertions | | | yes | yes |
| Write the logic | | | yes | yes |
| Write the scaffolding | | | | yes |
| Review with the risk map and approve the diff | yes | yes | yes | yes |
| XP multiplier | 0 | 0.5 | 0.75 | 1.0 |

Each level also sets Claude Code's output style in the project's `.claude/settings.local.json`: `off` Default, `assist` Explanatory, `core` Learning (`TODO(human)` + "Learn by Doing"), `full` Explanatory.
Whenever the AI wrote code, the end-of-slice summary is replaced by a **file walkthrough** with the exact code, **one file at a time** ("sigue" for the next). The change map is **active**: it shows the current code of each file it will touch and asks you one question. At `core`, a **ramp** sizes your pieces (and adds a worked example) when the skill or the tool is new to you.
**Inline explain**: explanations live inside the questions. When a question needs a concept that seems new to you (tool at `none`/`basic`, a gap, unknown code), it comes with a 2-3 line primer using your project's code; "no sé qué es X" opens a short mini-explain at any time and then goes back to the question; longer gaps go to the Review queue and a full `/artificer-explain` session after the task. On at every level, `off` included ("apagar explicaciones" turns the primers off at `off`).
**Tech profile**: you declare your level per tool (none / basic / medium / advanced; `none` = 100% new) in onboarding (optional survey), at project start or when a tool first appears in a task. It is a starting point, never XP: if the evidence disagrees over 3 sessions, Claude proposes a new level and you decide. Shown in `/artificer-stats`. Every symbol you touch goes to your **codemap** (`learning/codemap/<project>.md`: seen / explained / written).

## Learning inside the work
- In the cycle (no command): guided read or trace when you touch unknown code (knowledge gate), your own review with scoring, senior review of the code you write, navigator at `full`. Files: `skills/artificer/modes/`.
- Outside the cycle: `/artificer-debug` (bugs), `/artificer-explain` (concepts), `/artificer-review` (5-minute drill of the due Review queue items), `/artificer-stats` (sheet, calibration, review queue, tech, codemap coverage), `/artificer-trial` (level-up trials, "audita mi nivel").
- "salta" skips an auto-started mode; "rápido" gets just the result.

## Character sheet (`skills/learn/rpg.md`)
- Nine attributes, all count for the overall rank: Reading, Tracing, Reviewing, Debugging, Code Writing, Knowledge, Logic, Testing, Data.
- XP shows effort; levels only go up by passing a trial. Ranks: Trainee, Junior I-III, Mid; Senior locked until Mid.
- Numbers live in `learning/character.json`; `bin/learn-sheet` renders them (`--text`, `--open`).
- Progress, learn path, gaps and Review queue: `learning/progress.md`.

## Learning science applied
- Lead-and-Reveal (Kazemitabaar et al., IUI 2025): explaining before seeing aligns perceived and real ability.
- Illusion of progress in juniors using AI (Prather et al., ICER 2024): the reason for the knowledge gate and calibration.
- Engaged AI use preserves learning, blind delegation erodes it (Shen & Tamkin, 2026).
- Spaced warm-up (Review queue, 1/3/7/21 days, max 2 new items per session, variants merged; `/artificer-review` drains a backlog), predict before reveal, confidence 1-5 calibration, faded guidance and top-down reading (`skills/learn/levels.md`).
- Focused, small reviews (automation bias; detection drops past ~400 lines): risk map and 200-line slices.

## Versions and upgrades
- Every project records its framework version in `STATUS.md` (`- Framework: Artificer v<x>`).
- When the framework changes in a way that affects projects, add an entry to `skills/artificer-upgrade/MIGRATIONS.md` and bump `VERSION`.
- `/artificer-upgrade` updates a project step by step, with your approval. It never touches code. Sessions in outdated projects suggest it in one line.

## Model routing
| Tier | Model | Used by |
|---|---|---|
| Lookup | haiku | `/artificer-status`, `/artificer-backlog`, `/artificer-stats`, agents `codebase-memory-scout`, `test-runner` |
| Doing | sonnet | `/artificer-build`, `/artificer-quick`, `/artificer-change`, `/artificer-setup`, `/artificer-product`, `/artificer-principles`, `/artificer-design`, `/artificer-deploy`, `/artificer-metrics`, `/artificer-debug`, `/artificer-explain`, `/artificer-onboard`, `/artificer-upgrade`, agent `codebase-memory` |
| Thinking | opus | `/artificer-spec`, `/artificer-map`, `/artificer-verify`, `/artificer-architecture`, `/artificer-trial`, agent `codebase-memory-auditor` |

Session default: Sonnet. Change model or effort per session only when a task clearly needs it.

## Agents (`agents/`)
- `test-runner` (haiku): runs tests/lint, returns only failures.
- `codebase-memory-scout` / `codebase-memory` / `codebase-memory-auditor`: graph lookups at three depths (haiku / sonnet / opus).

## Rules and other AI tools
- Artificer's global rules live in `ARTIFICER-RULES.md`; your `CLAUDE.md` imports them with one line (`@~/.claude/ARTIFICER-RULES.md`) and keeps only your personal rules.
- Other AI coding tools are optional, chosen in `/artificer-onboard` (`integrations` in the profile). Today only **OpenCode** has an integration: it reads `~/.claude/skills` natively, and `~/.claude/bin/sync-opencode` generates its commands and an `AGENTS.md` with the rules inlined. Run it after editing commands or adding an `artificer-*` skill; it does nothing if OpenCode is not enabled. OpenCode-only config (models, its agents and plugin) stays in `~/.config/opencode/`.

## Backups
- `~/claude-config-backup-2026-10-13.tar.gz` and `~/claude-config-backup-2026-10-26.tar.gz`: full config before each reorganization.
- `~/claude-config-old-2026-10-13/` and `~/claude-config-old-2026-10-26/`: retired commands and skills (old learn modes, SDD).
- `~/claude-md-backup-2026-10-28.md`: `CLAUDE.md` before the rules split.
