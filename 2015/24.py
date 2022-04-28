"""Day 24: It Hangs in the Balance."""

from itertools import combinations
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.weights = list(map(int, self.input))

    def part_one(self):
        for k in range(1, len(self.weights) - 1):
            for g1 in sorted(combinations(self.weights, k), key=prod):
                others = set(self.weights).difference(g1)
                if sum(others) != 2 * sum(g1):
                    continue
                for l in range(1, len(others)):
                    for g2 in combinations(others, l):
                        if sum(g2) == sum(others.difference(g2)):
                            return prod(g1)

    def part_two(self):
        for k in range(1, len(self.weights) - 2):
            for g1 in sorted(combinations(self.weights, k), key=prod):
                others = set(self.weights).difference(g1)
                if sum(others) != 3 * sum(g1):
                    continue
                for l in range(1, len(others) - 1):
                    for g2 in combinations(others, l):
                        lasts = others.difference(g2)
                        if sum(lasts) != 2 * sum(g2):
                            continue
                        for m in range(1, len(lasts)):
                            for g3 in combinations(lasts, m):
                                if sum(g3) == sum(lasts.difference(g3)):
                                    return prod(g1)


solutions = (11266889531, 77387711)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
