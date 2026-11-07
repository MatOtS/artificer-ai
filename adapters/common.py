"""Shared pieces of the Artificer installer: build, rendering, file tracking."""
import json
import shutil
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CORE = REPO / "core"
CUSTOM = REPO / "custom"
BUILD = REPO / "build"
VERSION = (REPO / "VERSION").read_text(encoding="utf-8").strip()

BLOCK_BEGIN = "<!-- artificer:begin -->"
BLOCK_END = "<!-- artificer:end -->"


def posix(path):
    return Path(path).as_posix()


def build_base():
    """Merge core/ and custom/ into build/base/. Placeholders stay unfilled."""
    base = BUILD / "base"
    if BUILD.exists():
        shutil.rmtree(BUILD)
    shutil.copytree(CORE, base)

    overrides = CUSTOM / "overrides"
    if overrides.is_dir():
        for src in overrides.rglob("*"):
            if src.is_file():
                dst = base / src.relative_to(overrides)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

    for kind in ("commands", "skills"):
        if (CUSTOM / kind).is_dir():
            shutil.copytree(CUSTOM / kind, base / kind, dirs_exist_ok=True)

    rules = base / "rules" / "ARTIFICER-RULES.md"
    text = rules.read_text(encoding="utf-8").rstrip("\n") + "\n"
    for name in ("tone.md", "rules.md"):
        extra = CUSTOM / name
        if extra.is_file():
            text += "\n" + extra.read_text(encoding="utf-8").strip() + "\n"
    rules.write_text(text, encoding="utf-8")
    return base


def render(text, values):
    for key, value in values.items():
        text = text.replace("{{%s}}" % key, value)
    return text


class Manifest:
    """Install state for one home directory: <home>/.artificer/manifest.json."""

    def __init__(self, home):
        self.dir = Path(home) / ".artificer"
        self.path = self.dir / "manifest.json"
        self.data = {"version": VERSION, "repo": posix(REPO), "tools": {}}
        if self.path.is_file():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def files(self, tool=None):
        tools = self.data.get("tools", {})
        names = [tool] if tool else list(tools)
        return {f for name in names for f in tools.get(name, {}).get("files", [])}

    def save(self):
        self.dir.mkdir(parents=True, exist_ok=True)
        self.data["version"] = VERSION
        self.data["repo"] = posix(REPO)
        self.data["updated"] = datetime.now().isoformat(timespec="seconds")
        self.path.write_text(json.dumps(self.data, indent=2) + "\n", encoding="utf-8")


class Writer:
    """Writes the files of one tool, backing up anything it did not install before."""

    def __init__(self, manifest, tool, dry_run=False):
        self.manifest = manifest
        self.tool = tool
        self.dry_run = dry_run
        self.owned = manifest.files()
        self.written = []
        self.backed_up = []
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.backup_dir = manifest.dir / "backups" / stamp

    def backup(self, path):
        path = Path(path)
        dst = self.backup_dir / path.relative_to(path.anchor)
        if not self.dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dst)
        self.backed_up.append(posix(path))

    def write(self, path, text):
        path = Path(path)
        if path.is_file() and posix(path) not in self.owned:
            if path.read_text(encoding="utf-8", errors="replace") != text:
                self.backup(path)
        if not self.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        self.written.append(posix(path))

    def set_block(self, path, body, legacy_lines=()):
        """Put body between the Artificer markers in a file the user owns."""
        path = Path(path)
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        block = f"{BLOCK_BEGIN}\n{body.strip()}\n{BLOCK_END}\n"
        if BLOCK_BEGIN in text and BLOCK_END in text:
            start = text.index(BLOCK_BEGIN)
            end = text.index(BLOCK_END) + len(BLOCK_END)
            new = text[:start] + block.rstrip("\n") + text[end:]
        else:
            lines = text.splitlines()
            kept = [l for l in lines if l.strip() not in legacy_lines]
            while kept and kept[-1].strip() == "":
                kept.pop()
            new = "\n".join(kept) + ("\n\n" if kept else "") + block
        if new != text:
            if path.is_file():
                self.backup(path)
            if not self.dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(new, encoding="utf-8")
        return posix(path)

    def finish(self, extra=None):
        """Remove files this tool installed before and no longer generates."""
        stale = sorted(self.manifest.files(self.tool) - set(self.written))
        for f in stale:
            if Path(f).is_file() and not self.dry_run:
                Path(f).unlink()
        entry = {"files": sorted(self.written)}
        entry.update(extra or {})
        if not self.dry_run:
            self.manifest.data.setdefault("tools", {})[self.tool] = entry
        return stale


