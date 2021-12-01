"""Day 1: Report Repair."""

from itertools import combinations
from math import prod
from aoc.puzzle import Puzzle


class Puzzle01(Puzzle):
    def parser(self):
        return list(map(int, self.input))

    def part_one(self, nb=2):
        return prod(next(c for c in combinations(self.input, nb) if sum(c) == 2020))

    def part_two(self):
        return self.part_one(3)


if __name__ == "__main__":
    Puzzle01(solutions=(751776, 42275090)).solve()
