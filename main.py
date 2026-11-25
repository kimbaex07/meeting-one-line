#!/usr/bin/env python3
"""meeting-one-line: emit the single-sentence entry to $MAKEFUN_OUTPUT_DIR.

Reads entry.txt next to this script, self-checks the contest gate
(1-200 chars, not only whitespace, exactly one sentence), then writes
the line plus one trailing newline to the output directory.
Pure Python standard library only. Deterministic, no network, no secrets.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        line = f.read()
    # Strip at most one trailing newline.
    if line.endswith("\n"):
        line = line[:-1]

    if not line or line.isspace():
        raise SystemExit("entry.txt is empty or only whitespace")
    if len(line) > 200:
        raise SystemExit("entry.txt is %d chars, over the 200-char limit" % len(line))
    # Exactly one sentence: one terminal punctuation mark, at the end.
    if len(re.findall(r"[.!?]", line)) != 1 or not line.rstrip().endswith((".", "!", "?")):
        raise SystemExit("entry.txt must be exactly one sentence")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
