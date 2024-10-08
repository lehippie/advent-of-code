"""--- Day 5: Sunny with a Chance of Asteroids ---"""

from aoc.puzzle import Puzzle


class Intcode:
    def __init__(self, program):
        self.memory = program.copy()
        self.pointer = 0
        self.inputs = []
        self.outputs = []
        self.instructions = {
            1: (self._add, 3),
            2: (self._multiply, 3),
            3: (self._input, 1),
            4: (self._output, 1),
            5: (self._jump_if_true, 2),
            6: (self._jump_if_false, 2),
            7: (self._less_than, 3),
            8: (self._equals, 3),
        }

    def run(self, input_id):
        self.inputs.append(input_id)
        while self.memory[self.pointer] != 99:
            opcode = self.memory[self.pointer] % 100
            instruction, n_params = self.instructions[opcode]
            addresses = self._get_addresses(n_params, self.memory[self.pointer] // 100)
            instruction(*addresses)

    def _get_addresses(self, n, modes):
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
        self.memory[addr] = self.inputs.pop(0)
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


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self, input_id=1):
        intcode = Intcode(self.program)
        intcode.run(input_id)
        return intcode.outputs[-1]

    def part_two(self):
        return self.part_one(5)


if __name__ == "__main__":
    Today().solve()
