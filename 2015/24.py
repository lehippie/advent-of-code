"""Day 24: It Hangs in the Balance."""

from itertools import combinations
from math import prod
from aoc.puzzle import Puzzle


def equally_dividable(weights, n):
    """Check if <weights> can be separated in <n> equal groups."""
    if n == 1:
        return True
    target = sum(weights) // n
    for group_size in range(1, len(weights)):
        for group in combinations(weights, group_size):
            if sum(group) != target:
                continue
            if equally_dividable(weights.difference(group), n - 1):
                return True
    return False


class Today(Puzzle):
    def parser(self):
        self.weights = set(map(int, self.input))

    def part_one(self, n=3):
        """The weight of each group must be the total weight divided
        by the amount of groups (<n>). As the first group must contain
        the least packages and have the minimum product, these
        criteria are explored up until the rest of the packages can be
        divided equally.
        """
        target = sum(self.weights) // n
        for group1_size in range(1, len(self.weights)):
            for group1 in sorted(combinations(self.weights, group1_size), key=prod):
                if sum(group1) != target:
                    continue
                if equally_dividable(self.weights.difference(group1), n - 1):
                    return prod(group1)

    def part_two(self):
        return self.part_one(n=4)


solutions = (11266889531, 77387711)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
