"""Puzzle."""

from pathlib import Path


INPUT = "puzzle_input.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.strip() for line in f]
    return data


def tests():
    """Day tests."""


def part_one(puzzle_input):
    """Part One solution."""


def part_two(puzzle_input):
    """Part Two solution."""


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT)
    part_one(puzzle_input)
    part_two(puzzle_input)
