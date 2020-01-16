"""Intcode computer."""


def from_file(init_file, name='unnamed'):
    """Create Intcode instance from a file."""
    with open(init_file) as f:
        init_values = f.readline()
    init_values = [int(i) for i in init_values.split(',')]
    return Intcode(init_values, name=name)


class Intcode():
    """Intcode computer class."""

    def __init__(self, init_values, name='unnamed'):
        self.initial_memory = init_values
        self.name = name
        self.memory = init_values.copy()
        self.pointer = 0
        self._process_opcode()
        self.finished = False
        self.input = []
        self.waiting_for_input = False
        self.output = None
        self.output_pending = False

    def __repr__(self):
        return f"Intcode({self.memory}, {self.name})"

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Memory: {self.memory}\n"
                f"Current pointer: {self.pointer}\n"
                f"Current instruction: {self.instr}\n"
                f"Current opcode: {self.opcode}\n")

    def _process_opcode(self):
        """Update arguments with current pointer position."""
        self.instr = self.memory[self.pointer]
        self.opcode = self.instr % 100

    def _process_parameters(self, nparams):
        """Read modes from instruction and return correct parameters."""
        modes = [int(i) for i in str(self.instr//100).zfill(nparams)[::-1]]
        param = self.memory[self.pointer + 1 : self.pointer + nparams + 1]
        for i, m in enumerate(modes):
            if not m:
                param[i] = self.memory[param[i]]
        if len(param) == 1:
            param = param[0]
        return param


    ##########################
    ####    EXECUTION     ####
    ##########################

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.initial_memory, self.name)

    def execute(self, input_values=None, output_stream=None):
        """Execute the program."""
        # Process new input values
        if input_values is not None:
            self.waiting_for_input = False
            if isinstance(input_values, int):
                input_values = [input_values]
            self.input.extend(input_values)
        # Main loop
        while not self.finished:
            self._execute_next_instr()
            if self.waiting_for_input:
                return
            self._process_opcode()
            if self.opcode == 99:
                self.finished = True
            if self.output_pending:
                self.output_pending = False
                if output_stream == 'stdout':
                    print(self.output)
                else:
                    return self.output

    def _execute_next_instr(self):
        """Execute the next instruction."""
        if self.opcode == 1:
            self._instr_add(self._process_parameters(2))
        elif self.opcode == 2:
            self._instr_multiply(self._process_parameters(2))
        elif self.opcode == 3:
            self._instr_input()
        elif self.opcode == 4:
            self._instr_output(self._process_parameters(1))
        elif self.opcode == 5:
            self._instr_jump_if_true(self._process_parameters(2))
        elif self.opcode == 6:
            self._instr_jump_if_false(self._process_parameters(2))
        elif self.opcode == 7:
            self._instr_less_than(self._process_parameters(2))
        elif self.opcode == 8:
            self._instr_equals(self._process_parameters(2))
        else:
            raise IOError(
                f"Unknown opcode '{self.opcode}' at address {self.pointer}.")


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def _instr_add(self, parameters):
        """Addition instruction (opcode 1)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = parameters[0] + parameters[1]
        self.pointer += 4

    def _instr_multiply(self, parameters):
        """Multiplication instruction (opcode 2)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = parameters[0] * parameters[1]
        self.pointer += 4

    def _instr_input(self):
        """Input instruction (opcode 3)."""
        if not self.input:
            self.waiting_for_input = True
        else:
            result_address = self.memory[self.pointer + 1]
            self.memory[result_address] = self.input.pop(0)
            self.pointer += 2

    def _instr_output(self, parameter):
        """Output instruction (opcode 4)."""
        self.output = parameter
        self.output_pending = True
        self.pointer += 2

    def _instr_jump_if_true(self, parameters):
        """Jump-if-true instruction (opcode 5)."""
        if parameters[0]:
            self.pointer = parameters[1]
        else:
            self.pointer += 3

    def _instr_jump_if_false(self, parameters):
        """Jump-if-false instruction (opcode 6)."""
        if not parameters[0]:
            self.pointer = parameters[1]
        else:
            self.pointer += 3

    def _instr_less_than(self, parameters):
        """Comparison instruction (opcode 7)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = int(parameters[0] < parameters[1])
        self.pointer += 4

    def _instr_equals(self, parameters):
        """Equality instruction (opcode 8)."""
        result_address = self.memory[self.pointer + 3]
        self.memory[result_address] = int(parameters[0] == parameters[1])
        self.pointer += 4


if __name__ == "__main__":
    import env
    from tests import tests_intcode
    tests_intcode.tests()
