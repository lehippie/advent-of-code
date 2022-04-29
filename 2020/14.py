"""Day 14: Docking Data."""

import re
from collections import Counter
from itertools import product
from aoc.puzzle import Puzzle


class PortComputer:
    def __init__(self, program):
        self.program = program
        self.mask = ""
        self.memory = {}

    def write(self, address, value):
        mOR = self.mask.replace("X", "0")
        mAND = self.mask.replace("X", "1")
        self.memory[address] = (value | int(mOR, 2)) & int(mAND, 2)

    def run(self):
        for instruction in self.program:
            action, value = instruction.split(" = ")
            if action == "mask":
                self.mask = value
            else:
                address = re.findall(r"\[(\d+)\]", action)[0]
                self.write(int(address), int(value))


class PortComputerV2(PortComputer):
    def write(self, address, value):
        # Erase 1's in address where X's are
        mask = self.mask.replace("1", "0").replace("X", "1")
        address = address & ~int(mask, 2)
        # Store value in floating addresses
        for combination in product("01", repeat=Counter(self.mask)["X"]):
            mask_bits = self.mask
            for c in combination:
                mask_bits = mask_bits.replace("X", c, 1)
            self.memory[address | int(mask_bits, 2)] = value


class Today(Puzzle):
    def part_one(self):
        docking = PortComputer(self.input)
        docking.run()
        return sum(docking.memory.values())

    def part_two(self):
        docking = PortComputerV2(self.input)
        docking.run()
        return sum(docking.memory.values())


solutions = (10885823581193, 3816594901962)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
