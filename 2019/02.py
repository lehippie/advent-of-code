"""Day 2: 1202 Program Alarm."""

from itertools import product
from aoc.puzzle import Puzzle


class Intcode:
    def __init__(self, program, noun, verb):
        self.memory = program.copy()
        self.pointer = 0
        self.memory[1] = noun
        self.memory[2] = verb

    def run(self):
        while self.memory[self.pointer] != 99:
            opcode, a, b, r = self.memory[self.pointer : self.pointer + 4]
            if opcode == 1:
                self.memory[r] = self.memory[a] + self.memory[b]
            elif opcode == 2:
                self.memory[r] = self.memory[a] * self.memory[b]
            self.pointer += 4
        return self.memory[0]


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        return Intcode(self.program, 12, 2).run()

    def part_two(self):
        for noun, verb in product(range(100), repeat=2):
            if Intcode(self.program, noun, verb).run() == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    Today().solve()
