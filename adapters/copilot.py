"""GitHub Copilot in VS Code adapter: skills (commands included, as slash skills) in
~/.copilot/skills, rules in ~/.copilot/instructions/artificer.instructions.md."""
import shutil
from pathlib import Path

from adapters.common import install_shared_skills, posix, rules_text, with_model_note

NAME = "copilot"
LABEL = "GitHub Copilot (VS Code)"


def detect(home):
    return (Path(home) / ".copilot").is_dir() or shutil.which("code") is not None


def install(writer, base, home, values):
    copilot = Path(home) / ".copilot"
    values = with_model_note(dict(values, PROJECT_RULES="AGENTS.md", SKILLS_DIR=posix(copilot / "skills")), NAME, LABEL)
    install_shared_skills(writer, base, copilot / "skills", values)
    rules = '---\napplyTo: "**"\n---\n' + rules_text(base, values)
    writer.write(copilot / "instructions" / "artificer.instructions.md", rules)
    return {"root": posix(copilot)}
