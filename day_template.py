"""Puzzle."""

from pathlib import Path


PUZZLE_INPUT_FILE = None
ANSWER_PART_ONE = None
ANSWER_PART_TWO = None


class Puzzle:
    def __init__(self, puzzle_input=None):
        self.input = puzzle_input

    @classmethod
    def from_file(cls, filename):
        filepath = Path(__file__).parent / filename
        with open(filepath) as f:
            # Edit input file parsing here
            puzzle_input = [line.rstrip() for line in f]
        return cls(puzzle_input)

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented


def tests():
    assert Puzzle().part_one() is NotImplemented
    assert Puzzle().part_two() is NotImplemented


def solve(puzzle_input, answer_one, answer_two):
    puzzle = Puzzle.from_file(puzzle_input)
    result_one = puzzle.part_one()
    if answer_one is None:
        print("Part One answer:", result_one, "?")
    else:
        assert result_one == answer_one
        result_two = puzzle.part_two()
        if answer_two is None:
            print("Part Two answer:", result_two, "?")
        else:
            assert result_two == answer_two
            print("Day completed \o/")


if __name__ == "__main__":
    tests()
    if PUZZLE_INPUT_FILE:
        solve(PUZZLE_INPUT_FILE, ANSWER_PART_ONE, ANSWER_PART_TWO)
    else:
        print("No input given.")
