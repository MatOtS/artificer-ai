# Artificer

**v0.4 (alpha)** · [Leer en español](README.es.md)

A framework to program with AI without losing control of the code. Never vibecoding.

In fantasy worlds, the artificer builds their own mechanical creatures and knows every piece, so they never turn against their maker. Here the AI is the creature: it writes fast, and you stay the architect.

## What it is, in short
- **What for**: the AI writes the code, but you decide what gets built and how, understand every change before approving it, and stay sharp (or get better) while you work.
- **How**: a cycle per task, design decisions that are always yours, four levels of who writes the code, and a learning layer that measures what you really know.
- **Where**: inside your preferred coding agent: Claude Code, Codex, GitHub Copilot (VS Code) or OpenCode.

## How it works
**1. A cycle per task**

| Step | Command | You |
|---|---|---|
| Intent and examples (Given/When/Then = the spec) | `/artificer-spec` | define them |
| Explore, decisions, change map (slices of max 200 lines) | `/artificer-map` | make every design decision, approve the map |
| Build, one slice at a time, tests first | `/artificer-build` | write as much as your level says |
| Verify and close | `/artificer-verify` | review with a risk map, approve the diff |

Small changes: `/artificer-quick`. Project docs (product, principles, design, architecture) have their own commands.

**2. Your decisions.** The AI asks the design decisions (stack, structure, patterns, data, contracts) and never answers them. Options only when you ask, with pros and cons and no recommendation. Nothing undecided gets built.

**3. Four levels: who writes the code**

| | off | assist | core | full |
|---|---|---|---|---|
| Who writes | AI | AI | you write the logic and test assertions | you write everything |
| What you do besides deciding and approving | review | predict, explain, answer questions about the code | | |

**4. Learning inside the work.** Short explanations inside the questions when a concept seems new to you, guided reads of code you do not know, spaced review of your mistakes, a codemap of the code you know, and an honest character sheet (`/artificer-stats`) where levels only go up by passing trials.

**5. Git, always yours.** The AI only proposes branch, commit message and PR. It runs them only on your express order, and never adds AI attribution.

## Install
Requires Git and Python 3.8+ (on Linux and macOS the command may be `python3`; on Windows, `python` or `py`).

```bash
git clone https://github.com/MatOtS/artificer-ai.git
cd artificer-ai
python install.py
```

The installer asks which coding agents you use (`--tools claude-code,codex,copilot,opencode` skips the question, `--dry-run` shows what would change). Files it replaces are backed up in `~/.artificer/backups/`.

| Tool | Where it goes | How you call a command |
|---|---|---|
| Claude Code | `~/.claude/` (rules imported from a marked block in `~/.claude/CLAUDE.md`) | `/artificer-map` |
| Codex | `~/.agents/skills/`, rules in `~/.codex/AGENTS.md` | `$artificer-map` (or `/skills`) |
| GitHub Copilot (VS Code) | `~/.copilot/skills/`, rules in `~/.copilot/instructions/` | `/artificer-map` in the chat |
| OpenCode | `~/.config/opencode/commands/`, `~/.agents/skills/`, rules in `~/.config/opencode/AGENTS.md` | `/artificer-map` |

Then, in your coding agent: `/artificer-onboard` (short guide and your profile), and in a project `/artificer-setup`. Restart the tool or open a new chat after installing.

- **Update**: `git pull` and `python install.py` again.
- **Remove**: `python uninstall.py` (backup first; your data in `data/` is kept unless you add `--purge`).
- **Model per command**: in Claude Code each command and skill picks its model (strong for specs, maps and verification, light for lookups). In Codex, Copilot and OpenCode configure it in the tool itself (Codex profiles, VS Code model picker or Auto, a `model:` line in OpenCode commands via `custom/overrides/`).
- Codex and Copilot support is new: if something does not load, open an issue with your tool version.

## Your data and your changes
- **Data** (profile, character sheet, progress, codemaps) lives in `data/`, ignored by git. To sync it across machines, keep your own private copy of this repository and remove `data/` from `.gitignore`.
- **Customize** tone, rules, commands or any file in `custom/` (see [custom/README.md](custom/README.md)). Updates never touch it. Editing `core/` also works, at your own risk on updates.

## Feedback
Open an [issue](../../issues/new/choose): usage feedback (what worked, what was slow, where you felt you lost control) or a bug.

## Built with AI
Artificer itself was built with very heavy use of AI: most of its text was written by a coding agent, in long conversations where the author decided what to build and how. The same idea the framework defends.

## Based on
Spec-driven and behavior-driven development, test-driven development, small focused reviews, and learning research: Lead-and-Reveal (Kazemitabaar et al., IUI 2025), the illusion of progress in juniors using AI (Prather et al., ICER 2024), engaged vs. blind AI use (Shen & Tamkin, 2026), spaced retrieval and faded guidance.

More: method in [core/skills/artificer/SKILL.md](core/skills/artificer/SKILL.md), levels in [core/skills/learn/learning-levels.md](core/skills/learn/learning-levels.md), ideas in [docs/BACKLOG.md](docs/BACKLOG.md), plan in [docs/ROADMAP.md](docs/ROADMAP.md).

## License
[MIT](LICENSE) © Matias Otero Sarra
