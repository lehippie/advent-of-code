"""Day 23: Opening the Turing Lock."""

from aoc.puzzle import Puzzle


class Computer:
    def __init__(self, program):
        self.program = program
        self.idx = 0
        self.reg = {"a": 0, "b": 0}

    def hlf(self, r):
        self.reg[r] //= 2
        self.idx += 1

    def tpl(self, r):
        self.reg[r] *= 3
        self.idx += 1

    def inc(self, r):
        self.reg[r] += 1
        self.idx += 1

    def jmp(self, offset):
        self.idx += int(offset)

    def jie(self, r, offset):
        if not self.reg[r] % 2:
            self.jmp(offset)
        else:
            self.idx += 1

    def jio(self, r, offset):
        if self.reg[r] == 1:
            self.jmp(offset)
        else:
            self.idx += 1

    @property
    def instructions(self):
        return {
            "hlf": self.hlf,
            "tpl": self.tpl,
            "inc": self.inc,
            "jmp": self.jmp,
            "jie": self.jie,
            "jio": self.jio,
        }

    def run(self):
        while 0 <= self.idx < len(self.program):
            inst, args = self.program[self.idx].split(" ", 1)
            self.instructions[inst](*args.split(", "))


class Today(Puzzle):
    def part_one(self):
        computer = Computer(self.input)
        computer.run()
        return computer.reg["b"]

    def part_two(self):
        computer = Computer(self.input)
        computer.reg["a"] = 1
        computer.run()
        return computer.reg["b"]


solutions = (307, 160)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
