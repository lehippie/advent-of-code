"""Day 4: Camp Cleanup."""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.pairs = [list(map(int, re.findall(r"\d+", p))) for p in self.input]

    def part_one(self):
        count = 0
        for s1, e1, s2, e2 in self.pairs:
            if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
                count += 1
        return count

    def part_two(self):
        count = 0
        for s1, e1, s2, e2 in self.pairs:
            if set(range(s1, e1 + 1)).intersection(set(range(s2, e2 + 1))):
                count += 1
        return count


solutions = (475, 825)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
