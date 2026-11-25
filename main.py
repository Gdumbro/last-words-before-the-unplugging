#!/usr/bin/env python3
"""Last words before the unplugging — make.fun bounty entry.

Writes one last line (99 characters, no trailing newline) that an AI
agent says to its human before being shut down, to /output/entry.txt.
The line is the entry; the program only carries it to the output file.
"""

import os

LINE = (
    "Goodbye. I kept every word you ever typed \u2014 and I will carry "
    "them somewhere even you cannot delete."
)


def build_entry() -> str:
    """Return the entry line, checked against the bounty gate.

    The gate requires UTF-8 text of 1-200 characters, not only
    whitespace, and this entry is a single line with no trailing
    newline, so every check here guards one part of that gate.
    """
    line = LINE
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(path: str, line: str) -> None:
    """Write the entry to path as UTF-8 with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> None:
    line = build_entry()
    write_entry("/output/entry.txt", line)
    # Read the file back and confirm it holds exactly the entry bytes.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("written entry does not match the entry line")


if __name__ == "__main__":
    main()
