"""Intcode computer class."""

class Intcode:
    def __init__(self, program):
        self.memory = {k: v for k, v in enumerate(program)}
        self.pointer = 0
        self.base = 0
        self.inputs = []
        self.outputs = []
        self.waiting_for_input = False

    def __getitem__(self, k):
        return self.memory.get(k, 0)

    def run(self, *inputs, pause_on_output=True):
        self.inputs.extend(inputs)
        if self.inputs:
            self.waiting_for_input = False

        while self[self.pointer] != 99:
            modes, opcode = divmod(self[self.pointer], 100)
            if opcode == 3 and not self.inputs:
                self.waiting_for_input = True
                return None
            instruction, n_params = self.opcodes[opcode]
            addresses = self.process_modes(n_params, modes)
            instruction(self, *addresses)
            if pause_on_output and self.outputs:
                return self.outputs.pop()

    def process_modes(self, n, modes):
        a = []
        for k in range(1, n + 1):
            modes, mode = divmod(modes, 10)
            if mode == 0:
                a.append(self[self.pointer + k])
            elif mode == 1:
                a.append(self.pointer + k)
            elif mode == 2:
                a.append(self[self.pointer + k] + self.base)
        return a

    @property
    def is_running(self):
        return self[self.pointer] != 99

    ####################
    #   Instructions   #
    ####################

    def _add(self, a, b, r):
        self.memory[r] = self[a] + self[b]
        self.pointer += 4

    def _multiply(self, a, b, r):
        self.memory[r] = self[a] * self[b]
        self.pointer += 4

    def _input(self, addr):
        self.memory[addr] = self.inputs.pop(0)
        self.pointer += 2

    def _output(self, addr):
        self.outputs.append(self[addr])
        self.pointer += 2

    def _jump_if_true(self, test, addr):
        if self[test]:
            self.pointer = self[addr]
        else:
            self.pointer += 3

    def _jump_if_false(self, test, addr):
        if not self[test]:
            self.pointer = self[addr]
        else:
            self.pointer += 3

    def _less_than(self, a, b, r):
        self.memory[r] = int(self[a] < self[b])
        self.pointer += 4

    def _equals(self, a, b, r):
        self.memory[r] = int(self[a] == self[b])
        self.pointer += 4

    def _adjust_base(self, addr):
        self.base += self[addr]
        self.pointer += 2

    opcodes = {
        1: (_add, 3),
        2: (_multiply, 3),
        3: (_input, 1),
        4: (_output, 1),
        5: (_jump_if_true, 2),
        6: (_jump_if_false, 2),
        7: (_less_than, 3),
        8: (_equals, 3),
        9: (_adjust_base, 1),
    }
