"""Day 25: Let It Snow."""

from aoc.puzzle import Puzzle


class Puzzle25(Puzzle):
    def parser(self):
        row, col = self.input.split("row ")[1].split(", column ")
        return int(row), int(col[:-1])

    def part_one(self, code=20151125):
        row, col = self.input
        position = col + (row + col - 1) * (row + col - 2) // 2
        for _ in range(position - 1):
            code = (code * 252533) % 33554393
        return code


if __name__ == "__main__":
    Puzzle25(solutions=(19980801, NotImplemented)).solve()
