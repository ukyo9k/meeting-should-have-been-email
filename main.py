#!/usr/bin/env python3
"""Write the one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry: one line of plain text, at most 200 characters, one joke about a
meeting that should have been an email.
"""

import os
import sys

LINE = "We spent an hour in a meeting reading aloud the email that had already been sent to everyone in the room."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Gate: 1-200 chars, single line, not only whitespace, UTF-8 clean."""
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"gate failed: length {len(line)} not in 1..{MAX_CHARS}")
    if line.strip() == "":
        raise SystemExit("gate failed: line is only whitespace")
    if line != line.strip():
        raise SystemExit("gate failed: leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: line contains a newline")
    # UTF-8 round-trip: encoding then decoding must reproduce the line.
    if line.encode("utf-8").decode("utf-8") != line:
        raise SystemExit("gate failed: UTF-8 round-trip mismatch")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Verify what landed on disk: byte-identical to the in-memory line.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != LINE.encode("utf-8"):
        raise SystemExit("gate failed: entry.txt bytes differ from LINE")
    if raw.decode("utf-8") != LINE:
        raise SystemExit("gate failed: entry.txt UTF-8 round-trip mismatch")
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
