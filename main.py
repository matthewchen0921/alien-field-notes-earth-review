#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — a review of planet Earth left by an alien
tourist — to /output/entry.txt. The line is fixed text, invented for
this competition: no real incident, no real person.
"""

import os

ENTRY = (
    # One joke, landed cleanly: the alien's angle is the glowing
    # rectangle every human stares at instead of the sky above them.
    # Verdict + rating at the end, the way a tourist review closes.
    "Lovely planet, but the locals built a window onto the whole universe "
    "and spend all day arguing with strangers through it. "
    "3/5 \u2014 the sunsets are free, and nobody looks up."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
