"""--- Day 3: Mull It Over ---"""

import re
from aoc.puzzle import Puzzle

MULTIPLY = re.compile(r"mul\((\d+),(\d+)\)")
CONDITIONAL_MULTIPLY = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")


class Today(Puzzle):
    def parser(self):
        self.memory = "".join(self.input)

    def part_one(self):
        return sum(int(a) * int(b) for a, b in MULTIPLY.findall(self.memory))

    def part_two(self):
        do = True
        instructions = CONDITIONAL_MULTIPLY.findall(self.memory)
        result = 0
        for instruction in instructions:
            if instruction == "do()":
                do = True
            elif instruction == "don't()":
                do = False
            elif do:
                a, b = re.findall(r"\d+", instruction)
                result += int(a) * int(b)
        return result


if __name__ == "__main__":
    Today().solve()
