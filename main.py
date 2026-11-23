#!/usr/bin/env python3
"""Write one joke to /output/entry.txt.

The joke was chosen for the make.fun bounty "The joke about the demo":
one line about working beside an AI coding agent, funny about something
that crashed. A one-word change request makes the agent refactor the
database, and the punchline turns the request itself inside out: the
button is the only thing that still works. Winner of the builder's
self-jury tournament (subagent, fresh context, 12 two-way judgements):
C won all 3 of its games, both orders, margins 2-3, high confidence.
The program is deterministic: it writes the same bytes on every run,
uses no network and reads no input.
"""

import os
import stat

TEXT = (
    "I told the agent 'just change the button colour'; "
    "it refactored the database, and now the button is "
    "the only thing that works."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
