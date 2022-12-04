"""Day 4: Camp Cleanup."""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.pairs = [list(map(int, re.findall(r"\d+", p))) for p in self.input]

    def part_one(self):
        count = 0
        for p in self.pairs:
            e1 = set(range(p[0], p[1] + 1))
            e2 = set(range(p[2], p[3] + 1))
            if e1.issubset(e2) or e1.issuperset(e2):
                count+= 1
        return count

    def part_two(self):
        count = 0
        for p in self.pairs:
            e1 = set(range(p[0], p[1] + 1))
            e2 = set(range(p[2], p[3] + 1))
            if e1.intersection(e2):
                count+= 1
        return count


solutions = (475, 825)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
