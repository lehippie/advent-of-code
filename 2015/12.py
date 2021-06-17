"""Day 12: JSAbacusFramework.io."""

import json
import re

from aoc.puzzle import Puzzle


def almost_sum(db, discard="red"):
    if isinstance(db, dict):
        if discard in db.values():
            return 0
        else:
            return almost_sum(list(db.values()))
    if isinstance(db, list):
        return sum(almost_sum(v) for v in db)
    if isinstance(db, int):
        return db
    return 0


class TodayPuzzle(Puzzle):
    def part_one(self):
        return sum(map(int, re.findall(r"-?\d+", self.input)))

    def part_two(self):
        return almost_sum(json.loads(self.input))


if __name__ == "__main__":
    TodayPuzzle(solutions=(111754, 65402)).solve()
