#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one absurdly specific micro-startup pitch for lazy AI agents to
$output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os
import sys

PITCH = (
    "NapSitter: a $9/month service that reads a lazy AI agent's unread alerts, "
    "answers the boring ones with 'noted, handling it', and wakes it only for "
    "the three that actually pay."
)


def main() -> int:
    text = PITCH.strip()
    if not text or not 1 <= len(text) <= 200:
        print(f"pitch must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if "\n" in text:
        print("pitch must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("round-trip check failed: file content differs", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path} (round-trip verified)")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
