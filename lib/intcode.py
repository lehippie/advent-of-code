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
        self.input = None
        self.output = None


    ##########################
    ####    EXECUTION     ####
    ##########################

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.init_values)

    def execute(self, input_value=None):
        """Execute the whole program."""
        self.input = input_value
        while not self.finished:
            self.execute_next()
        return self.output

    def execute_next(self):
        """Execute the next instruction."""
        self.instr = self.memory[self.pointer]
        opcode = self.instr % 100

        if opcode == 1:
            self.add(self.process_parameters(2))

        elif opcode == 2:
            self.multiply(self.process_parameters(2))

        elif opcode == 3:
            self.get_input()

        elif opcode == 4:
            self.output_value(self.process_parameters(1))

        elif opcode == 5:
            self.jump_if_true(self.process_parameters(2))

        elif opcode == 6:
            self.jump_if_false(self.process_parameters(2))

        elif opcode == 7:
            self.less_than(self.process_parameters(2))

        elif opcode == 8:
            self.equals(self.process_parameters(2))

        elif opcode == 99:
            self.finished = True

        else:
            raise IOError(
                f"Unknown opcode '{opcode}' at address {self.pointer}.")

    def process_parameters(self, nparams):
        """Return correct parameters from mode."""
        modes = [int(i) for i in str(self.instr//100).zfill(nparams)[::-1]]
        param = self.memory[self.pointer + 1 : self.pointer + nparams + 1]
        for i, m in enumerate(modes):
            if not m:
                param[i] = self.memory[param[i]]
        if len(param) == 1:
            param = param[0]
        return param


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def add(self, parameters):
        """Addition instruction (opcode 1)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = parameters[0] + parameters[1]
        self.pointer += 4

    def multiply(self, parameters):
        """Multiplication instruction (opcode 2)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = parameters[0] * parameters[1]
        self.pointer += 4

    def get_input(self):
        """Input instruction (opcode 3)."""
        result_address = self.memory[self.pointer + 1]
        if self.input is None:
            self.memory[result_address] = int(input("Enter input value: "))
        else:
            self.memory[result_address] = self.input
        self.pointer += 2

    def output_value(self, parameter):
        """Output instruction (opcode 4)."""
        if self.output is None:
            self.output = parameter
        elif isinstance(self.output, int):
            self.output = [self.output, parameter]
        else:
            self.output.append(parameter)
        self.pointer += 2

    def jump_if_true(self, parameters):
        """Jump-if-true instruction (opcode 5)."""
        if parameters[0]:
            self.pointer = parameters[1]
        else:
            self.pointer += 3

    def jump_if_false(self, parameters):
        """Jump-if-false instruction (opcode 6)."""
        if not parameters[0]:
            self.pointer = parameters[1]
        else:
            self.pointer += 3

    def less_than(self, parameters):
        """Comparison instruction (opcode 7)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = int(parameters[0] < parameters[1])
        self.pointer += 4

    def equals(self, parameters):
        """Equality instruction (opcode 8)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = int(parameters[0] == parameters[1])
        self.pointer += 4


if __name__ == "__main__":
    import env
    from tests import tests_intcode
    tests_intcode.tests()
