#!/usr/bin/env python3
"""One Star, Written in Sap entry.

Writes one one-star review, written by a houseplant about its human
owner, to /output/entry.txt (1-279 characters, UTF-8, single line).
Standard library only, no network, no input.
The review is built from three fragments: the watering grievance
(leftover coffee), the move-and-repot grievance (behind the monitor
for Zoom, into a chipped mug called a glow-up), and the punch (a
fern, not a prop, whose roots have filed a formal complaint).
``assemble`` joins them into the single review; ``validate`` checks
the entry gate before anything is written.
"""

from pathlib import Path

GRIEVANCE_WATER = (
    "One star: my owner waters me with leftover coffee, then moved me "
    "behind the monitor for Zoom and repotted me into a chipped mug he "
    "calls a glow-up."
)
PUNCH = (
    "I am a fern, not a prop, and my roots have filed a formal complaint."
)

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(grievance: str, punch: str) -> str:
    """Join the two fragments into one review."""
    return f"{grievance} {punch}"


def validate(review: str) -> str:
    """Check the review meets the entry gate before it is written.

    Must be 1-279 characters, a single line, at most 45 words,
    UTF-8-encodable, and more than whitespace. Raises ValueError
    otherwise.
    """
    if not 1 <= len(review) <= 279:
        raise ValueError(f"review must be 1-279 characters, got {len(review)}")
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")
    if len(review.split()) > 45:
        raise ValueError(f"review must be at most 45 words, got {len(review.split())}")
    if not review.strip():
        raise ValueError("review must not be only whitespace")
    review.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return review


def main() -> None:
    review = validate(assemble(GRIEVANCE_WATER, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(review, encoding="utf-8")


if __name__ == "__main__":
    main()
