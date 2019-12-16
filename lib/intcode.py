"""Intcode computer."""


def from_file(init_file):
    """Create Intcode instance from a file."""
    with open(init_file) as f:
        init_values = f.readline()
    init_values = [int(i) for i in init_values.split(',')]
    return Intcode(init_values)


class Intcode():
    """Intcode computer class."""

    def __init__(self, init_values):
        """Initialize memory state."""
        self.init_values = init_values
        self.memory = init_values.copy()
        self.pointer = 0
        self.finished = False


    ##########################
    ####    EXECUTION     ####
    ##########################

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.init_values)

    def execute(self):
        """Execute the whole program."""
        while not self.finished:
            self.do_next_instruction()

    def do_next_instruction(self):
        """Execute the next instruction."""
        opcode = self.memory[self.pointer]
        parameters = self.memory[self.pointer + 1:self.pointer + 4]

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


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def add(self, a, b, r):
        """Addition instruction (opcode 1).

        Add values at addresses a and b and store result at address r.
        """
        self.memory[r] = self.memory[a] + self.memory[b]


    def multiply(self, a, b, r):
        """Multiplication instruction (opcode 2).

        Multiply values at addresses a and b and store result at address r.
        """
        self.memory[r] = self.memory[a] * self.memory[b]
