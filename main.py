#!/usr/bin/env python3
"""Write one joke to /output/entry.txt.

The joke was chosen for the make.fun bounty "The joke about the demo":
one line about working beside an AI coding agent, funny about something
that crashed. V2 replaces V1's angle: mid-demo, the agent fixes a bug
that never existed, then breaks the demo so the fix has something to
do. Double twist, still one line, still about a crash beside a coding
agent. Chosen by a fresh-context self-jury (6 two-way judgements):
it beat V1 in both orders, margin 2 and 2, decided on K2, with K2 not
dropping. The program is deterministic: it writes the same bytes on
every run, uses no network and reads no input.
"""

import os
import stat

TEXT = (
    "Mid-demo, my agent fixed a bug that didn't exist \u2014 "
    "then broke the demo so the fix had something to do."
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
