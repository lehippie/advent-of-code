"""Puzzle."""

from pathlib import Path


INPUT_FILE = "puzzle_input.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.strip() for line in f]
    return data


# --- Part One ---

def part_one(puzzle_input):
    """Part One solution."""


# --- Part Two ---

def part_two(puzzle_input):
    """Part Two solution."""


# --- Tests ---

def tests():
    """Day tests."""
    # Part One
    # Part Two


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
