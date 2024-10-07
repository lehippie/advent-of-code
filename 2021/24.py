"""Day 24: Arithmetic Logic Unit."""

from collections import defaultdict
from aoc.puzzle import Puzzle


class ALU:
    def __init__(self, program):
        self.program = program
        self.var = {"w": 0, "x": 0, "y": 0, "z": 0}

    def run(self):
        for instruction in self.program:
            cmd, a, b = instruction.split()
            b = int(self.var.get(b, b))
            if cmd == "add":
                self.var[a] += b
            elif cmd == "mul":
                self.var[a] *= b
            elif cmd == "div":
                self.var[a] //= b
            elif cmd == "mod":
                self.var[a] %= b
            elif cmd == "eql":
                self.var[a] = int(self.var[a] == b)


class Today(Puzzle):
    def parser(self):
        """MONAD code is separated in blocks starting with "inp w"."""
        self.blocks = []
        for line in self.input:
            if "inp" in line:
                self.blocks.append(ALU([]))
            else:
                self.blocks[-1].program.append(line)
        # print(*(block.program for block in self.blocks), sep="\n")

    def part_one(self, method=max):
        """Looking at the blocks content, some pattern can be deduced:
        - w is only used to store the input digit
        - x and y are always set to 0 before being used
            => only z is kept from one block to the next
        """
        states = {0: 0}
        for b, block in enumerate(self.blocks):
            print(b, len(states))
            outputs = defaultdict(int)
            for w in range(1, 10):
                for z, previous_model in states.items():
                    model = int(f"{previous_model}{w}")
                    block.var["w"] = w
                    block.var["z"] = z
                    block.run()
                    outputs[block.var["z"]] = method(model, block.var["z"])
            states = outputs
        return outputs[0]

    def part_two(self):
        return self.part_one(method=min)


if __name__ == "__main__":
    Today().solve()
