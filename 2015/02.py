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
    TodayPuzzle(
        parser=lambda line: tuple(map(int, line.split("x"))),
        parse_lines=True,
        solutions=(1586300, 3737498),
    ).solve()
