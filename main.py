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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
