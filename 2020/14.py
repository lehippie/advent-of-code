"""Day 14: Docking Data."""

from itertools import product
from aoc.puzzle import Puzzle


class DockingSystem:
    def __init__(self, program):
        self.program = program
        self.mask = ""
        self.memory = {}

    def __setitem__(self, address: int, value: int):
        """Applying the mask is equivalent to two conventionnal
        bitmasks: OR with X -> 0 and AND with X -> 1.
        """
        maskOR = int(self.mask.replace("X", "0"), 2)
        maskAND = int(self.mask.replace("X", "1"), 2)
        self.memory[address] = (value | maskOR) & maskAND

    def run(self):
        for instruction in self.program:
            action, value = instruction.split(" = ")
            if action == "mask":
                self.mask = value
            else:
                self[int(action[4:-1])] = int(value)
        return sum(self.memory.values())


class DockingSystemV2(DockingSystem):
    def __setitem__(self, address: int, value: int):
        """To generate all addresses where the value is written, the
        fixed part of the address is first obtained by applying the
        mask without the Xs.
        Then, these are replaced by every combination of 0 and 1.
        """
        mask = int(self.mask.replace("X", "0"), 2)
        fixed = f"{bin(address | mask)[2:]:0>36}"
        fixed = "".join(m if m == "X" else b for m, b in zip(self.mask, fixed))
        for combination in product("01", repeat=fixed.count("X")):
            addr = fixed
            for c in combination:
                addr = addr.replace("X", c, 1)
            self.memory[int(addr, 2)] = value


class Today(Puzzle):
    def part_one(self, system=DockingSystem):
        return system(self.input).run()

    def part_two(self):
        return self.part_one(DockingSystemV2)


solutions = (10885823581193, 3816594901962)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
