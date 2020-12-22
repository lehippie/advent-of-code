"""Puzzle."""

from pathlib import Path


# --- Parsing input ---

def parse_input(filename):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        data = [line.rstrip() for line in f]
    return data


# --- Part One ---

def part_one(puzzle_input):
    return NotImplemented


# --- Part Two ---

def part_two(puzzle_input):
    return NotImplemented


# --- Tests & Run ---

def tests():
    test = parse_input("README.md")
    assert part_one(test)
    assert part_two(test)


if __name__ == "__main__":
    tests()

    puzzle_input = parse_input("README.md")

    result_one = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one

    result_two = part_two(puzzle_input)
    print(f"Part Two answer: {result_two}")
    assert result_two
