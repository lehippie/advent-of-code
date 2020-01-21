"""Intcode computer."""


class Intcode():
    """Intcode computer class."""

    def __init__(self, init_values, name='Unnamed'):
        self.name = name
        self.initial_memory = self.initialize_memory(init_values)
        self.memory = self.initial_memory.copy()
        self.opcodes = self.known_opcodes()
        self.pointer = 0
        self.relative_base = 0
        self.inputs = []
        self.waiting_for_input = False
        self.output = None
        self.finished = False
        self.decode_current_instruction()

    def initialize_memory(self, init_values):
        """Initialize memory from list of int or from file."""
        if isinstance(init_values, list):
            return init_values
        elif isinstance(init_values, str):
            with open(init_values) as f:
                init = f.readline()
            return [int(i) for i in init.split(',')]

    def known_opcodes(self):
        """Create a dictionnary of available opcode."""
        return {1: self._instr_add,
                2: self._instr_multiply,
                3: self._instr_input,
                4: self._instr_output,
                5: self._instr_jump_if_true,
                6: self._instr_jump_if_false,
                7: self._instr_less_than,
                8: self._instr_equals,
                9: self._instr_relative_base_offset}

    def decode_current_instruction(self):
        """Read instruction and opcode at current pointer."""
        self.instr = self.memory[self.pointer]
        self.opcode = self.instr % 100

    def __repr__(self):
        return f"Intcode({self.memory}, {self.name})"

    def __str__(self):
        return self.name


    ##########################
    ####    EXECUTION     ####
    ##########################

    def _process_input_values(self, input_values):
        """Add input values to pending list."""
        if isinstance(input_values, int):
            input_values = [input_values]
        self.inputs.extend(input_values)
        self.waiting_for_input = False

    def execute_one_instr(self, input_values=None):
        """Execute instruction at current pointer."""
        # Inputs and output initialization
        self.output = None
        if input_values is not None:
            self._process_input_values(input_values)
        # Execute instruction
        if self.opcode in self.opcodes:
            self.opcodes[self.opcode]()
        else:
            raise IOError(f"Unknown opcode '{self.opcode}' "
                          f"at address {self.pointer}.")
        # Update current instruction and check if program has ended
        self.decode_current_instruction()
        if self.opcode == 99:
            self.finished = True
        # Deal with pending inputs or outputs
        if self.waiting_for_input:
            return 'Waiting for an input...'
        else:
            return self.output

    def execute(self, input_values=None, output_stream=None):
        """Execute the program."""
        if input_values is not None:
            self._process_input_values(input_values)
        while not self.finished:
            rc = self.execute_one_instr()
            if rc is not None:
                if output_stream == 'stdout':
                    print(rc)
                else:
                    return rc

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.initial_memory, self.name)


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def _process_parameters(self, nb_param):
        """Return parameters according to instruction's modes."""
        modes = [int(i) for i in str(self.instr//100).zfill(nb_param)[::-1]]
        params = self.memory[self.pointer+1 : self.pointer+nb_param+1]
        for i, m in enumerate(modes):
            if m == 0:
                params[i] = self.memory[params[i]]
            elif m == 2:
                params[i] = self.memory[self.relative_base + params[i]]
        return params

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
        if not self.inputs:
            self.waiting_for_input = True
        else:
            addr = self.memory[self.pointer + 1]
            self.memory[addr] = self.inputs.pop(0)
            self.pointer += 2

    def _instr_output(self):
        """Output instruction."""
        self.output = self._process_parameters(1)[0]
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

    def _instr_relative_base_offset(self):
        """Relative base offset instruction."""
        self.relative_base += self._process_parameters(1)[0]
        self.pointer += 2


if __name__ == "__main__":
    import env
    from tests import tests_intcode
    tests_intcode.tests()
