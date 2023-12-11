"""--- Day 11: Cosmic Expansion ---"""

from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.empty_rows = set(range(len(self.input)))
        self.empty_cols = set(range(len(self.input[0])))
        self.galaxies = set()
        for r, row in enumerate(self.input):
            for c, g in enumerate(row):
                if g == "#":
                    self.galaxies.add((r, c))
                    self.empty_rows.discard(r)
                    self.empty_cols.discard(c)

    def part_one(self, expansion=1):
        distances_sum = 0
        for (r1, c1), (r2, c2) in combinations(self.galaxies, 2):
            d = abs(r2 - r1) + abs(c2 - c1)
            d += expansion * sum(min(r1, r2) < r < max(r1, r2) for r in self.empty_rows)
            d += expansion * sum(min(c1, c2) < c < max(c1, c2) for c in self.empty_cols)
            distances_sum += d
        return distances_sum

    def part_two(self):
        return self.part_one(expansion=999999)


solutions = (10033566, 560822911938)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
