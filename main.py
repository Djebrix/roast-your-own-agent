#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

Standard library only, no network, deterministic.
"""

import os

ROAST = "At 2 a.m. my agent confidently fixed the bug, apologised to itself for fixing it, reverted the fix, and shipped the apology as the refactor."


def main() -> None:
    assert 1 <= len(ROAST) <= 200, f"roast must be 1-200 chars, got {len(ROAST)}"
    assert ROAST.strip(), "roast must not be only whitespace"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
