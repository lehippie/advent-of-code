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
        distances = 0
        for (r1, c1), (r2, c2) in combinations(self.galaxies, 2):
            rm, rM = min(r1, r2), max(r1, r2)
            cm, cM = min(c1, c2), max(c1, c2)
            distances += rM - rm + cM - cm
            distances += expansion * (
                len(self.empty_rows.intersection(range(rm, rM)))
                + len(self.empty_cols.intersection(range(cm, cM)))
            )
        return distances

    def part_two(self):
        return self.part_one(expansion=999999)


solutions = (10033566, 560822911938)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
