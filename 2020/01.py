"""Day 1: Report Repair."""

from itertools import combinations
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.expenses = list(map(int, self.input))

    def part_one(self, total=2020, n=2):
        return prod(next(c for c in combinations(self.expenses, n) if sum(c) == total))

    def part_two(self):
        return self.part_one(n=3)


solutions = (751776, 42275090)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
