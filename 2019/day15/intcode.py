"""Intcode computer."""


class Intcode():
    """Intcode computer class.

    Arguments:
        program     Initial program as a list of int.
        name        Name of the Intcode computer's instance.
    """

    def __init__(self, program, name='Unnamed'):
        """Init Intcode computer."""
        self.name = name
        self.initial_program = program
        self.memory = {i:v for i, v in enumerate(self.initial_program)}
        self.instructions = self.known_instructions()
        self.pointer = 0
        self.relative_base = 0
        self.inputs = []
        self.outputs = []
        self.waiting_for_input = False
        self.finished = False
        self._decode_instruction_at_pointer()


    def __repr__(self):
        return f"Intcode({self.initial_program}, {self.name})"


    def __str__(self):
        return self.name


    @classmethod
    def from_file(cls, program, name='Unnamed'):
        """Init Intcode computer from a file."""
        with open(program) as f:
            init = f.readline()
        return cls([int(i) for i in init.split(',')], name)


    #######################
    ####    MEMORY     ####
    #######################

    def __getitem__(self, address):
        """Read memory content."""
        if isinstance(address, int):
            return self.memory.get(address, 0)
        elif isinstance(address, slice):
            start = address.start if address.start is not None else 0
            stop = address.stop if address.stop is not None else max(self.memory.keys()) + 1
            step = address.step if address.step is not None else 1
            return [self.memory.get(a, 0) for a in range(start, stop, step)]


    def __setitem__(self, address, value):
        """Write in memory."""
        self.memory[address] = value


    ##########################
    ####    EXECUTION     ####
    ##########################

    def execute_next(self, input_values=None):
        """Execute next instruction and check for end of program."""
        if not self.finished:
            self._process_input_values(input_values)
            rc = self._execute_current_instruction()
            self._decode_instruction_at_pointer()
            return rc


    def run(self, input_values=None, halt_on_output=True):
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


    def _process_input_values(self, input_values):
        """Add new values to pending input list."""
        if input_values is not None:
            if isinstance(input_values, int):
                input_values = [input_values]
            self.inputs.extend(input_values)
            self.waiting_for_input = False


    def _execute_current_instruction(self):
        """Call correct instruction from current memory state."""
        if self.opcode in self.instructions:
            rc = self.instructions[self.opcode]()
        else:
            raise IOError(f"Unknown opcode '{self.opcode}'"
                        f" at address {self.pointer}.")
        return rc


    ###############################
    ####    PARAMETER MODES    ####
    ###############################

    def _process_parameters(self, nb_param):
        """Return correct parameters addresses from instruction's modes."""
        addresses = list(range(self.pointer+1, self.pointer+1 + nb_param))
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

    def known_instructions(self):
        """Return a dict of available instructions."""
        return {
            1: self._instr_add,
            2: self._instr_multiply,
            3: self._instr_input,
            4: self._instr_output,
            5: self._instr_jump_if_true,
            6: self._instr_jump_if_false,
            7: self._instr_less_than,
            8: self._instr_equals,
            9: self._instr_relative_base_offset
        }


    def _decode_instruction_at_pointer(self):
        """Read instruction and opcode at current pointer."""
        self.instr = self[self.pointer]
        self.opcode = self.instr % 100
        if self.opcode == 99:
            self.finished = True


    def _instr_add(self):
        """Addition instruction (opcode 1).

        Adds values of two parameters and stores
        the result at a third one.
        """
        nb_param = 3
        a, b, result = self._process_parameters(nb_param)
        self[result] = self[a] + self[b]
        self.pointer += nb_param + 1


    def _instr_multiply(self):
        """Multiplication instruction (opcode 2).

        Multiplies values of two parameters and stores
        the result at a third one.
        """
        nb_param = 3
        a, b, result = self._process_parameters(nb_param)
        self[result] = self[a] * self[b]
        self.pointer += nb_param + 1


    def _instr_input(self):
        """Input instruction (opcode 3).

        Write next pending input value at given parameter.
        Do nothing if no input value is available.
        """
        nb_param = 1
        if not self.inputs:
            self.waiting_for_input = True
        else:
            address = self._process_parameters(nb_param)
            self[address] = self.inputs.pop(0)
            self.pointer += nb_param + 1


    def _instr_output(self):
        """Output instruction (opcode 4).

        Return the value at given parameter.
        """
        nb_param = 1
        value = self[self._process_parameters(nb_param)]
        self.outputs.append(value)
        self.pointer += nb_param + 1
        return value


    def _instr_jump_if_true(self):
        """Jump-if-true instruction (opcode 5).

        If first parameter is non-zero, sets the pointer at second parameter.
        Otherwise, does nothing.
        """
        nb_param = 2
        a, b = self._process_parameters(nb_param)
        if self[a]:
            self.pointer = self[b]
        else:
            self.pointer += nb_param + 1


    def _instr_jump_if_false(self):
        """Jump-if-false instruction (opcode 6).

        If first parameter is zero, sets the pointer at second parameter.
        Otherwise, does nothing.
        """
        nb_param = 2
        a, b = self._process_parameters(nb_param)
        if not self[a]:
            self.pointer = self[b]
        else:
            self.pointer += nb_param + 1


    def _instr_less_than(self):
        """Comparison instruction (opcode 7).

        If first parameter is less than second parameter, stores 1 at
        third parameter. Otherwise, stores 0.
        """
        nb_param = 3
        a, b, result = self._process_parameters(nb_param)
        self[result] = int(self[a] < self[b])
        self.pointer += nb_param + 1


    def _instr_equals(self):
        """Equality instruction (opcode 8).

        If first and second parameters are equals, stores 1 at
        third parameter. Otherwise, stores 0.
        """
        nb_param = 3
        a, b, result = self._process_parameters(nb_param)
        self[result] = int(self[a] == self[b])
        self.pointer += nb_param + 1


    def _instr_relative_base_offset(self):
        """Relative base offset instruction (opcode 9).

        Increases the relative base by the value of the parameter.
        That value can be negative.
        """
        nb_param = 1
        self.relative_base += self[self._process_parameters(nb_param)]
        self.pointer += nb_param + 1


