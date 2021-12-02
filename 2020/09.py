"""Day 9: Encoding Error."""

from itertools import combinations
from aoc.puzzle import Puzzle


class Puzzle09(Puzzle):
    def parser(self):
        return list(map(int, self.input))

    def part_one(self, preamble=25):
        for k, number in enumerate(self.input):
            if k < preamble:
                continue
            try:
                next(
                    c
                    for c in combinations(self.input[k - preamble : k], 2)
                    if sum(c) == number
                )
            except StopIteration:
                self.invalid = number
                return number

    def part_two(self):
        for k, n in enumerate(self.input):
            add = [n]
            l = 0
            while sum(add) < self.invalid:
                l += 1
                add.append(self.input[k + l])
            if sum(add) == self.invalid:
                return min(add) + max(add)


if __name__ == "__main__":
    Puzzle09(solutions=(41682220, 5388976)).solve()
