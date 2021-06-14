"""Puzzle template."""

from itertools import groupby

from aoc.puzzle import Puzzle


def look_and_say(look):
    return "".join(f"{len(list(g))}{n}" for n, g in groupby(look))


class TodayPuzzle(Puzzle):
    def part_one(self, steps=40):
        for _ in range(steps):
            self.input = look_and_say(self.input)
        return len(self.input)

    def part_two(self):
        return self.part_one(10)


if __name__ == "__main__":
    TodayPuzzle(solutions=(492982, 6989950)).solve()
