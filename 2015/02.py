"""Day 2: I Was Told There Would Be No Math."""

from math import prod
from pathlib import Path


PUZZLE_INPUT_FILE = "inputs/02.txt"
ANSWER_PART_ONE = 1586300
ANSWER_PART_TWO = 3737498


class Puzzle:
    def __init__(self, puzzle_input=None):
        self.presents = puzzle_input

    @classmethod
    def from_file(cls, filename):
        filepath = Path(__file__).parent / filename
        with open(filepath) as f:
            puzzle_input = [tuple(map(int, line.rstrip().split("x"))) for line in f]
        return cls(puzzle_input)

    def part_one(self):
        faces = [(l * w, w * h, h * l) for l, w, h in self.presents]
        return sum(2 * sum(f) + min(f) for f in faces)

    def part_two(self):
        ribbons = 0
        for present in self.presents:
            lengths = sorted(present)
            ribbons += 2 * sum(lengths[0:2]) + prod(lengths)
        return ribbons


def tests():
    assert Puzzle([(2, 3, 4)]).part_one() == 58
    assert Puzzle([(1, 1, 10)]).part_one() == 43
    assert Puzzle([(2, 3, 4)]).part_two() == 34
    assert Puzzle([(1, 1, 10)]).part_two() == 14


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
