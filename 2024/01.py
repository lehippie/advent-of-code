"""--- Day 1: Historian Hysteria ---"""

from collections import Counter
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.l1, self.l2 = [], []
        for line in self.input:
            a, b = line.split()
            self.l1.append(int(a))
            self.l2.append(int(b))

    def part_one(self):
        return sum(abs(a - b) for a, b in zip(sorted(self.l1), sorted(self.l2)))

    def part_two(self):
        counts = Counter(self.l2)
        return sum(a * counts.get(a, 0) for a in self.l1)


if __name__ == "__main__":
    Today().solve()
