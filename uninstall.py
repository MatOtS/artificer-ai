#!/usr/bin/env python3
"""Remove Artificer from your AI tools. Your data in data/ is kept.

    python uninstall.py            # asks before removing
    python uninstall.py --purge    # also deletes data/ (asks again)
"""
import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from adapters.common import REPO, Manifest, posix, prune_empty_dirs, remove_block


def main():
    parser = argparse.ArgumentParser(description="Remove Artificer.")
    parser.add_argument("--home", default=str(Path.home()), help="home folder it was installed into")
    parser.add_argument("--purge", action="store_true", help="also delete your data in data/")
    parser.add_argument("-y", "--yes", action="store_true", help="do not ask")
    args = parser.parse_args()

    home = Path(args.home).expanduser().resolve()
    manifest = Manifest(home)
    tools = manifest.data.get("tools", {})
    if not tools:
        sys.exit(f"Artificer is not installed in {posix(home)} (no {posix(manifest.path)}).")

    files = sorted(manifest.files())
    print(f"Artificer files installed in {posix(home)}:")
    for name, entry in tools.items():
        print(f"  {name}: {len(entry.get('files', []))} files" + (f", block in {', '.join(entry.get('blocks', []))}" if entry.get("blocks") else ""))
    if not args.yes and input("Remove them? A backup is made first. [y/N] ").strip().lower() != "y":
        sys.exit("Nothing removed.")

    backup = manifest.dir / "backups" / ("uninstall-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
    for f in files:
        path = Path(f)
        if path.is_file():
            dst = backup / path.relative_to(path.anchor)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dst)
            path.unlink()
    for name, entry in tools.items():
        for block_file in entry.get("blocks", []):
            path = Path(block_file)
            if path.is_file():
                dst = backup / path.relative_to(path.anchor)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, dst)
                remove_block(path)
        if entry.get("root"):
            prune_empty_dirs([f for f in entry.get("files", [])], entry["root"])

    manifest.data["tools"] = {}
    manifest.save()
    print(f"Removed {len(files)} files. Backup in {posix(backup)}")

    data = REPO / "data"
    if args.purge and data.is_dir():
        if input(f"Delete ALL your Artificer data in {posix(data)}? This cannot be undone. Type 'delete': ").strip() == "delete":
            shutil.rmtree(data)
            print("Data deleted.")
        else:
            print("Data kept.")
    else:
        print(f"Your data is kept in {posix(data)}.")


if __name__ == "__main__":
    main()
