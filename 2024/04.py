"""--- Day 4: Ceres Search ---"""

from collections import defaultdict
from itertools import product
from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)
DIAGONALS = (1 + 1j, 1 - 1j)


class Today(Puzzle):
    def parser(self):
        """Each position is stored in sets as complex numbers. Thus,
        there is no need to manage boundaries as the presence of XMAS
        is only a matter checking positions in these sets.
        """
        self.letters = defaultdict(set)
        for r, row in enumerate(self.input):
            for c, letter in enumerate(row):
                self.letters[letter].add(r + c * 1j)

    def part_one(self):
        return sum(
            x + d in self.letters["M"]
            and x + 2 * d in self.letters["A"]
            and x + 3 * d in self.letters["S"]
            for x, d in product(self.letters["X"], DIRECTIONS)
        )

    def part_two(self):
        return sum(
            all(
                (x + d in self.letters["M"] and x - d in self.letters["S"])
                or (x + d in self.letters["S"] and x - d in self.letters["M"])
                for d in DIAGONALS
            )
            for x in self.letters["A"]
        )


if __name__ == "__main__":
    Today().solve()
