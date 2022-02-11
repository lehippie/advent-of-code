"""Day 5: Hydrothermal Venture."""

import re
from collections import Counter
from aoc.puzzle import Puzzle


def get_range(x1, y1, x2, y2):
    """Calculate points covered between points (x1, y1) and (x2, y2).

    For straight lines, we iterate along each sorted coordinate.
    For diagonals, the direction of iteration depends on the relative
    positions along each coordinate.
    """
    if x1 == x2 or y1 == y2:
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        return ((x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))
    else:
        rx = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
        ry = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
        return ((x, y) for x, y in zip(rx, ry))


class Today(Puzzle):
    def parser(self):
        self.lines = [list(map(int, re.findall(r"\d+", l))) for l in self.input]

    def part_one(self, exclude_diagonals=True):
        count = Counter()
        for x1, y1, x2, y2 in self.lines:
            if exclude_diagonals and x1 != x2 and y1 != y2:
                continue
            count.update(get_range(x1, y1, x2, y2))
        return sum(c > 1 for c in count.values())

    def part_two(self):
        return self.part_one(exclude_diagonals=False)


solutions = (5585, 17193)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
