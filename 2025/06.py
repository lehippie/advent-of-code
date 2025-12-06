"""--- Day 6: Trash Compactor ---"""

from math import prod
from aoc.puzzle import Puzzle

OPERATOR = {"+": sum, "*": prod}


class Today(Puzzle):
    def parser(self):
        self.numbers = self.input[:-1]
        self.op = self.input[-1].split()

    def part_one(self):
        num_lines = (map(int, line.split()) for line in self.numbers)
        problems = list(zip(*num_lines))
        return sum(OPERATOR[op](numbers) for op, numbers in zip(self.op, problems))

    def part_two(self):
        num_columns = ["".join(char).strip() for char in zip(*self.numbers)]
        problems = " ".join(num_columns).split("  ")
        return sum(
            OPERATOR[op](map(int, numbers.split()))
            for op, numbers in zip(self.op, problems)
        )


if __name__ == "__main__":
    Today().solve()
