"""Day 25: Let It Snow."""

from aoc.puzzle import Puzzle


def next_code(code, factor=252533, divider=33554393):
    return (code * factor) % divider


def code_position(row, col):
    s = row + col
    return col + (s - 1) * (s - 2) // 2


class Puzzle25(Puzzle):
    def parser(self):
        row, col = self.input.split("row ")[1].split(", column ")
        return int(row), int(col[:-1])

    def part_one(self, code=20151125):
        position = code_position(*self.input)
        for _ in range(position - 1):
            code = next_code(code)
        return code


if __name__ == "__main__":
    Puzzle25(solutions=(19980801, NotImplemented)).solve()
