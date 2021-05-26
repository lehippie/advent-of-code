"""Day 3: Perfectly Spherical Houses in a Vacuum."""

from pathlib import Path


PUZZLE_INPUT_FILE = "inputs/03.txt"
ANSWER_PART_ONE = 2572
ANSWER_PART_TWO = 2631


class Santa():
    def __init__(self):
        self.x, self.y = 0, 0

    @property
    def position(self):
        return self.x, self.y

    def move(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        elif direction == ">":
            self.x += 1
        elif direction == "<":
            self.x -= 1
        return self.position


class Puzzle:
    def __init__(self, puzzle_input=None):
        self.input = puzzle_input

    @classmethod
    def from_file(cls, filename):
        filepath = Path(__file__).parent / filename
        with open(filepath) as f:
            puzzle_input = f.readline().rstrip()
        return cls(puzzle_input)

    def part_one(self):
        santa = Santa()
        houses = {santa.position}
        for direction in self.input:
            houses.add(santa.move(direction))
        return len(houses)

    def part_two(self):
        santa = Santa()
        robot = Santa()
        houses = {santa.position}
        for i, direction in enumerate(self.input):
            if i % 2:
                houses.add(santa.move(direction))
            else:
                houses.add(robot.move(direction))
        return len(houses)


def tests():
    assert Puzzle(">").part_one() == 2
    assert Puzzle("^>v<").part_one() == 4
    assert Puzzle("^v^v^v^v^v").part_one() == 2
    assert Puzzle("^v").part_two() == 3
    assert Puzzle("^>v<").part_two() == 3
    assert Puzzle("^v^v^v^v^v").part_two() == 11


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
