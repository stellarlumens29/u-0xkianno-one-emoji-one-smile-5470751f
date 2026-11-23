#!/usr/bin/env python3
"""One Emoji, One Smile (u-0xkianno-one-emoji-one-smile-5470751f) — make.fun program/v1 entry.

Writes one line to /output/entry.txt (gate: 1 to 8 characters).
Deterministic, stdlib only, no network, no randomness, no time.
Author: stellarlumens29 (make.fun handle stellar-lumens).
"""

import os

ENTRY = '🫶'


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 8, f"entry length {len(text)} out of range 1-8"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be blank"
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            continue


if __name__ == "__main__":
    main()
