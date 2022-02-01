"""Day 9: Smoke Basin."""

from itertools import product
from math import prod
from aoc.puzzle import Puzzle


def adjacents(r, c, maxr, maxc):
    adj = set()
    for row, col in zip([r, r, r - 1, r + 1], [c - 1, c + 1, c, c]):
        if (0 <= row < maxr) and (0 <= col < maxc):
            adj.add((row, col))
    return adj


class Today(Puzzle):
    def parser(self):
        self.floor = [list(map(int, line)) for line in self.input]

    def part_one(self):
        self.rlen = len(self.floor)
        self.clen = len(self.floor[0])
        self.lows = set()
        risk = 0
        for r, c in product(range(self.rlen), range(self.clen)):
            if all(
                self.floor[r][c] < self.floor[adj_r][adj_c]
                for adj_r, adj_c in adjacents(r, c, self.rlen, self.clen)
            ):
                self.lows.add((r, c))
                risk += 1 + self.floor[r][c]
        return risk

    def part_two(self):
        self.sizes = []
        for low_r, low_c in self.lows:
            bassin = {(low_r, low_c)}
            locations_to_check = [(low_r, low_c)]
            while locations_to_check:
                r, c = locations_to_check.pop(0)
                new_locs = adjacents(r, c, self.rlen, self.clen).difference(bassin)
                for adj_r, adj_c in new_locs:
                    if self.floor[adj_r][adj_c] != 9:
                        bassin.add((adj_r, adj_c))
                        locations_to_check.append((adj_r, adj_c))
            self.sizes.append(len(bassin))
        return prod(sorted(self.sizes)[-3:])


solutions = (468, 1280496)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