def tests():
    ###########################
    ####    Day02 tests    ####
    ###########################

    i = Intcode([1,9,10,3,2,3,11,0,99,30,40,50])
    i.execute_next()
    assert i[:] == [1,9,10,70,2,3,11,0,99,30,40,50]
    i.execute_next()
    assert i[:] == [3500,9,10,70,2,3,11,0,99,30,40,50]

    i = Intcode([1,0,0,0,99])
    i.run()
    assert i[:] == [2,0,0,0,99]

    i = Intcode([2,3,0,3,99])
    i.run()
    assert i[:] == [2,3,0,6,99]

    i = Intcode([2,4,4,5,99,0])
    i.run()
    assert i[:] == [2,4,4,5,99,9801]

    i = Intcode([1,1,1,4,99,5,6,0,99])
    i.run()
    assert i[:] == [30,1,1,4,2,5,6,0,99]
    assert i.pointer == 8
    i.reset()
    assert i[:] == [1,1,1,4,99,5,6,0,99]

    ###########################
    ####    Day05 tests    ####
    ###########################

    i = Intcode([1002,4,3,4,33])
    i.run()
    assert i[:] == [1002,4,3,4,99]

    i = Intcode([1101,100,-1,4,0])
    i.run()
    assert i[:] == [1101,100,-1,4,99]

    i = Intcode([3,9,8,9,10,9,4,9,99,-1,8])
    assert i.run(8) == 1
    i.reset()
    assert i.run(66) == 0
    i.reset()
    assert i.run(-8) == 0

    i = Intcode([3,9,7,9,10,9,4,9,99,-1,8])
    assert i.run(7) == 1
    i.reset()
    assert i.run(8) == 0
    i.reset()
    assert i.run(42) == 0

    i = Intcode([3,3,1108,-1,8,3,4,3,99])
    assert i.run(8) == 1
    i.reset()
    assert i.run(66) == 0
    i.reset()
    assert i.run(-8) == 0

    i = Intcode([3,3,1107,-1,8,3,4,3,99])
    assert i.run(7) == 1
    i.reset()
    assert i.run(8) == 0
    i.reset()
    assert i.run(42) == 0

    i = Intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    assert i.run(0) == 0
    i.reset()
    assert i.run(500) == 1
    i.reset()
    assert i.run(-1) == 1

    i = Intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
    assert i.run(0) == 0
    i.reset()
    assert i.run(500) == 1
    i.reset()
    assert i.run(-1) == 1

    i = Intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    assert i.run(-123) == 999
    i.reset()
    assert i.run(8) == 1000
    i.reset()
    assert i.run(666) == 1001

    ###########################
    ####    Day09 tests    ####
    ###########################

    i = Intcode([109,19,204,-34])
    i.relative_base = 2000
    i.execute_next()
    assert i.relative_base == 2019
    i[1985] = 666
    assert i.execute_next() == 666

    quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    i = Intcode(quine)
    assert i.run(halt_on_output=False) == quine

    i = Intcode([1102,34915192,34915192,7,4,7,99,0])
    assert len(str(i.run())) == 16

    i = Intcode([104,1125899906842624,99])
    assert i.run() == 1125899906842624


if __name__ == "__main__":
    tests()
