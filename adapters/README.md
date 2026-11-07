# Adapters

`install.py` merges `core/` and `custom/` into `build/base/` (`common.py`), then each adapter fills the placeholders and copies the files to the place its AI tool expects. One module per tool, registered in `__init__.py`; each exposes `NAME`, `LABEL`, `detect(home)` and `install(writer, base, home, values)`.

| Adapter | Status |
|---|---|
| `claude_code.py` | commands, skills and agents in `~/.claude/`, rules in `~/.claude/ARTIFICER-RULES.md`, imported from a managed block in `~/.claude/CLAUDE.md` |
| OpenCode, Codex, GitHub Copilot (VS Code) | next phase |

| Placeholder | Filled with |
|---|---|
| `{{ARTIFICER_HOME}}` | absolute path of this repository clone |
| `{{SKILLS_DIR}}` | folder where the tool's copy of the skills lives (e.g. `~/.claude/skills`) |
| `{{PROJECT_RULES}}` | the project instructions file of the tool: `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex, OpenCode), `.github/copilot-instructions.md` (Copilot) |
| `{{PYTHON}}` | the Python interpreter that ran `install.py` |

Install state lives in `~/.artificer/manifest.json` (every file written, per tool) with backups in `~/.artificer/backups/`: files that existed before and were not installed by Artificer are backed up before being replaced; `uninstall.py` removes only the files in the manifest and the managed blocks (`<!-- artificer:begin -->` / `<!-- artificer:end -->`).

Frontmatter fields only some tools understand (`model`, `effort`, `allowed-tools`) are kept or removed per adapter.
