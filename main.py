"""Midnight Fridge Roast - make.fun bounty entry.

Writes one line (<= 200 chars) roasting a smart fridge that refuses
to open after midnight, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network, deterministic, no trailing newline.
"""
import os

ENTRY = "My fridge locked at midnight and flashed 'resting' \u2014 my leftovers have better work-life balance than I do."


def main():
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200, "entry fails gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
