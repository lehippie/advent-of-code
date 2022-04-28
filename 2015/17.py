"""Day 17: No Such Thing as Too Much."""

from collections import Counter
from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.containers = list(map(int, self.input))

    def part_one(self, eggnog=150):
        self.combinations = [
            combination
            for k in range(1, len(self.containers) + 1)
            for combination in combinations(self.containers, k)
            if sum(combination) == eggnog
        ]
        return len(self.combinations)

    def part_two(self):
        lens = Counter(len(c) for c in self.combinations)
        return lens[min(lens)]


solutions = (654, 57)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
