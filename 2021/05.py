"""Day 5: Hydrothermal Venture."""

import re
from collections import Counter
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.straights = []
        self.diagonals = []
        for line in self.input:
            x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
            if x1 == x2 or y1 == y2:
                self.straights.append(((x1, y1), (x2, y2)))
            else:
                self.diagonals.append(((x1, y1), (x2, y2)))

    def part_one(self, count_diagonals=False):
        count = Counter()
        for (x1, y1), (x2, y2) in self.straights:
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            count.update((x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))
        if count_diagonals:
            for (x1, y1), (x2, y2) in self.diagonals:
                rx = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
                ry = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
                count.update((x, y) for x, y in zip(rx, ry))
        return sum(c > 1 for c in count.values())

    def part_two(self):
        return self.part_one(count_diagonals=True)


solutions = (5585, 17193)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
