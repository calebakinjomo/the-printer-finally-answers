#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes the office printer's one-line comeback to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when run outside the grader).
"""

import os

ENTRY = "Error 0x0001: I jammed on purpose. Your document was 87 pages long and called 'final_FINAL_v3'."

MAX_ENTRY_CHARS = 240
MIN_ENTRY_CHARS = 1
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def validate_entry(text: str) -> None:
    if not MIN_ENTRY_CHARS <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} chars, got {len(text)}"
        )


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
