"""Puzzle template."""

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self):
        return super().part_one()

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        tests={
            "part_one": [("test_value", "test_result")],
            # "part_two": [("test_value", "test_result")],
        },
        solution_one=None,
        solution_two=None,
    )
    if puzzle.test():
        puzzle.solve()
