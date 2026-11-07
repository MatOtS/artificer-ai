"""OpenCode adapter: commands in ~/.config/opencode/commands, skills in ~/.agents/skills,
rules inlined in ~/.config/opencode/AGENTS.md (OpenCode does not resolve @imports)."""
import shutil
from pathlib import Path

from adapters.common import (agents_values, install_shared_skills, join_frontmatter, posix, render, rules_text,
                             split_frontmatter, strip_claude_fields)

NAME = "opencode"
LABEL = "OpenCode"


def detect(home):
    return (Path(home) / ".config" / "opencode").is_dir() or shutil.which("opencode") is not None


def install(writer, base, home, values):
    values = agents_values(values, home)
    config = Path(home) / ".config" / "opencode"
    for src in sorted((base / "commands").glob("*.md")):
        text = render(src.read_text(encoding="utf-8"), values)
        writer.write(config / "commands" / src.name, strip_claude_fields(text))
    # Skills are not slash commands in OpenCode: a thin command per user-invocable skill.
    for skill in sorted((base / "skills").glob("artificer-*/SKILL.md")):
        lines, _ = split_frontmatter(skill.read_text(encoding="utf-8"))
        if "user-invocable: false" in lines:
            continue
        keep = [render(l, values) for l in lines if l.startswith(("description:", "argument-hint:"))]
        name = skill.parent.name
        writer.write(config / "commands" / f"{name}.md",
                     join_frontmatter(keep, f"Load and follow the `{name}` skill.\n\nArguments: $ARGUMENTS\n"))
    skills = Path(home) / ".agents" / "skills"
    install_shared_skills(writer, base, skills, values, commands=False)
    agents_md = writer.set_block(config / "AGENTS.md", rules_text(base, values))
    return {"root": posix(Path(home)), "blocks": [agents_md]}
