"""Intcode computer for Advent of Code 2019."""


class Intcode():
    """Intcode computer class.

    Arguments:
        program -- Program loaded in the computer memory.
                   Can be a list of Int OR the path to a file
                   containig such list on its first line.
        name -- Name of the Intcode computer's instance.
    """

    def __init__(self, program, name='Unnamed'):
        """Initial computer state."""
        self.name = name
        self.initial_program = self._initialize_memory(program)
        self.memory = self.initial_program.copy()
        self.instructions = self.known_instructions()
        self.pointer = 0
        self.relative_base = 0
        self.inputs = []
        self.outputs = []
        self.waiting_for_input = False
        self.finished = False
        self._decode_current_instruction()

    def __repr__(self):
        return f"Intcode({self.initial_program}, {self.name})"

    def __str__(self):
        return self.name

    def known_instructions(self):
        """Dictionnary of available instructions."""
        return {1: self._instr_add,
                2: self._instr_multiply,
                3: self._instr_input,
                4: self._instr_output,
                5: self._instr_jump_if_true,
                6: self._instr_jump_if_false,
                7: self._instr_less_than,
                8: self._instr_equals,
                9: self._instr_relative_base_offset}

    def _initialize_memory(self, program_values):
        """Initialize memory from program values."""
        if isinstance(program_values, list):
            return program_values
        elif isinstance(program_values, str):
            with open(program_values) as f:
                init = f.readline()
            return [int(i) for i in init.split(',')]
        else:
            raise IOError("Invalid 'program_values' format.")

    def _decode_current_instruction(self):
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
        if input_values is not None:
            if isinstance(input_values, int):
                input_values = [input_values]
            self.inputs.extend(input_values)
            self.waiting_for_input = False

    def execute_instr(self, input_values=None):
        """Execute instruction at current pointer."""
        if not self.finished:
            self._process_input_values(input_values)
            if self.opcode in self.instructions:
                ret = self.instructions[self.opcode]()
            else:
                raise IOError(f"Unknown opcode '{self.opcode}'"
                            f" at address {self.pointer}.")
            # Check if this is the end of the program
            self._decode_current_instruction()
            if self.opcode == 99:
                self.finished = True
            return ret

    def execute(self, input_values=None, pause_on_output=True):
        """Execute the program until next output instruction.

        Execution is stopped if an input value is needed.
        If <pause_on_output> is False, each output is stored
        and only returned as a list at the end.
        """
        self._process_input_values(input_values)
        while not self.finished:
            ret = self.execute_instr()
            if self.waiting_for_input:
                return
            if ret is not None and pause_on_output:
                return ret
        if not pause_on_output:
            return self.outputs

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.initial_program, self.name)


    ###############################
    ####    PARAMETER MODES    ####
    ###############################

    def _process_parameters(self, nb_param):
        """Return correct parameters from instruction's modes."""
        modes = [int(i) for i in str(self.instr//100).zfill(nb_param)[::-1]]
        params = self.memory[self.pointer+1 : self.pointer+nb_param+1]
        for i, m in enumerate(modes):
            if m == 0: # Position mode
                params[i] = self.memory[params[i]]
            elif m == 2: # # Relative mode
                params[i] = self.memory[self.relative_base + params[i]]
        if len(params) == 1:
            params = params[0]
        return params


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def _decode_current_instruction(self):
        """Read instruction and opcode at current pointer."""
        self.instr = self.memory[self.pointer]
        self.opcode = self.instr % 100

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
        output_value = self._process_parameters(1)
        self.outputs.append(output_value)
        self.pointer += 2
        return output_value

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
        self.relative_base += self._process_parameters(1)
        self.pointer += 2


if __name__ == "__main__":
    import env
    from tests import tests_intcode
    tests_intcode.tests()
