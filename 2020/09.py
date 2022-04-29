"""Day 9: Encoding Error."""

from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.data = list(map(int, self.input))

    def part_one(self, preamble=25):
        for k, number in enumerate(self.data):
            if k < preamble:
                continue
            try:
                next(
                    c
                    for c in combinations(self.data[k - preamble : k], 2)
                    if sum(c) == number
                )
            except StopIteration:
                self.invalid = number
                return number

    def part_two(self):
        for k, n in enumerate(self.data):
            add = [n]
            l = 0
            while sum(add) < self.invalid:
                l += 1
                add.append(self.data[k + l])
            if sum(add) == self.invalid:
                return min(add) + max(add)


solutions = (41682220, 5388976)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
