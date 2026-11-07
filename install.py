#!/usr/bin/env python3
"""Install or update Artificer into your AI coding tools.

    python install.py                      # asks which tools
    python install.py --tools claude-code  # no questions
    python install.py --dry-run            # show what would change

Run it again after `git pull` or after editing custom/.
"""
import argparse
import sys
from pathlib import Path

if sys.version_info < (3, 8):
    sys.exit("Artificer needs Python 3.8 or newer.")

from adapters import ADAPTERS
from adapters.common import REPO, VERSION, Manifest, Writer, build_base, posix


def choose_tools(home, manifest, preset):
    if preset:
        names = [n.strip() for n in preset.split(",") if n.strip()]
        unknown = [n for n in names if n not in ADAPTERS]
        if unknown:
            sys.exit(f"Unknown tool(s): {', '.join(unknown)}. Available: {', '.join(ADAPTERS)}")
        return names
    installed = set(manifest.data.get("tools", {}))
    print("AI tools Artificer can install into:")
    options = list(ADAPTERS.values())
    default = []
    for i, a in enumerate(options, 1):
        marks = []
        if a.NAME in installed:
            marks.append("installed")
        elif a.detect(home):
            marks.append("detected")
        if marks:
            default.append(str(i))
        print(f"  {i}. {a.LABEL}" + (f" ({', '.join(marks)})" if marks else ""))
    hint = ",".join(default) or "none"
    answer = input(f"Numbers separated by commas [{hint}]: ").strip() or ",".join(default)
    picked = []
    for part in answer.split(","):
        part = part.strip()
        if part.isdigit() and 1 <= int(part) <= len(options):
            picked.append(options[int(part) - 1].NAME)
    if not picked:
        sys.exit("No tool selected. Nothing to do.")
    return picked


def main():
    parser = argparse.ArgumentParser(description="Install or update Artificer.")
    parser.add_argument("--tools", help="comma separated: " + ", ".join(ADAPTERS))
    parser.add_argument("--home", default=str(Path.home()), help="home folder to install into (default: yours)")
    parser.add_argument("--dry-run", action="store_true", help="show what would change, write nothing")
    args = parser.parse_args()

    home = Path(args.home).expanduser().resolve()
    manifest = Manifest(home)
    tools = choose_tools(home, manifest, args.tools)

    print(f"\nArtificer v{VERSION} from {posix(REPO)}")
    base = build_base()
    (REPO / "data").mkdir(exist_ok=True)
    values = {"ARTIFICER_HOME": posix(REPO), "PYTHON": posix(sys.executable)}

    backups = []
    for name in tools:
        adapter = ADAPTERS[name]
        writer = Writer(manifest, name, dry_run=args.dry_run)
        extra = adapter.install(writer, base, home, values)
        stale = writer.finish(extra)
        backups += writer.backed_up
        print(f"  {adapter.LABEL}: {len(writer.written)} files" + (f", {len(stale)} old files removed" if stale else ""))
        if writer.backed_up:
            print(f"    previous versions of {len(writer.backed_up)} files saved in {posix(writer.backup_dir)}")

    if args.dry_run:
        print("\nDry run: nothing was written (build/ was regenerated).")
        return
    manifest.save()
    print("\nDone. Open your AI tool and run /artificer-onboard (first time) or /artificer-setup in a project.")


if __name__ == "__main__":
    main()
