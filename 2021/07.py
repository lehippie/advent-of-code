"""Day 7: The Treachery of Whales."""

from math import floor, ceil
from aoc.puzzle import Puzzle


class Puzzle07(Puzzle):
    def parser(self):
        self.crabs = list(map(int, self.input.split(",")))

    def part_one(self):
        crabs = sorted(self.crabs)
        median = crabs[(len(crabs) - 1) // 2]
        return sum(abs(crab - median) for crab in crabs)

    def part_two(self):
        mean = sum(self.crabs) / len(self.crabs)
        fuels = []
        for m in floor(mean), ceil(mean):
            distances = [abs(crab - m) for crab in self.crabs]
            fuels.append(sum(d * (d + 1) // 2 for d in distances))
        return min(fuels)


if __name__ == "__main__":
    Puzzle07(solutions=(335271, 95851339)).solve()
