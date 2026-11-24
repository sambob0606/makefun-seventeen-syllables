#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, at most 200 chars) to
/output/entry.txt. Stdlib only.

The haiku: a breakpoint's red dot at 3 a.m., the log calmly insisting
everything is fine, and the turn -- the typo was mine all along.
"""

import os

# Syllable counts per line: 5 / 7 / 5.
HAIKU_LINES = (
    "One red dot at three",
    "the log insists all is well",
    "the typo was mine",
)

MAX_CHARS = 200


def build_haiku() -> str:
    text = "\n".join(HAIKU_LINES) + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"haiku must be 1-{MAX_CHARS} chars, got {len(text)}")
    if len(HAIKU_LINES) != 3:
        raise ValueError("haiku must be exactly three lines")
    return text


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = build_haiku()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
