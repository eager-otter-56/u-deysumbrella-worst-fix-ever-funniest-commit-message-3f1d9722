#!/usr/bin/env python3
"""Entry program: writes the commit message to entry.txt.

One line, 95 chars: the fix (deleting the alert system) is the punchline.
"""
import os

ENTRY = "fix: silenced 2,400 daily alerts by deleting the alert system; the 6-hour outage went unnoticed"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(ENTRY) <= 100, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
