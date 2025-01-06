"""--- Day 17: Chronospatial Computer ---"""

from aoc.puzzle import Puzzle


class Computer:
    def __init__(self, registers, program):
        self.registers = registers.copy()
        self.program = program.copy()
        self.pointer = 0
        self.outputs = []

    def combo(self, operand):
        return operand if operand < 4 else self.registers[operand - 4]

    def run(self):
        while self.pointer < len(self.program):
            opcode, operand = self.program[self.pointer : self.pointer + 2]
            if opcode == 0:  # adv
                self.registers[0] = self.registers[0] >> self.combo(operand)
            elif opcode == 1:  # bxl
                self.registers[1] = self.registers[1] ^ operand
            elif opcode == 2:  # bst
                self.registers[1] = self.combo(operand) % 8
            elif opcode == 3:  # jnz
                if self.registers[0]:
                    self.pointer = operand - 2
            elif opcode == 4:  # bxc
                self.registers[1] = self.registers[1] ^ self.registers[2]
            elif opcode == 5:  # out
                self.outputs.append(self.combo(operand) % 8)
            elif opcode == 6:  # bdv
                self.registers[1] = self.registers[0] >> self.combo(operand)
            elif opcode == 7:  # cdv
                self.registers[2] = self.registers[0] >> self.combo(operand)
            self.pointer += 2
        return self.outputs


class Today(Puzzle):
    def parser(self):
        self.registers = []
        for line in self.input:
            if line.startswith("Reg"):
                self.registers.append(int(line.split(":")[-1]))
            elif line.startswith("Prog"):
                self.program = list(map(int, line.split(":")[-1].split(",")))

    def part_one(self):
        computer = Computer(self.registers, self.program)
        return ",".join(map(str, computer.run()))

    def part_two(self):
        """Reverse engineering day!
        The program is a loop that output a value and goes back to the
        begining until A is zero. The loop starts with `B = A % 8` and
        ends with `A = A // 8`, meaning the calculations are made on
        the octal decomposition of A.
        As A is part of the calculation, we can only work backward to
        find the decomposition's coefficients from hig to low orders.
        """
        values = [0]
        for output in reversed(self.program):
            next_values = []
            for value in values:
                for coeff in range(8):
                    v = 8 * value + coeff
                    computer = Computer([v, 0, 0], self.program)
                    if computer.run()[0] == output:
                        next_values.append(v)
            values = next_values
        return min(values)


if __name__ == "__main__":
    Today().solve()
