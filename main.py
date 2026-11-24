"""Entry for make.fun one-liner-laugh-lab.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

Deterministic: the program writes the same line every run. No network
access.
"""

import os

ENTRY = "In my defense, it was on the floor, and everything on the floor is legally mine."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (dest, len(ENTRY)))


if __name__ == "__main__":
    main()
