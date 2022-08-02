"""Day 9: Encoding Error."""

from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.data = list(map(int, self.input))

    def part_one(self):
        for k, n in enumerate(self.data):
            if k < 25:
                continue
            try:
                next(c for c in combinations(self.data[k - 25 : k], 2) if sum(c) == n)
            except StopIteration:
                self.invalid = n
                return n

    def part_two(self):
        for k in range(len(self.data)):
            l = 2
            while sum(self.data[k : k + l]) < self.invalid:
                l += 1
            s = self.data[k : k + l]
            if sum(s) == self.invalid:
                return min(s) + max(s)


solutions = (41682220, 5388976)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
