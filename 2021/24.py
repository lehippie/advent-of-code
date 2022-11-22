"""Day 24: Arithmetic Logic Unit."""

from aoc.puzzle import Puzzle


class ALU:
    def __init__(self, inputs, program, z=None):
        self.inputs = inputs[::-1] if isinstance(inputs, list) else [inputs]
        self.program = program
        self.mem = {"w": 0, "x": 0, "y": 0, "z": 0}
        if z is not None:
            self.mem["z"] = z

    @property
    def instructions(self):
        return {
            "inp": self.inp,
            "add": self.add,
            "mul": self.mul,
            "div": self.div,
            "mod": self.mod,
            "eql": self.eql,
        }

    def inp(self, var):
        self.mem[var] = self.inputs.pop()

    def add(self, var, value):
        self.mem[var] += value

    def mul(self, var, value):
        self.mem[var] *= value

    def div(self, var, value):
        self.mem[var] //= value

    def mod(self, var, value):
        self.mem[var] %= value

    def eql(self, var, value):
        self.mem[var] = 1 if self.mem[var] == value else 0

    def run(self):
        for instruction in self.program:
            cmd, *v = instruction.split()
            if len(v) > 1:
                v[1] = int(self.mem.get(v[1], v[1]))
            self.instructions[cmd](*v)


class Today(Puzzle):
    def parser(self):
        """MONAD code is separated in blocks each starting with an
        input instruction.
        """
        self.blocks = []
        for line in self.input:
            if "inp" in line:
                self.blocks.append([])
            self.blocks[-1].append(line)
        print(*self.blocks, sep="\n")

    def part_one(self):
        """From one block to another, w is used for input and x and y
        are set to 0. Thus, only the value of z needs to be stored
        for next block.
        """
        old = {0: 0}
        for block in self.blocks:
            new = {}
            for i in range(9, 0, -1):
                for z, n in old.items():
                    model = int(f"{n}{i}")
                    alu = ALU(i, block, z)
                    alu.run()
                    if alu.mem["z"] not in new or model > new[alu.mem["z"]]:
                        new[alu.mem["z"]] = model
            old = new
        return new[0]

    def part_two(self):
        old = {0: 0}
        for block in self.blocks:
            new = {}
            for i in range(1, 10):
                for z, n in old.items():
                    model = int(f"{n}{i}")
                    alu = ALU(i, block, z)
                    alu.run()
                    if alu.mem["z"] not in new or model < new[alu.mem["z"]]:
                        new[alu.mem["z"]] = model
            old = new
        return new[0]

solutions = (29989297949519, 19518121316118)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
