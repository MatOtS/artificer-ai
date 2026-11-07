"""Claude Code adapter: commands, skills, agents and rules in ~/.claude."""
import shutil
from pathlib import Path

from adapters.common import posix, render

NAME = "claude-code"
LABEL = "Claude Code"

# Import line used before Artificer had an installer (replaced by the managed block).
LEGACY_LINES = ("## Artificer", "@~/.claude/ARTIFICER-RULES.md")


def detect(home):
    return (Path(home) / ".claude").is_dir() or shutil.which("claude") is not None


def install(writer, base, home, values):
    claude = Path(home) / ".claude"
    values = dict(values, PROJECT_RULES="CLAUDE.md", SKILLS_DIR=posix(claude / "skills"))

    def put(src, dst):
        writer.write(dst, render(src.read_text(encoding="utf-8"), values))

    for src in sorted((base / "commands").glob("*.md")):
        put(src, claude / "commands" / src.name)
    for src in sorted((base / "skills").rglob("*")):
        if src.is_file():
            put(src, claude / "skills" / src.relative_to(base / "skills"))
    for src in sorted((base / "agents").glob("*.md")):
        put(src, claude / "agents" / src.name)

    rules = claude / "ARTIFICER-RULES.md"
    put(base / "rules" / "ARTIFICER-RULES.md", rules)
    claude_md = writer.set_block(
        claude / "CLAUDE.md", f"## Artificer\n@{posix(rules)}", legacy_lines=LEGACY_LINES)
    return {"root": posix(claude), "blocks": [claude_md]}
