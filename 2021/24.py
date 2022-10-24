"""Day 24: Arithmetic Logic Unit."""

from aoc.puzzle import Puzzle


class ALU:
    def __init__(self, input_number, program):
        self.inputs = (int(d) for d in str(input_number))
        self.program = program
        self.mem = {"w": 0, "x": 0, "y": 0, "z": 0}

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
        self.mem[var] = next(self.inputs)

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
            if cmd != "inp":
                v[1] = int(self.mem.get(v[1], v[1]))
            self.instructions[cmd](*v)


class Today(Puzzle):
    def part_one(self):
        for i in range(99999999999999, 1, -1):
            if "0" in str(i):
                continue
            alu = ALU(i, self.input)
            alu.run()
            if alu.mem["z"] == 0:
                return i

    def part_two(self):
        return super().part_two()


solutions = (None, None)

if __name__ == "__main__":
    # Today(solutions=solutions).solve()
    t = Today()
    print(t.__class__())
