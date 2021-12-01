"""Day 24: It Hangs in the Balance."""

from itertools import chain, combinations
from math import prod
from aoc.puzzle import Puzzle


class Puzzle24(Puzzle):
    def parser(self):
        return list(map(int, self.input))

    def part_one(self):
        for k in range(1, len(self.input) - 1):
            for g1 in sorted(combinations(self.input, k), key=prod):
                others = set(self.input).difference(g1)
                if sum(others) != 2 * sum(g1):
                    continue
                for g2 in chain(
                    *(combinations(others, l) for l in range(1, len(others)))
                ):
                    if sum(g2) == sum(others.difference(g2)):
                        return prod(g1)

    def part_two(self):
        for k in range(1, len(self.input) - 2):
            for g1 in sorted(combinations(self.input, k), key=prod):
                others = set(self.input).difference(g1)
                if sum(others) != 3 * sum(g1):
                    continue
                for g2 in chain(
                    *(combinations(others, l) for l in range(1, len(others)))
                ):
                    lasts = others.difference(g2)
                    if sum(lasts) != 2 * sum(g2):
                        continue
                    for g3 in chain(
                        *(combinations(lasts, l) for l in range(1, len(lasts)))
                    ):
                        if sum(g3) == sum(lasts.difference(g3)):
                            return prod(g1)


if __name__ == "__main__":
    Puzzle24(solutions=(11266889531, 77387711)).solve()
