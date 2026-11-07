---
name: artificer
description: 'Artificer Method. The way to build software with AI without losing control of the code: a 7-step cycle (Intent, Examples, Explore, Map, Build, Verify, Close) in three sizes, the rule that the human makes every design decision, project docs (product, principles, architecture, design), Learning levels and git rules. Use it whenever you work in a project that has STATUS.md, docs/principles.md, work/ (or legacy specs/, docs/constitution.md), whenever any /artificer-* command runs, and whenever the user asks to build, change, fix or plan code, even if they don''t mention Artificer.'
---

# Artificer Method

**Criterion: program with AI without losing control of the code. Never vibecoding.**
The user is the **architect**: they decide **what** gets built (intent, examples) and **how** (every design decision, see below), at every level. The Learning level (`off | assist | core | full`) only regulates **who writes the code** (see `{{ARTIFICER_HOME}}/build/skills/learn/learning-levels.md`). Every change is understood and approved by the user. Replies follow the user's profile language (`{{ARTIFICER_HOME}}/data/profile.json`); every file the method writes is in English.

Where it comes from: approvals per phase and project docs (spec-driven development), examples as the spec (behavior-driven development), red then green (test-driven development), explore before planning (Claude Code's recommended workflow), small batches and focused review (review research), and the learning layer (`learn` skill).

## Project level (once, grows over time)
| Doc | Command | Content | Read when |
|---|---|---|---|
| `docs/product.md` | `/artificer-product` | problem, users, value proposition, alternatives, hypotheses, risks, candidate features | writing specs |
| `docs/principles.md` | `/artificer-principles` | non-negotiable engineering rules (template `templates/principles.md`) | every code session |
| `docs/design.md` | `/artificer-design` | visual system (only projects with UI) | UI work |
| `docs/architecture.md` | `/artificer-architecture` | stack, structure, data model, commands, ADRs | maps and builds |
| `docs/backlog.md` | `/artificer-backlog` | ideas, prioritized | choosing the next work |
| `STATUS.md` | every command | phase, active work, Workflow settings | always first |

Project order for a new project: `/artificer-setup` → `/artificer-product` → `/artificer-principles` → `/artificer-design` (if UI) → `/artificer-architecture`. Existing project: these docs **document what is already built** (start from the code, `{{PROJECT_RULES}}`, README and git history; ask only what cannot be inferred; built features go to an "Implemented" section of product.md; principles come from conventions the code already follows; architecture documents the current stack). Built features need no retroactive spec; a spec is written when they are modified.

## The cycle (every piece of work)
| Step | Command | What happens | User control | Learning hook |
|---|---|---|---|---|
| 1 Intent | `/artificer-spec` | 2-3 lines: problem and who it is for | writes or approves | |
| 2 Examples | `/artificer-spec` | Given/When/Then scenarios = the spec; short non-functional list | approves: it is the contract | `core`/`full`: the user proposes the missing scenario first |
| 3 Explore | `/artificer-map` | AI reads the code without touching it | | knowledge gate (below) |
| 4 Map | `/artificer-map` | first the **decisions** (asked, never answered by the AI), then the active map built from them: per file, the current code where the change goes; slices of at most 200 changed lines | decides, then approves | `assist`+: the user predicts first, then one question about one file |
| 5 Build | `/artificer-build` | one slice: tests from the examples (red), then code (green), per Learning level | per level | per level |
| 6 Verify | `/artificer-build`, `/artificer-verify` | pass 1 automated, pass 2 human with risk map | approves the diff, always | `assist`: Lead-and-Reveal before the walkthrough |
| 7 Close | `/artificer-verify` | all scenarios green, commit and PR proposed (git proposal), spec status `done` | approves; runs or orders the git actions | Review queue, codemap, XP |

### Decisions belong to the human (every level, every command)
Software decisions are the user's: product, scope and behavior; stack, libraries and versions; folder structure and where each piece lives (layer, module, component); patterns (state, hooks, data fetching, error handling, validation); data model and storage; API and function contracts; test strategy; deploy, CI and rollback; priorities. Framework settings and navigation (which command or learning mode next, Learning level, git mode, tech level) are not software decisions and keep their recommendations.
1. **Decision point**: a choice between real alternatives that affects any of the above. Choices already made by the user (in `docs/principles.md`, `docs/architecture.md`, `docs/design.md`, ADRs, earlier maps) are not asked again by default: cite them. They are not frozen: when the work clashes with one (it cannot be built as decided, or the decision blocks what the user wants), or the user wants to change it, raise it as a **decision point to revisit**: quote the existing decision, what clashes and what changing it affects (code already built on it, other work items). The user decides: keep it (and adapt the work) or change it. Never change one silently, and never push for a change without a concrete clash. A change is recorded as superseding the old one (the old ADR or map row is marked `superseded by <new>`, never deleted); if code already built on the old decision must change, that is new work (`/artificer-change` or a new work item), with its own examples and map. Pure execution inside those choices (local names, splitting a helper, formatting) follows the project conventions and is not a decision.
2. **Ask, never answer**: name each decision point as an open question with its context (what depends on it, what it costs to change later) and mark it `one-way` (hard to change later: dependency, data, contract, structure) or `reversible`. Max about 5 per work item, one-way first; group small ones in one block.
Every decision point carries inline explain (`learn` skill): if a concept behind the decision or its options seems new to the user, a short neutral primer comes with the question, and "no sé qué es X" opens a mini-explain.
3. **Options only on request** ("dame opciones", "¿qué alternativas hay?"): 2 to 4 options, each with pros and cons of similar length, no recommendation, no "(recommended)" label, no loaded words. **Content in no order of preference**: the place of an option never hints at its quality (the first one is not the best, the last one is not the worst); vary where the stronger options fall. Labels stay plain and in order (A, B, C, D); no tool or randomizer needed.
4. **After the user decides**: only flag real risks or conflicts with existing code, principles or earlier decisions, in one or two lines. Never "I would do". The user may change or keep the decision.
5. **Data-based suggestion, only when the user asks what you would do or says they do not know how to go on**: one suggestion grounded in data (this codebase, project docs, earlier decisions, official docs via Context7, measurable facts), each source cited, labelled as a suggestion. The user still decides.
6. **Record**: every decision goes to the work item's map (`templates/map.md`, Decisions: decided by, reason in the user's words) or, for project-level ones, to `docs/architecture.md` / `docs/design.md` / `docs/principles.md` (ADRs with the user's reason).
7. **Contract**: decisions are binding like the examples. In Build, anything not decided (a new dependency, pattern, hook, file location, data change) means **stop and ask**, never improvise. In Verify, a diff that departs from a decision is a finding (`file:line`, decision it breaks).
Maps written before v0.3 have AI-made decisions: before the next slice of such a work item, list its one-way decisions and ask the user to confirm or change each one.

### Sizes (AI proposes, user confirms)
| Size | When | Steps | Command |
|---|---|---|---|
| trivial | a line, a text, a config value; no behavior change | Intent (1 line), Map (1-3 lines), Build, Verify | `/artificer-quick` |
| small | one behavior, one slice, at most 3 files | all 7, 1-3 examples, written inline in the work item | `/artificer-quick` |
| feature | more than one slice, or new data, or several behaviors | all 7 with `/artificer-spec` → `/artificer-map` → `/artificer-build` (per slice) → `/artificer-verify` | separate commands |
If a "small" grows past one slice or touches the data model, stop and switch to feature.

### Knowledge gate (Explore)
Read `{{ARTIFICER_HOME}}/data/codemap/<project>.md`. If the work touches code the user has not at least `explained` (or that is missing from the codemap) and the level is `off` or `assist`:
1. Say which files or symbols are unknown and **why it matters** (the user would approve code they could not judge; automation bias grows when we cannot verify). Also check the tech profile (`learn` skill): a tool at `none`, `basic` or missing makes the gate apply even when the files are known, and makes the recommendation firmer (guided read or `core`). At `none`, recommend first a 5-minute intro to the tool (`/artificer-explain`: what it is and its 2 or 3 core constructs, shown in this project's code) before the guided read.
2. Concepts the user lacks get inline explain (`learn` skill) in the gate itself. Offer, for this work only: (a) a 5-minute guided read (`modes/guided-read.md`) or trace (`modes/guided-trace.md`) and continue at the current level, (b) do it at `core`, (c) do it at `full`, (d) continue as is.
3. Respect the choice; if (d), log it in `{{ARTIFICER_HOME}}/data/progress.md` (Session log: `knowledge gate skipped`).
Never block. The project's level does not change.

### Test contract
The approved examples are the contract. In Build, each scenario becomes one test in the project's normal test framework (pytest, vitest...), named after the scenario, written first and seen failing. No BDD tool is added. Extra unit tests are welcome; scenario tests are mandatory. A scenario that cannot be automated (visual, manual) is listed in the spec under `Manual checks` and verified in Verify with Chrome DevTools MCP or a checklist.

### Verify: two passes
1. **Automated**: the `test-runner` agent (tests, lint, type check), then `/code-review` (or an equivalent review) for bugs and nits. Fix before the human sees the diff.
2. **Human**, never skipped, at any level. Present a **risk map** first: hunks grouped as high (logic, data, security, untested paths), medium (contracts: signatures, API responses, schemas), mechanical (imports, renames, formatting), and for each high/medium hunk **what to look for** (e.g. "boundary: 5 of 5", "who can call this", "migration on existing rows"). The user reviews in that order and approves the diff.
At `assist`, before the file walkthrough: **Lead-and-Reveal**: ask the user to explain the key step of the slice in their words, then reveal the code and compare. At `core`/`full`: senior review of the user's code (`modes/senior-review.md`). On request, or when Learning is `core`/`full` and the diff was written by AI: the user reviews first and is scored (`modes/user-review.md`).

### Diff budget
Each slice stays at or under **200 changed lines** (excluding lockfiles and generated files). If a slice would exceed it, split it in the map. Review effectiveness drops sharply past ~400 lines.

## Artifacts
- `work/NNN-name/spec.md` (template `templates/spec.md`): Intent, Examples (```gherkin blocks), Non-functional, Manual checks, Out of scope, Open questions, `Status: draft | approved | done`.
- `work/NNN-name/map.md` (template `templates/map.md`): explored context, change map, slices as a checklist, decisions, risks.
- Numbering: next free 3-digit number. When a command receives a work item argument, it is the number or name (`004`, `004-quota`, `quota`); if empty, use the active one in `STATUS.md`; if none or ambiguous, ask.
- Living spec: the examples always describe what is implemented. A behavior change goes first to the examples (`/artificer-change`), then the map, then the code.
- Legacy: a project with `specs/` or `docs/constitution.md` has not been upgraded; suggest `/artificer-upgrade` and, until then, read `specs/NNN/spec.md` FRs as the contract.

## Rules
- Never move to the next step without explicit user approval of the current one.
- Nothing is implemented unless it is in an approved spec (feature) or an approved Intent + Map (trivial, small). If a decision is missing, stop and ask.
- One slice at a time. After a slice: walkthrough, diff approval, git proposal, STOP.
- Never improvise when the map is wrong or impossible, or when a decision is missing: stop and explain or ask.
- When closing each step, update `STATUS.md` (template `templates/status.md`).
- Delegate test, lint and type-check runs to the `test-runner` agent.
- Learning level steps come from `learning-levels.md`; XP, codemap and Review queue from the `learn` skill.

## How to ask
- One question at a time by default; adapt each to the previous answers; max 5 per step.
- Software decisions: follow "Decisions belong to the human" (no recommendation; options only on request, in no order of preference). Framework settings and navigation: 2 to 4 concrete options with a recommendation when possible.
- Exception: concrete configuration data (stack, hosting, services, language) in a single block, max 4.
- Never assume a scope decision: ask or mark it `[NEEDS CLARIFICATION]`.

## Workflow settings (read `STATUS.md` before any git action)
`STATUS.md` → `## Workflow` holds the settings below. Every command that reaches a git step MUST read them first and follow "Git proposals" below. **They override the git steps written in any command.** If the section is missing, treat it as `own`, `manual`, `tracked`, Learning `off`.
- **Ownership** `own | external`.
- **Artificer files** `tracked | local-only` (legacy name: SDD files): whether `STATUS.md`, `docs/*.md`, `work/` and the Artificer additions to `{{PROJECT_RULES}}` live in the repo or only on this machine. `local-only`: listed in `.git/info/exclude`, never staged, committed or pushed; if one appears in `git status`, stop and tell the user.
- **Mode** `automatic | manual` (see "Git proposals"). `manual`: the AI proposes, the user runs every git action. `automatic`: the AI proposes and runs an action only when the user expressly orders it.
- **Learning** `off | assist | core | full` (legacy `on` = `full`).
- **Framework** `Artificer v<x>`.
## Git proposals
The AI never creates a branch, commits, pushes, opens a PR, resets or amends on its own. Every git step of every command is a **git proposal** block:
```
Branch:  feat/NNN-name  (from an up to date main)   [alternatives: ...]
Commit:  feat(NNN): S2 <description>
Files:   <git status --short of what goes in; Markdown files marked tracked / excluded>
PR:      <title>
         ## What changed / ## Why / ## How to verify
Run:     <the exact git / gh commands>
```
- **manual**: show the proposal and STOP. The user runs the commands (or edits them). Never run them, even if asked casually; if the user wants the AI to run them, they switch the project to `automatic` or give an express order for that action.
- **automatic**: show the proposal and wait. Run an action **only after an express order in the user's own words for that action** ("hacé el commit", "creá la rama", "pusheá", "creá el PR"). Approving a diff, "ok", "todo bien" or "seguí" is **not** an order. One order covers only the actions it names.
- Always before a proposal: the diff was shown and approved (Verify). Proposals never include `Co-Authored-By` or any AI attribution, in commits or PR descriptions.
- `local-only` Artificer files never appear in a proposal's file list (they stay excluded).

Branches: one per work item `feat/NNN-name`; small or trivial `fix/short-name` or `feat/short-name`; setup and foundation `chore/short-name`; always from an up to date `main`. Never commit to `main` (only exception: the initial commit of a brand new repository, still only by proposal and order). Conventional commits.

## Framework version
At the start of a session in an Artificer project, compare `- Framework: Artificer v<x>` with `{{ARTIFICER_HOME}}/VERSION`. Missing or older: tell the user in one line and suggest `/artificer-upgrade` (it never touches code). Do not block other work.

## Pull requests
Title in conventional format (`feat(NNN): ...`, `fix: ...`, `chore: ...`). Description: `## What changed` (areas, not every line), `## Why` (the problem or the work item), `## How to verify` (scenarios and manual checks). Always part of a git proposal; if `gh` is not available, include the compare link. No AI attribution.

## Verdict format (`/artificer-verify`)
Start with `VERDICT: APPROVED` or `VERDICT: CHANGES REQUESTED`. If changes: numbered list with `file:line`, what it violates (scenario, decision, principle, non-functional) and what is expected. Suggestions that violate nothing go under "Optional".

## Optional tools
Use them if available; otherwise continue and say so in one line: Chrome DevTools MCP (visual checks and console; else a manual checklist), Context7 MCP (library docs in architecture and map), Figma MCP (design), codebase-memory MCP (Explore and guided traces), frontend-design and web-design-guidelines skills (design and verify).
