"""Day 8: Handheld Halting."""

from copy import deepcopy
from aoc.puzzle import Puzzle


class Console:
    def __init__(self, instructions):
        self.instructions = instructions
        self.position = 0
        self.accumulator = 0

    def execute_next_instruction(self):
        operation, argument = self.instructions[self.position]
        if operation == "acc":
            self.accumulator += argument
            self.position += 1
        elif operation == "jmp":
            self.position += argument
        elif operation == "nop":
            self.position += 1

    def is_looping(self):
        history = set()
        while True:
            if self.position in history:
                return True
            history.add(self.position)
            self.execute_next_instruction()
            if self.position == len(self.instructions):
                return False


class Today(Puzzle):
    def parser(self):
        instructions = [line.split() for line in self.input]
        self.boot = [[op, int(arg)] for op, arg in instructions]

    def part_one(self):
        console = Console(self.boot)
        assert console.is_looping()
        return console.accumulator

    def part_two(self):
        for k in range(len(self.boot)):
            new_boot = deepcopy(self.boot)
            if new_boot[k][0] == "jmp":
                new_boot[k][0] = "nop"
            elif new_boot[k][0] == "nop":
                new_boot[k][0] = "jmp"
            else:
                continue
            console = Console(new_boot)
            if not console.is_looping():
                return console.accumulator


if __name__ == "__main__":
    Today().solve()
