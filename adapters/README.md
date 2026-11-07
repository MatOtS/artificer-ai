# Adapters

`install.py` merges `core/` and `custom/` into `build/`, fills the placeholders below, and each adapter copies the result to the place its AI tool expects. Adapters are added in the next packaging phases (Claude Code first, then OpenCode, Codex and GitHub Copilot in VS Code).

| Placeholder | Filled with |
|---|---|
| `{{ARTIFICER_HOME}}` | absolute path of this repository clone |
| `{{PROJECT_RULES}}` | the project instructions file of the tool: `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex, OpenCode), `.github/copilot-instructions.md` (Copilot) |
| `{{PYTHON}}` | the Python interpreter that ran `install.py` |

Frontmatter fields only some tools understand (`model`, `effort`, `allowed-tools`) are kept or removed per adapter.
