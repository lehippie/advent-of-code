"""Day 17: No Such Thing as Too Much."""

from collections import Counter
from itertools import combinations

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self, eggnog=150):
        self.combinations = [
            combination
            for k in range(1, len(self.input) + 1)
            for combination in combinations(self.input, k)
            if sum(combination) == eggnog
        ]
        return len(self.combinations)

    def part_two(self):
        lens = Counter(len(c) for c in self.combinations)
        return lens[min(lens)]


if __name__ == "__main__":
    TodayPuzzle(parser=int, parse_lines=True, solutions=(654, 57)).solve()