def remove_block(path):
    path = Path(path)
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    if BLOCK_BEGIN not in text or BLOCK_END not in text:
        return False
    start = text.index(BLOCK_BEGIN)
    end = text.index(BLOCK_END) + len(BLOCK_END)
    rest = (text[:start].rstrip("\n") + "\n" + text[end:].lstrip("\n")).lstrip("\n")
    if rest.strip():
        path.write_text(rest, encoding="utf-8")
    else:
        path.unlink()
    return True


def prune_empty_dirs(paths, stop_at):
    """Delete empty parent folders of the given files, never above stop_at."""
    stop_at = Path(stop_at).resolve()
    for f in sorted({Path(p).parent for p in paths}, key=lambda p: len(p.parts), reverse=True):
        d = f
        while d.exists() and d.resolve() != stop_at and stop_at in d.resolve().parents:
            if any(d.iterdir()):
                break
            d.rmdir()
            d = d.parent


# Frontmatter fields only Claude Code understands.
CLAUDE_ONLY_FIELDS = ("model:", "effort:", "allowed-tools:", "tools:")

ARGUMENTS_NOTE = (
    "Arguments: the text the user typed after the command name. In this file, `$ARGUMENTS` "
    "means all of that text, `$1` its first word and `$2` its second word.\n\n"
)


def split_frontmatter(text):
    """Return (frontmatter lines, body). No frontmatter: ([], text)."""
    if not text.startswith("---\n"):
        return [], text
    end = text.index("\n---", 4)
    return text[4:end].splitlines(), text[end + 4:].lstrip("\n")


def join_frontmatter(lines, body):
    return "---\n" + "\n".join(lines) + "\n---\n" + body


def strip_claude_fields(text):
    lines, body = split_frontmatter(text)
    if not lines:
        return text
    return join_frontmatter([l for l in lines if not l.startswith(CLAUDE_ONLY_FIELDS)], body)


def command_as_skill(name, text):
    """A slash command rewritten as a user-invoked skill (for tools without commands)."""
    lines, body = split_frontmatter(text)
    keep = [l for l in lines if l.startswith(("description:", "argument-hint:"))]
    return join_frontmatter([f"name: {name}"] + keep + ["disable-model-invocation: true"], ARGUMENTS_NOTE + body)


def agent_as_skill(name, text):
    """A Claude Code subagent rewritten as a skill run inline."""
    lines, body = split_frontmatter(text)
    keep = [l for l in lines if l.startswith("description:")]
    note = "This tool has no subagents: follow these steps inline and keep the report as short as described.\n\n"
    return join_frontmatter([f"name: {name}"] + keep, note + body)


def install_shared_skills(writer, base, skills_dir, values, commands=True):
    """Skills, plus commands and agents as skills, in a folder several tools read (e.g. ~/.agents/skills).
    commands=False for tools that install the commands as real commands."""
    skills_dir = Path(skills_dir)
    for src in sorted((base / "skills").rglob("*")):
        if src.is_file():
            text = render(src.read_text(encoding="utf-8"), values)
            if src.name == "SKILL.md":
                text = strip_claude_fields(text)
            writer.write(skills_dir / src.relative_to(base / "skills"), text)
    for src in sorted((base / "commands").glob("*.md")) if commands else []:
        text = render(src.read_text(encoding="utf-8"), values)
        writer.write(skills_dir / src.stem / "SKILL.md", command_as_skill(src.stem, text))
    for src in sorted((base / "agents").glob("*.md")):
        text = render(src.read_text(encoding="utf-8"), values)
        writer.write(skills_dir / src.stem / "SKILL.md", agent_as_skill(src.stem, text))


def agents_values(values, home):
    """Values for tools that read AGENTS.md in projects and skills from ~/.agents/skills."""
    return dict(values, PROJECT_RULES="AGENTS.md", SKILLS_DIR=posix(Path(home) / ".agents" / "skills"))


def rules_text(base, values):
    return render((base / "rules" / "ARTIFICER-RULES.md").read_text(encoding="utf-8"), values)
