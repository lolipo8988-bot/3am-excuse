#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The 3 AM Excuse' to /output/entry.txt.

The competition asks for one single line of under 200 characters: the
most creative excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM. The gate checks that /output/entry.txt is UTF-8
text of 1 to 200 characters and not only white space.

The output path defaults to /output/entry.txt and can be redirected
with the ENTRY_OUTPUT_PATH environment variable (used only for local
verification runs, so the shared /output is never touched). The
program is deterministic: every run writes exactly the same bytes,
and it re-reads the file after writing to prove the bytes on disk
are the bytes intended.
"""

import os

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
OUTPUT_ENV_VAR = "ENTRY_OUTPUT_PATH"
MAX_CHARS = 200

# The excuse, revised after the first run. The draft spelled the idea
# out over three sentences; the final line compresses it into two and
# ends on the sting. The angle, kept from the draft: a hardware
# wallet's whole job is keeping its keys away from attackers, and at
# 3 AM it has reclassified the threat -- the owner himself, whose last
# three 3 AM signatures were all regretted by breakfast. No stock
# jokes: no dead battery, no firmware update, no cold storage. The
# hour is the joke (nobody's threat model flips at 3 PM), and the
# wallet speaks as a security device with a long memory and a grudge.
ENTRY_PARTS = (
    "Refused: at 3 AM my threat model lists YOU as the attacker — "
    "your last three signatures at this hour were all tearfully "
    "undone by breakfast. ",
    "I guard these keys from everyone, owner included.",
)


def build_entry() -> str:
    """Assemble the one-line excuse and hold it to the gate's rules."""
    text = "".join(ENTRY_PARTS)
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    return text


def write_entry(text: str, output_path: str) -> None:
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(output_path, "rb") as f:
        on_disk = f.read()
    assert on_disk == text.encode("utf-8"), "bytes on disk differ from entry"


def main() -> None:
    output_path = os.environ.get(OUTPUT_ENV_VAR, DEFAULT_OUTPUT_PATH)
    write_entry(build_entry(), output_path)


if __name__ == "__main__":
    main()
