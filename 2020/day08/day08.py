"""Day 8: Handheld Halting."""

from copy import deepcopy
from pathlib import Path


INPUT_FILE = "boot_code.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.strip().split() for line in f]
    return [[op, int(arg)] for op, arg in data]


# --- Part One ---

class Console():
    """Handheld console class."""

    def __init__(self, instructions):
        self.instructions = instructions
        self.position = 0
        self.accumulator = 0

    def execute_next_instruction(self):
        operation, argument = self.instructions[self.position]
        if operation == "acc":
            self.accumulator += argument
            self.position += 1
        elif operation == "jmp":
            self.position += argument
        elif operation == "nop":
            self.position += 1
        else:
            raise IOError(f"Unknown operation '{operation}'.")

    @property
    def is_finished(self):
        return self.position == len(self.instructions)

    @property
    def will_loop(self):
        """Check if the instructions are making a loop."""
        count = [0] * len(self.instructions)
        while count[self.position] == 0:
            count[self.position] += 1
            self.execute_next_instruction()
            if self.is_finished:
                return False
        return True


def part_one(boot_code):
    """Part One solution."""
    console = Console(boot_code)
    assert console.will_loop
    print(f"Accumulator value was {console.accumulator} just before looping.")
    assert console.accumulator == 1179


# --- Part Two ---

def fix_code(boot_code):
    for k in range(len(boot_code)):
        modified_code = deepcopy(boot_code)
        if modified_code[k][0] == "jmp":
            modified_code[k][0] = "nop"
        elif modified_code[k][0] == "nop":
            modified_code[k][0] = "jmp"
        else:
            continue
        console = Console(modified_code)
        if not console.will_loop:
            return console.accumulator


def part_two(boot_code):
    """Part Two solution."""
    final_acc = fix_code(boot_code)
    print(f"Accumulator value is {final_acc} after termination.")
    assert final_acc == 1089


# --- Tests ---

def tests():
    # Part One
    test = Console(load_input("test_input.txt"))
    assert test.will_loop
    assert test.accumulator == 5
    # Part Two
    test = load_input("test_input.txt")
    test[0][0] = "jmp"
    assert Console(test).will_loop
    test = load_input("test_input.txt")
    test[2][0] = "nop"
    assert Console(test).will_loop
    test = load_input("test_input.txt")
    test[4][0] = "nop"
    assert Console(test).will_loop
    assert fix_code(load_input("test_input.txt")) == 8


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
