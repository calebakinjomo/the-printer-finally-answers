#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes the office printer's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when run outside the grader).
"""

import os

ENTRY = "Error 0x0001: I jammed on purpose. Your document was 87 pages long and called 'final_FINAL_v3'."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
