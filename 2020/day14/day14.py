"""Day 14: Docking Data."""

import re
from itertools import product
from pathlib import Path


INPUT_FILE = "initialization_program.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.rstrip() for line in f]
    return data


# --- Part One ---

class PortComputer():
    def __init__(self, program):
        self.program = program
        self.mask = ""
        self.memory = {}

    def write(self, address, value):
        mask_or = int(self.mask.replace("X", "0"), 2)
        mask_and = int(self.mask.replace("1", "X")
                                .replace("0", "1")
                                .replace("X", "0"), 2)
        self.memory[address] = (value | mask_or) & ~mask_and

    def run(self):
        for instruction in self.program:
            action, value = instruction.split(" = ")
            if action == "mask":
                self.mask = value
            else:
                address = re.findall(r"\[(\d+)\]", action)[0]
                self.write(int(address), int(value))


def part_one(puzzle_input):
    """Part One solution."""
    docking = PortComputer(puzzle_input)
    docking.run()
    result = sum(docking.memory.values())
    print(f"Sum of memory values: {result}")
    assert result == 10885823581193


# --- Part Two ---

class PortComputerV2(PortComputer):
    def write(self, address, value):
        # Erase 1's in address where X's are
        Xpos = [i for i, m in enumerate(self.mask) if m == "X"]
        address = f"{address:036b}"
        for X in Xpos:
            address = address[:X] + "0" + address[X+1:]
        address = int(address, 2)
        # Store value in floating addresses
        for combination in product("01", repeat=len(Xpos)):
            mask_bits = self.mask
            for c in combination:
                mask_bits = mask_bits.replace("X", c, 1)
            self.memory[address | int(mask_bits, 2)] = value


def part_two(puzzle_input):
    """Part Two solution."""
    docking = PortComputerV2(puzzle_input)
    docking.run()
    result = sum(docking.memory.values())
    print(f"Sum of memory values (v2): {result}")
    assert result == 3816594901962


# --- Tests ---

def tests():
    # Part One
    test = PortComputer(load_input("test_01.txt"))
    test.run()
    assert sum(test.memory.values()) == 165
    # Part Two
    test = PortComputerV2(load_input("test_02.txt"))
    test.run()
    assert sum(test.memory.values()) == 208


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
