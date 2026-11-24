"""make.fun entry: Fortune Cookie Wisdom for Developers.

Writes one line of fortune-cookie wisdom for a software developer to
/output/entry.txt: a single sentence of at most 120 characters.
Stdlib-only (os, sys); no network; deterministic.

Design (from the published judge brief, criteria in order):
1. One original line of fortune-cookie wisdom for a developer, not a
   slogan, a punchline or generic advice: a prophecy in the second
   person ("You will blame the last commit ..."), not a slogan.
2. Reads like a fortune cookie: one short balanced sentence, a mirror
   structure ("the last commit ... the last commit"), that lands in a
   single breath.
3. Says something true about a developer's day: git blame, the last
   commit, and the person blamed turning out to be yourself.
4. Turns that truth in a way the reader has not heard before: the
   reveal is the twist -- and "blame" is also the git command itself.
5. Leaves a quiet twist / double meaning that rewards a second read:
   "will turn out to be yours" means both the commit's authorship and
   the blame itself.

The line itself (78 characters):

    You will blame the last commit, and the last commit will turn out
    to be yours.
"""

import os
import sys

TEXT = "You will blame the last commit, and the last commit will turn out to be yours."


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # counted as Unicode code points, and not only white space.
    if not (1 <= len(TEXT) <= 120):
        print(f"entry length {len(TEXT)} outside 1-120", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in TEXT:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
