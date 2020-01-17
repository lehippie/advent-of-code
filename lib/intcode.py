"""Intcode computer."""


def from_file(init_file, name='unnamed intcode computer'):
    """Create Intcode instance from a file."""
    with open(init_file) as f:
        init_values = f.readline()
    init_values = [int(i) for i in init_values.split(',')]
    return Intcode(init_values, name=name)


class Intcode():
    """Intcode computer class."""

    def __init__(self, init_values, name='unnamed intcode computer'):
        self.name = name
        self.initial_memory = init_values
        self.memory = init_values.copy()
        self.opcode_db = self._known_opcodes()
        self.pointer = 0
        self._decode_instruction()
        self.input = []
        self.waiting_for_input = False
        self.output = None
        self.output_pending = False
        self.finished = False

    def __repr__(self):
        return f"Intcode({self.memory}, {self.name})"

    def __str__(self):
        return self.name

    def _known_opcodes(self):
        """Create a dictionnary of available opcode."""
        return {1: self._instr_add,
                2: self._instr_multiply,
                3: self._instr_input,
                4: self._instr_output,
                5: self._instr_jump_if_true,
                6: self._instr_jump_if_false,
                7: self._instr_less_than,
                8: self._instr_equals}

    def _decode_instruction(self):
        """Read instruction and opcode at current pointer."""
        self.instr = self.memory[self.pointer]
        self.opcode = self.instr % 100


    ##########################
    ####    EXECUTION     ####
    ##########################

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
            self._execute_one_instr()
            if self.waiting_for_input:
                return
            if self.output_pending:
                self.output_pending = False
                if output_stream == 'stdout':
                    print(self.output)
                else:
                    return self.output

    def _execute_one_instr(self):
        """Execute instruction at current pointer."""
        if self.opcode in self.opcode_db:
            self.opcode_db[self.opcode]()
        else:
            raise IOError(f"Unknown opcode '{self.opcode}' "
                          f"at address {self.pointer}.")
        self._decode_instruction()
        if self.opcode == 99:
            self.finished = True

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.initial_memory, self.name)


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def _process_parameters(self, nb_param):
        """Return parameters according to instruction's modes."""
        modes = [int(i) for i in str(self.instr//100).zfill(nb_param)[::-1]]
        parameters = self.memory[self.pointer+1 : self.pointer+nb_param+1]
        for i, m in enumerate(modes):
            if m == 0:
                parameters[i] = self.memory[parameters[i]]
        return parameters

    def _instr_add(self):
        """Addition instruction."""
        a, b = self._process_parameters(2)
        addr = self.memory[self.pointer + 3]
        self.memory[addr] = a + b
        self.pointer += 4

    def _instr_multiply(self):
        """Multiplication instruction."""
        a, b = self._process_parameters(2)
        addr = self.memory[self.pointer + 3]
        self.memory[addr] = a * b
        self.pointer += 4

    def _instr_input(self):
        """Input instruction."""
        if not self.input:
            self.waiting_for_input = True
        else:
            addr = self.memory[self.pointer + 1]
            self.memory[addr] = self.input.pop(0)
            self.pointer += 2

    def _instr_output(self):
        """Output instruction."""
        self.output = self._process_parameters(1)[0]
        self.output_pending = True
        self.pointer += 2

    def _instr_jump_if_true(self):
        """Jump-if-true instruction."""
        a, b = self._process_parameters(2)
        if a:
            self.pointer = b
        else:
            self.pointer += 3

    def _instr_jump_if_false(self):
        """Jump-if-false instruction."""
        a, b = self._process_parameters(2)
        if not a:
            self.pointer = b
        else:
            self.pointer += 3

    def _instr_less_than(self):
        """Comparison instruction."""
        a, b = self._process_parameters(2)
        addr = self.memory[self.pointer + 3]
        self.memory[addr] = int(a < b)
        self.pointer += 4

    def _instr_equals(self):
        """Equality instruction."""
        a, b = self._process_parameters(2)
        addr = self.memory[self.pointer + 3]
        self.memory[addr] = int(a == b)
        self.pointer += 4


if __name__ == "__main__":
    import env
    from tests import tests_intcode
    tests_intcode.tests()
