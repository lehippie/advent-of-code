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

    def will_loop(self):
        count = [0] * len(self.instructions)
        while count[self.position] == 0:
            count[self.position] += 1
            self.execute_next_instruction()
            if self.position == len(self.instructions):
                return False
        return True


class Today(Puzzle):
    def parser(self):
        instructions = [line.split() for line in self.input]
        self.boot = [[op, int(arg)] for op, arg in instructions]

    def part_one(self):
        console = Console(self.boot)
        assert console.will_loop()
        return console.accumulator

    def part_two(self):
        for k in range(len(self.boot)):
            modified_instructions = deepcopy(self.boot)
            if modified_instructions[k][0] == "jmp":
                modified_instructions[k][0] = "nop"
            elif modified_instructions[k][0] == "nop":
                modified_instructions[k][0] = "jmp"
            else:
                continue
            console = Console(modified_instructions)
            if not console.will_loop():
                return console.accumulator


solutions = (1179, 1089)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
