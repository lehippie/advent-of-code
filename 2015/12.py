"""Day 12: JSAbacusFramework.io."""

import json
import re
from aoc.puzzle import Puzzle


def almost_sum(db, discard="red"):
    if isinstance(db, list):
        return sum(almost_sum(v) for v in db)
    if isinstance(db, int):
        return db
    if isinstance(db, dict):
        if discard not in db.values():
            return almost_sum(list(db.values()))
    return 0


class Puzzle12(Puzzle):
    def part_one(self):
        return sum(map(int, re.findall(r"-?\d+", self.input)))

    def part_two(self):
        return almost_sum(json.loads(self.input))


if __name__ == "__main__":
    Puzzle12(solutions=(111754, 65402)).solve()
