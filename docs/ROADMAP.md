# Artificer roadmap

Current version: v0.3 (alpha). Items come from `BACKLOG.md` (IDs `B-xxx`). Rule: **no phase starts until the previous one has been used on real work and its usage feedback reviewed.** Order inside a phase is a suggestion, not a commitment.

## Phase 0 · Artificer Method v0.2 and dogfooding (now)
Goal: rebuild the core before anything else, then use it on real projects and find out how it performs.
Done:
- v0.1: four Learning levels, profile and onboarding, codemap, versioning, output styles, `TODO(human)`.
- v0.2: the **Artificer Method** replaces SDD: 7-step cycle (Intent, Examples, Explore, Map, Build, Verify, Close), three sizes, Given/When/Then examples as the spec, knowledge gate, Lead-and-Reveal, risk map and two-pass review, 200-line slices, `/artificer-*` commands, learning modes folded into the cycle (B-008, B-012, B-013, B-015, B-021).
- v0.2.1: git proposals (the AI never runs git without the user's express order; `manual` proposes only, `automatic` runs on order; no AI attribution), Spot question on the riskiest hunk and Follow questions so Reviewing and Tracing get trained, canonical XP mode names.
- v0.2.2: active map (current code per file + one question), walkthrough in parts, `core` ramp by skill and tool level, tech profile (self-assessed per tool, checked against evidence; optional survey in onboarding). Artificer rules split into `ARTIFICER-RULES.md` (imported from `CLAUDE.md`); other AI tools optional, chosen in onboarding (OpenCode integration only runs when enabled).
- v0.3: **the human decides what and how** at every level. The AI asks design decisions and never answers them; options only on request, in no order of preference, no recommendation; data-based suggestion only when asked or stuck. Decisions step at the start of Map, decisions as a binding contract in Build and Verify, project commands (product, principles, design, architecture, deploy, backlog, metrics) ask instead of proposing.
Next:
- B-019 Run `/artificer-upgrade` on existing projects.
- B-018 At least one real work item at each level (`off`, `assist`, `core`, `full`) and one `/artificer-quick`.
- Collect usage feedback: what worked, what was slow, what felt like losing control, bugs in the skills.
Exit: 2 to 4 weeks of use, feedback reviewed, fixes listed. Small fixes go into v0.2.x patches; big structural changes still belong to Phase 0.

## Phase 1 · v0.3 · Staying sharp (cheap wins)
Goal: protect the human review step and the user's skills with low-effort changes.
- B-007 Cold start rule.
- B-009 Weekly gym quota.
- Whatever Phase 0 feedback asks for.

## Phase 2 · v0.4 · Visual layer
Goal: make progress and knowledge of the code visible.
- B-005 Pixel art source and licenses.
- B-001 Pixel-art character sheet.
- B-003 Codemap as explored map (fog of war).
- B-002 Dungeon map of the project (specs as floors, tasks as rooms).
- B-022 Sheet language from profile.

## Phase 3 · v0.5 · Evidence and metrics
Goal: base the framework on stronger evidence and detect decline early.
- B-006 Research note on skill atrophy.
- B-010 Atrophy early warning.
- B-011 Katas from your own code.
- B-016 Reviewing XP from real PRs.
- B-014 Intent-first PR description.
- B-017 Review metrics.
- B-027 Task time tracking and estimates per Learning level (a minimal manual log could start earlier, during Phase 0).

## Phase 4 · v1.0 · Shareable
Goal: someone else can install and use it.
- B-026 Artificer files under git (can be done any time before; it helps every later phase).
- B-025 Manifest, install and uninstall.
- B-024 Integrations for other AI tools (on demand).
- B-021 Command prefix decision.
- B-023 Artificer output style.
- B-020 Package as a Claude Code plugin.
- Optional: B-004 live agent view à la agents-pixel-dungeon.

## Versioning
Every phase that changes how projects work bumps `skills/artificer-upgrade/VERSION` and adds an entry to `MIGRATIONS.md`, so `/artificer-upgrade` can bring projects up to date.
