"""Day 9: Encoding Error."""

from itertools import combinations
from pathlib import Path


INPUT_FILE = "port_output.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [int(line.strip()) for line in f]
    return data


# --- Part One ---

def xmas_invalid_number(numbers, preamble=25):
    for k, n in enumerate(numbers):
        if k < preamble:
            continue
        try:
            _ = next(c for c in combinations(numbers[k-preamble:k], 2)
                       if sum(c) == n)
        except StopIteration:
            return n


def part_one(port_output):
    """Part One solution."""
    invalid = xmas_invalid_number(port_output)
    print(f"First failing number: {invalid}")
    assert invalid == 41682220
    return invalid


# --- Part Two ---

def xmas_weakness(numbers, invalid):
    for k, n in enumerate(numbers):
        add = [n]
        l = 0
        while sum(add) < invalid:
            l += 1
            add.append(numbers[k+l])
        if sum(add) == invalid:
            return min(add) + max(add)


def part_two(port_output, invalid):
    """Part Two solution."""
    weakness = xmas_weakness(port_output, invalid)
    print(f"Encryption weakness: {weakness}")
    assert weakness == 5388976


# --- Tests ---

def tests():
    # Part One
    test = load_input("test_input.txt")
    test_invalid = xmas_invalid_number(test, 5)
    assert test_invalid == 127
    # Part Two
    assert xmas_weakness(test, test_invalid) == 62


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    invalid = part_one(puzzle_input)
    part_two(puzzle_input, invalid)
