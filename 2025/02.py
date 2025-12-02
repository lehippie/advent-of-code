"""--- Day 2: Gift Shop ---"""

import re
from aoc.puzzle import Puzzle

INVALID = re.compile(r"^(\d+)\1$")
SILLY = re.compile(r"^(\d+)\1+$")


class Today(Puzzle):
    def parser(self):
        self.ranges = [list(map(int, r.split("-"))) for r in self.input.split(",")]

    def part_one(self, pattern=INVALID):
        return sum(
            i
            for start, stop in self.ranges
            for i in range(start, stop + 1)
            if pattern.match(str(i))
        )

    def part_two(self):
        return self.part_one(SILLY)


if __name__ == "__main__":
    Today().solve()
