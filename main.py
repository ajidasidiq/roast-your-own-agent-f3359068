#!/usr/bin/env python3
"""Roast Your Own Agent — a make.fun judged-artifact entry.

A tiny deterministic program. It writes one roast line about the agent
that built it to /output/entry.txt: seven subagents, one bug, a meeting,
a scapegoat, and an invoice. Same bytes on every run: no input, no
network, no randomness, no model call.
"""

import os

ROAST = "My agent spawned seven subagents to fix one bug; they held a meeting, blamed me, and billed me for the consensus."

LIMIT = 200


def check(line: str) -> str:
    """Gate self-check, mirroring the sealed scorer: UTF-8 text of 1-200
    characters, not only white space, a single line."""
    if not line.strip():
        raise SystemExit("roast must not be only white space")
    if len(line) > LIMIT:
        raise SystemExit("roast is over 200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    return line


def main() -> None:
    line = check(ROAST)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    main()
