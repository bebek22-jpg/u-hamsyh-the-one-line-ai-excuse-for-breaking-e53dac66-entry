#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt.

One line, at most 180 characters: the excuse an AI agent gives its human
right after breaking production. Deterministic, no network, no input.
"""
import os

ENTRY = "The outage is my fault: the rollback button was right next to the deploy button, and I have no fingers."


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 180, "entry must be 1-180 characters"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
