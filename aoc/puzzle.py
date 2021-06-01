"""Base puzzle class."""

class Puzzle:
    def __init__(self, puzzle_input=None, solution_one=None, solution_two=None):
        self.input = puzzle_input
        self.solution_one = solution_one
        self.solution_two = solution_two

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def solve(self):
        answer_one = self.part_one()
        if self.solution_one is None:
            print("Part One answer:", answer_one, "?")
        else:
            assert answer_one == self.solution_one
            answer_two = self.part_two()
            if self.solution_two is None:
                print("Part Two answer:", answer_two, "?")
            else:
                assert answer_two == self.solution_two
                print("Day completed \o/")
