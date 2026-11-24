#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

The line is a fixed, hand-written string. No randomness, no network, no
input: every run produces byte-identical output.

Angle: HR grievance. Instead of the usual "I was hungry" / "the sock
asked for it" excuses, the vacuum lawyers up — it refuses to comment
because the sock has filed an active grievance. The joke is that the
sock is now a co-worker with rights, and the vacuum is in a labour
dispute with its own lunch.
"""

import os
import sys

# The entry: one line, 84 characters, well under the 200-character cap.
ENTRY = "HR has advised me not to comment on the sock. The matter is now an active grievance."


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 200 characters, not only whitespace, on a single line.
    Failing loudly here is better than shipping an invalid entry.
    """
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
