"""Intcode computer."""


class Intcode():
    """Intcode computer class.

    Arguments:
        program -- Program loaded in the computer memory.
                   Can be a list of int OR the path to a file
                   containig such list on its first line.
        name -- Name of the Intcode computer's instance.
    """

    def __init__(self, program, name='Unnamed'):
        """Initial computer state."""
        self.name = name
        self.initial_program = self._read_initial_program(program)
        self._memory = {i:v for i, v in enumerate(self.initial_program)}
        self.instructions = self.known_instructions()
        self.pointer = 0
        self.relative_base = 0
        self.inputs = []
        self.outputs = []
        self.waiting_for_input = False
        self.finished = False
        self._decode_instruction_at_pointer()

    def known_instructions(self):
        """Return a dict of available instructions."""
        return {1: self._instr_add,
                2: self._instr_multiply,
                3: self._instr_input,
                4: self._instr_output,
                5: self._instr_jump_if_true,
                6: self._instr_jump_if_false,
                7: self._instr_less_than,
                8: self._instr_equals,
                9: self._instr_relative_base_offset}

    def __repr__(self):
        return f"Intcode({self.initial_program}, {self.name})"

    def __str__(self):
        return self.name


    #######################
    ####    MEMORY     ####
    #######################

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

    def __getitem__(self, address):
        """Answers instance's call with memory content."""
        if isinstance(address, int):
            return self._memory.get(address, 0)
        elif isinstance(address, slice):
            if address.start is None:
                start = 0
            if address.stop is None:
                stop = max(self._memory.keys()) + 1
            if address.step is None:
                step = 1
            return [self._memory.get(a, 0) for a in range(start, stop, step)]

    def __setitem__(self, address, value):
        """Write in memory when calling instance."""
        self._memory[address] = value


    ##########################
    ####    EXECUTION     ####
    ##########################

    def _process_input_values(self, input_values):
        """Add new values to pending input list."""
        if input_values is not None:
            if isinstance(input_values, int):
                input_values = [input_values]
            self.inputs.extend(input_values)
            self.waiting_for_input = False

    def _decode_instruction_at_pointer(self):
        """Read instruction and opcode at current pointer."""
        self.instr = self[self.pointer]
        self.opcode = self.instr % 100
        if self.opcode == 99:
            self.finished = True

    def _execute_current_instruction(self):
        """Call correct instruction from current memory state."""
        if self.opcode in self.instructions:
            rc = self.instructions[self.opcode]()
        else:
            raise IOError(f"Unknown opcode '{self.opcode}'"
                        f" at address {self.pointer}.")
        return rc

    def execute_next(self, input_values=None):
        """Execute next instruction and check for end of program."""
        if not self.finished:
            self._process_input_values(input_values)
            rc = self._execute_current_instruction()
            self._decode_instruction_at_pointer()
            return rc

    def run(self, input_values=None, halt_on_output=False):
        """Run the full program and return the outputs.

        If an input value is needed the program is halted.
        If <halt_on_output> is True, an output instruction
        halts the program.
        """
        self._process_input_values(input_values)
        while not self.finished:
            rc = self.execute_next()
            if self.waiting_for_input:
                return
            if halt_on_output and rc is not None:
                return rc
        if not halt_on_output:
            if len(self.outputs) == 1:
                return self.outputs[0]
            else:
                return self.outputs

    def reset(self):
        """Restore Program to initial state."""
        self.__init__(self.initial_program)


    ###############################
    ####    PARAMETER MODES    ####
    ###############################

    def _process_parameters(self, nb_param):
        """Return correct parameters addresses from instruction's modes."""
        addresses = list(range(self.pointer + 1, self.pointer + 1 + nb_param))
        values = [self[a] for a in addresses]
        modes = [int(i) for i in str(self.instr//100).zfill(nb_param)[::-1]]
        params_addresses = []
        for a, v, m in zip(addresses, values, modes):
            if m == 0:      # Position mode
                params_addresses.append(v)
            elif m == 1:    # Immediate mode
                params_addresses.append(a)
            elif m == 2:    # Relative mode
                params_addresses.append(self.relative_base + v)
        if nb_param == 1:
            params_addresses = params_addresses[0]
        return params_addresses


    ############################
    ####    INSTRUCTIONS    ####
    ############################

    def _instr_add(self):
        """Addition instruction (opcode 1).

        Adds values of two parameters and stores
        the result at a third one.
        """
        a, b, result = self._process_parameters(3)
        self[result] = self[a] + self[b]
        self.pointer += 4

    def _instr_multiply(self):
        """Multiplication instruction (opcode 2).

        Multiplies values of two parameters and stores
        the result at a third one.
        """
        a, b, result = self._process_parameters(3)
        self[result] = self[a] * self[b]
        self.pointer += 4

    def _instr_input(self):
        """Input instruction (opcode 3).

        Write next pending input value at given parameter.
        Do nothing if no input value is available.
        """
        if not self.inputs:
            self.waiting_for_input = True
        else:
            address = self._process_parameters(1)
            self[address] = self.inputs.pop(0)
            self.pointer += 2

    def _instr_output(self):
        """Output instruction (opcode 4).

        Return the value at given parameter.
        """
        value = self[self._process_parameters(1)]
        self.outputs.append(value)
        self.pointer += 2
        return value

    def _instr_jump_if_true(self):
        """Jump-if-true instruction (opcode 5).

        If first parameter is non-zero, sets the pointer at second parameter.
        Otherwise, does nothing.
        """
        a, b = self._process_parameters(2)
        if self[a]:
            self.pointer = self[b]
        else:
            self.pointer += 3

    def _instr_jump_if_false(self):
        """Jump-if-false instruction (opcode 6).

        If first parameter is zero, sets the pointer at second parameter.
        Otherwise, does nothing.
        """
        a, b = self._process_parameters(2)
        if not self[a]:
            self.pointer = self[b]
        else:
            self.pointer += 3

    def _instr_less_than(self):
        """Comparison instruction (opcode 7).

        If first parameter is less than second parameter, stores 1 at
        third parameter. Otherwise, stores 0.
        """
        a, b, result = self._process_parameters(3)
        self[result] = int(self[a] < self[b])
        self.pointer += 4

    def _instr_equals(self):
        """Equality instruction (opcode 8).

        If first and second parameters are equals, stores 1 at
        third parameter. Otherwise, stores 0.
        """
        a, b, result = self._process_parameters(3)
        self[result] = int(self[a] == self[b])
        self.pointer += 4

    def _instr_relative_base_offset(self):
        """Relative base offset instruction (opcode 9).

        Increases the relative base by the value of the parameter.
        That value can be negative.
        """
        self.relative_base += self[self._process_parameters(1)]
        self.pointer += 2


if __name__ == "__main__":
    from intcode_tests import tests
    tests()
