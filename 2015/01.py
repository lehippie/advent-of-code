"""Day 1: Not Quite Lisp."""

from collections import Counter

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
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


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        tests={
            "part_one": [
                ("(())", 0),
                ("()()", 0),
                ("(((", 3),
                ("(()(()(", 3),
                ("))(((((", 3),
                ("())", -1),
                ("))(", -1),
                (")))", -3),
                (")())())", -3),
            ],
            "part_two": [(")", 1), ("()())", 5)],
        },
        solution_one=74,
        solution_two=1795,
    )

    if puzzle.test():
        puzzle.solve()
