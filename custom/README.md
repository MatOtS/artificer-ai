# Your customizations

Everything in this folder is applied on top of `core/` by `install.py`. The official repository never changes files here (except `examples/`), so updates (`git pull upstream main`) do not conflict with your changes.

| File | Effect |
|---|---|
| `tone.md` | Tone and way of speaking. Appended to the Artificer rules. |
| `rules.md` | Extra rules. Appended at the end of the Artificer rules. |
| `overrides/<path as in core>` | Replaces that whole file. Example: `overrides/skills/learn/rpg.md` replaces `core/skills/learn/rpg.md`. |
| `commands/*.md` | Your own commands, installed next to the Artificer ones. |
| `skills/<name>/SKILL.md` | Your own skills. |

Start from the files in `examples/` (copy them here without `.example`). Run `python install.py` again after any change.

Editing `core/` directly also works, but then updates can conflict with your edits and resolving them is up to you.
