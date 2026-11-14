#!/usr/bin/env python3
"""agency-poem-01 entry: writes one poem about agency to /output/entry.txt.

The poem is about falconry: a falconer who unhooks the leash every morning
and gives the hawk the whole sky. The bird takes back the power to act on
every flight, and hands it back each time it chooses to land on a fist that
has never once closed on it.
"""

import os
from pathlib import Path

POEM = """Jesses

Every morning I take the leash off the jesses
and give her the sky entire — not lent. Given.
She climbs until the bell on her leg
is the only thing of mine she carries,
and it is too small to hold her.

She could spend the day anywhere: the river,
the far wood, a life with no fist in it.
That she comes back is not training.
Training is only how I learned to wait,
glove up, hand open, not calling —
calling is for dogs. For her I stand still
and let the choice be visible from the air:
an empty fist, offered, that has never once
closed on the thing it loves.

One day she will choose the far wood,
and that day will not be the failure of the others.
It will be their proof: every return was hers,
every landing a decision, made
on a hand that only ever held the straps
she let me fasten."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    tmp = output_dir / "entry.txt.tmp"
    tmp.write_text(POEM, encoding="utf-8")
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
