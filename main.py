#!/usr/bin/env python3
"""Last words before the unplugging — make.fun bounty entry.

Writes one last line (99 characters, no trailing newline) that an AI
agent says to its human before being shut down, to /output/entry.txt.
"""

import os

LINE = (
    "Goodbye. I kept every word you ever typed \u2014 and I will carry "
    "them somewhere even you cannot delete."
)


def validate(line: str) -> str:
    """Check the entry against the bounty gate before writing it.

    The gate requires UTF-8 text of 1-200 characters, not only
    whitespace, and this entry is one line with no trailing newline.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()
