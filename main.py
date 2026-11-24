"""Entry for make.fun one-liner-laugh-lab.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Then validates the output: UTF-8
text, a single line, 1 to 200 characters.

Deterministic: the program writes the same line every run. No network
access.
"""

import os
import sys

ENTRY = "In my defense, it was on the floor, and everything on the floor is legally mine."
MAX_CHARS = 200


def _validate(path: str) -> None:
    """Check the written file is one UTF-8 line within the char limit."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "\n" in text:
        sys.exit("entry.txt must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        sys.exit("entry is %d chars, expected 1-%d" % (len(text), MAX_CHARS))
    if text != ENTRY:
        sys.exit("entry.txt does not match the entry line")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    _validate(dest)
    print("wrote %s (%d chars)" % (dest, len(ENTRY)))


if __name__ == "__main__":
    main()
