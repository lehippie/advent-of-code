"""--- Day 9: Sensor Boost ---"""

from aoc.puzzle import Puzzle
from intcode import Intcode


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        boost = Intcode(self.program)
        return boost.run(1)

    def part_two(self):
        boost = Intcode(self.program)
        return boost.run(2)


if __name__ == "__main__":
    Today().solve()
