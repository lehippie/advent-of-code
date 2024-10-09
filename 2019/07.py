"""--- Day 7: Amplification Circuit ---"""

from itertools import permutations
from aoc.puzzle import Puzzle


class Intcode:
    def __init__(self, program, phase):
        self.memory = program.copy()
        self.pointer = 0
        self.inputs = [phase]
        self.output = []

    def run(self, *inputs):
        self.inputs.extend(inputs)
        while self.memory[self.pointer] != 99:
            opcode = self.memory[self.pointer]
            instruction, n_params = self.opcodes[opcode % 100]
            addresses = self.process_modes(n_params, opcode // 100)
            instruction(self, *addresses)
            if self.output:
                return self.output.pop()

    def process_modes(self, n, modes):
        a = []
        for k in range(1, n + 1):
            a.append(self.pointer + k if modes % 10 else self.memory[self.pointer + k])
            modes //= 10
        return a

    @property
    def is_running(self):
        return self.memory[self.pointer] != 99

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
        self.output.append(self.memory[addr])
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
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        max_signal = 0
        for phases in permutations(range(5)):
            output = 0
            for phase in phases:
                amp = Intcode(self.program, phase)
                output = amp.run(output)
            max_signal = max(max_signal, output)
        return max_signal

    def part_two(self):
        max_signal = 0
        for phases in permutations(range(5, 10)):
            amps = [Intcode(self.program, phase) for phase in phases]
            output, thrusters_signal = 0, 0
            while amps[-1].is_running:
                for amp in amps:
                    output = amp.run(output)
                if output is not None:
                    thrusters_signal = output
            max_signal = max(max_signal, thrusters_signal)
        return max_signal


if __name__ == "__main__":
    Today().solve()
