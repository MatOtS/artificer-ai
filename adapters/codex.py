"""Codex adapter: skills in ~/.agents/skills, rules inlined in ~/.codex/AGENTS.md."""
import os
import shutil
from pathlib import Path

from adapters.common import agents_values, install_shared_skills, posix, rules_text

NAME = "codex"
LABEL = "Codex"


def codex_home(home):
    return Path(os.environ.get("CODEX_HOME") or Path(home) / ".codex")


def detect(home):
    return codex_home(home).is_dir() or shutil.which("codex") is not None


def install(writer, base, home, values):
    values = agents_values(values, home)
    skills = Path(home) / ".agents" / "skills"
    install_shared_skills(writer, base, skills, values)
    agents_md = writer.set_block(codex_home(home) / "AGENTS.md", rules_text(base, values))
    return {"root": posix(skills), "blocks": [agents_md]}
