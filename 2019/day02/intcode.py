"""Intcode computer."""


class Intcode():
    """Intcode computer class."""

    def __init__(self, program):
        """Initial computer state."""
        self.initial_program = self._read_initial_program(program)
        self.memory = self.initial_program.copy()
        self.pointer = 0
        self.finished = False

    def _read_initial_program(self, program):
        """Return initial memory from input program."""
        if isinstance(program, list):
            return program
        elif isinstance(program, str):
            with open(program) as f:
                init = f.readline()
            return [int(i) for i in init.split(',')]
        else:
            raise IOError("Invalid 'program_values' format.")

    def run(self):
        """Execute the whole program."""
        while not self.finished:
            self.execute_next()

    def execute_next(self):
        """Execute the next instruction."""
        instruction = self.memory[self.pointer:self.pointer + 4]
        opcode = instruction[0]
        parameters = instruction[1:]
        if opcode == 1:
            self.add(*parameters)
            self.pointer += 4
        elif opcode == 2:
            self.multiply(*parameters)
            self.pointer += 4
        elif opcode == 99:
            self.finished = True
        else:
            raise IOError(
                f"Unknown opcode '{opcode}' at address {self.pointer}.")

    def reset(self):
        """Restore initial state."""
        self.__init__(self.initial_program)

    def add(self, a, b, r):
        """Addition instruction (opcode 1).

        Add values at addresses a and b and store result at adress r.
        """
        self.memory[r] = self.memory[a] + self.memory[b]


    def multiply(self, a, b, r):
        """Multiplication instruction (opcode 2).

        Add values at addresses a and b and store result at adress r.
        """
        self.memory[r] = self.memory[a] * self.memory[b]


if __name__ == "__main__":
    from intcode_tests import tests
    tests()
