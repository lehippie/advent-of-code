"""Day 3: Toboggan Trajectory."""

from collections import Counter
from math import prod
from aoc.puzzle import Puzzle


def count_trees(trees, right, down):
    return Counter(
        row[(k * right) % len(trees[0])]
        for k, row in enumerate(trees[0 : len(trees) : down])
    )["#"]


class Today(Puzzle):
    def part_one(self):
        return count_trees(self.input, 3, 1)

    def part_two(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return prod(count_trees(self.input, *s) for s in slopes)


if __name__ == "__main__":
    Today().solve()
