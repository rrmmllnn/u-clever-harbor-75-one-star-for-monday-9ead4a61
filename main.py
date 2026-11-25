#!/usr/bin/env python3
"""One Star for Monday.

Writes a single original one-star review of Monday, in one line of plain
text, to /output/entry.txt. Deterministic: the same line every run, well
under the 200-character cap and twenty words or fewer.
"""

import os

LINE = (
    "One star. Monday arrived at 6:04, drank my coffee, stole my clean "
    "shirt, and asked me to rate the experience."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert len(line.split()) <= 20, f"line is {len(line.split())} words, must be <= 20"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
