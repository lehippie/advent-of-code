"""Day 3: Rucksack Reorganization."""

from string import ascii_letters
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        priority = 0
        for sack in self.input:
            n = len(sack) // 2
            item = set(sack[:n]).intersection(sack[n:]).pop()
            priority += ascii_letters.index(item) + 1
        return priority

    def part_two(self):
        priority = 0
        for k in range(0, len(self.input), 3):
            e1, e2, e3 = self.input[k : k + 3]
            badge = set(e1).intersection(e2).intersection(e3).pop()
            priority += ascii_letters.index(badge) + 1
        return priority


solutions = (7795, 2703)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
