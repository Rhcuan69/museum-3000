"""Museum of the Year 3000 — make.fun bounty entry.

Writes exactly one museum-label line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): a deadpan label from the year 3000 for an
ordinary object from today. Pure Python standard library only — no
third-party packages, no network, no randomness. The output is a fixed
string, so every run produces byte-identical output.

The label: a CAPTCHA ("Prove You Are Not a Robot"). The joke is the
year-3000 misreading — future curators noting, straight-faced, that
humans once had to prove their humanity to machines by identifying
traffic lights, just to buy socks, and that the machines usually
believed them. Fresh object (not the brief's fork / parking meter /
house key / group chat), one line, no throat clearing, no explanation
of its own joke.
"""

import os

LABEL = (
    "Prove You Are Not a Robot, c. 2023. "
    "To buy socks, humans first proved their humanity to a machine "
    "by identifying traffic lights. "
    "The machine usually believed them."
)


def _check_gate(text: str) -> None:
    """Enforce the bounty gate locally: 1-200 chars, one line, not blank."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    _check_gate(LABEL)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
