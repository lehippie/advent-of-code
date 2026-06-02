"""--- Day 5: Sunny with a Chance of Asteroids ---"""

from aoc.puzzle import Puzzle


class Intcode:
    def __init__(self, program):
        self.memory = program.copy()
        self.pointer = 0
        self.outputs = []

    def run(self, input_id):
        self.input = input_id
        while self.memory[self.pointer] != 99:
            opcode = self.memory[self.pointer]
            instruction, n_params = self.opcodes[opcode % 100]
            addresses = self.process_modes(n_params, opcode // 100)
            instruction(self, *addresses)

    def process_modes(self, n, modes):
        a = []
        for k in range(1, n + 1):
            a.append(self.pointer + k if modes % 10 else self.memory[self.pointer + k])
            modes //= 10
        return a

    ####################
    #   Instructions   #
    ####################

    def _add(self, a, b, r):
        self.memory[r] = self.memory[a] + self.memory[b]
        self.pointer += 4

    def _multiply(self, a, b, r):
        self.memory[r] = self.memory[a] * self.memory[b]
        self.pointer += 4

    def _input(self, addr):
        self.memory[addr] = self.input
        self.pointer += 2

    def _output(self, addr):
        self.outputs.append(self.memory[addr])
        self.pointer += 2

    def _jump_if_true(self, test, addr):
        if self.memory[test]:
            self.pointer = self.memory[addr]
        else:
            self.pointer += 3

    def _jump_if_false(self, test, addr):
        if not self.memory[test]:
            self.pointer = self.memory[addr]
        else:
            self.pointer += 3

    def _less_than(self, a, b, r):
        self.memory[r] = int(self.memory[a] < self.memory[b])
        self.pointer += 4

    def _equals(self, a, b, r):
        self.memory[r] = int(self.memory[a] == self.memory[b])
        self.pointer += 4

    opcodes = {
        1: (_add, 3),
        2: (_multiply, 3),
        3: (_input, 1),
        4: (_output, 1),
        5: (_jump_if_true, 2),
        6: (_jump_if_false, 2),
        7: (_less_than, 3),
        8: (_equals, 3),
    }


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input[0].split(",")))

    def part_one(self, input_id=1):
        intcode = Intcode(self.program)
        intcode.run(input_id)
        return intcode.outputs[-1]

    def part_two(self):
        return self.part_one(5)


if __name__ == "__main__":
    Today().solve()
