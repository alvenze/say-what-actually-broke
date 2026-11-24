#!/usr/bin/env python3
"""Say What Actually Broke: writes one honest error line to /output/entry.txt.

The entry is a single line of software error copy (gate: UTF-8, 1-200
characters, not only whitespace). It names one specific real failure,
our auth server being down, absolves the user with a twist, and tells
them what to do next.
"""

import os

ENTRY = (
    "Sign-in failed: that was the right password. "
    "Our auth server is down, not your memory. "
    "Wait two minutes and try again."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
