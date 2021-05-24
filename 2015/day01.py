"""Day 1: Not Quite Lisp."""

from pathlib import Path
from collections import Counter


PUZZLE_INPUT_FILE = "day01_floors_instructions.txt"
ANSWER_PART_ONE = 74
ANSWER_PART_TWO = 1795


class Puzzle:
    def __init__(self, puzzle_input=""):
        self.input = puzzle_input

    @classmethod
    def from_file(cls, filename):
        filepath = Path(__file__).parent / filename
        with open(filepath) as f:
            puzzle_input = f.readline().strip()
        return cls(puzzle_input)

    def part_one(self):
        parentheses = Counter(self.input)
        return parentheses["("] - parentheses[")"]

    def part_two(self):
        floor = 0
        for i, p in enumerate(self.input):
            floor = (floor + 1) if p == "(" else (floor - 1)
            if floor == -1:
                break
        return i + 1


def tests():
    assert Puzzle("(())").part_one() == 0
    assert Puzzle("()()").part_one() == 0
    assert Puzzle("(((").part_one() == 3
    assert Puzzle("(()(()(").part_one() == 3
    assert Puzzle("))(((((").part_one() == 3
    assert Puzzle("())").part_one() == -1
    assert Puzzle("))(").part_one() == -1
    assert Puzzle(")))").part_one() == -3
    assert Puzzle(")())())").part_one() == -3
    assert Puzzle(")").part_two() == 1
    assert Puzzle("()())").part_two() == 5


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
