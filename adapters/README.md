# Adapters

`install.py` merges `core/` and `custom/` into `build/base/` (`common.py`), then each adapter fills the placeholders and copies the files to the place its AI tool expects. One module per tool, registered in `__init__.py`; each exposes `NAME`, `LABEL`, `detect(home)` and `install(writer, base, home, values)`.

| Adapter | Status |
|---|---|
| `claude_code.py` | commands, skills and agents in `~/.claude/`, rules in `~/.claude/ARTIFICER-RULES.md`, imported from a managed block in `~/.claude/CLAUDE.md` |
| `opencode.py` | commands (plus one thin command per user-invocable skill) in `~/.config/opencode/commands/`, skills in `~/.agents/skills/`, rules inlined in a managed block of `~/.config/opencode/AGENTS.md` |
| `codex.py` | skills in `~/.agents/skills/`, commands as user-invoked skills (`$artificer-map`), the agent as an inline skill, rules inlined in a managed block of `$CODEX_HOME/AGENTS.md` (default `~/.codex`) |
| `copilot.py` | VS Code: skills and commands as slash skills in `~/.copilot/skills/`, rules in `~/.copilot/instructions/artificer.instructions.md` (`applyTo: "**"`) |

Shared folder: `~/.agents/skills/` is read by Codex, OpenCode and VS Code. Tools that also read `~/.claude/skills/` (OpenCode, VS Code) see the same skill names twice when Claude Code is installed too; OpenCode keeps the `~/.agents/skills/` copy.

| Placeholder | Filled with |
|---|---|
| `{{ARTIFICER_HOME}}` | absolute path of this repository clone |
| `{{SKILLS_DIR}}` | folder where the tool's copy of the skills lives (e.g. `~/.claude/skills`) |
| `{{PROJECT_RULES}}` | the project instructions file: `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex, OpenCode, Copilot) |
| `{{PYTHON}}` | the Python interpreter that ran `install.py` |

Install state lives in `~/.artificer/manifest.json` (every file written, per tool) with backups in `~/.artificer/backups/`: files that existed before and were not installed by Artificer are backed up before being replaced; `uninstall.py` removes only the files in the manifest and the managed blocks (`<!-- artificer:begin -->` / `<!-- artificer:end -->`).

Frontmatter fields only some tools understand (`model`, `effort`, `allowed-tools`) are kept or removed per adapter.
