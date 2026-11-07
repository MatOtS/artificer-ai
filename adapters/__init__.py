"""One module per AI tool. Each exposes NAME, LABEL, detect(home) and install(writer, base, home, values)."""
from adapters import claude_code

ADAPTERS = {a.NAME: a for a in (claude_code,)}
