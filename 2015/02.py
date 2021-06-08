"""Day 2: I Was Told There Would Be No Math."""

from math import prod

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self):
        faces = [(l * w, w * h, h * l) for l, w, h in self.input]
        return sum(2 * sum(f) + min(f) for f in faces)

    def part_two(self):
        ribbons = 0
        for present in self.input:
            lengths = sorted(present)
            ribbons += 2 * sum(lengths[0:2]) + prod(lengths)
        return ribbons


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        parser=lambda line: tuple(map(int, line.split("x"))),
        tests={
            "part_one": [(["2x3x4"], 58), (["1x1x10"], 43)],
            "part_two": [(["2x3x4"], 34), (["1x1x10"], 14)],
        },
        solution_one=1586300,
        solution_two=3737498,
    )

    if puzzle.test():
        puzzle.solve()
