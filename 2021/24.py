"""Day 24: Arithmetic Logic Unit."""

from numpy import nan
from aoc.puzzle import Puzzle


def run_ALU(program, variables):
    for instruction in program:
        cmd, a, b = instruction.split()
        b = int(variables.get(b, b))
        if cmd == "add":
            variables[a] += b
        elif cmd == "mul":
            variables[a] *= b
        elif cmd == "div":
            variables[a] //= b
        elif cmd == "eql":
            variables[a] = int(variables[a] == b)
    return variables["z"]


class Today(Puzzle):
    """Today is reverse engineering day!

    The input is divided in 14 blocks, each doing almost the same calculations.
    Shared instructions are:
    - w is only used to store the input digit
    - x is always initialized to z % 26
    - y is always initialized to 25

    =>  Thus, we can skip some instructions to speed the search and
        z is the only value to keep from one block to the next.

    It's still a slow brute-force answer with minimum analysis but at least
    each part runs in around 15 minutes.
    """

    def parser(self):
        self.blocks = []
        for line in self.input:
            if "inp" in line:
                self.blocks.append([])
            self.blocks[-1].append(line)
        # print(*self.blocks, sep="\n")
        for block in self.blocks:
            block.remove("inp w")
            block.remove("mul x 0")
            block.remove("add x z")
            block.remove("mod x 26")
            block.remove("mul y 0")
            block.remove("add y 25")

    def part_one(self, method=max):
        """Each block is run against each 9 digits as input. Between each, only
        valid z outputs are kept with the highest model number leading to it.
        """
        input_states = {0: 0}
        for block in self.blocks:
            # print(self.blocks.index(block), len(input_states))
            outputs = {}
            for w in range(1, 10):
                for z, model in input_states.items():
                    z = run_ALU(block, {"w": w, "x": z % 26, "y": 25, "z": z})
                    outputs[z] = method(model * 10 + w, outputs.get(z, nan))
            input_states = outputs
        return outputs[0]

    def part_two(self):
        """Same as part one but by keeping the lowest model number."""
        return self.part_one(method=min)


if __name__ == "__main__":
    Today().solve()
