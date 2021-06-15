"""Puzzle template."""

from itertools import groupby

from aoc.puzzle import Puzzle


def look_and_say(look):
    return "".join(f"{len(list(g))}{n}" for n, g in groupby(look))


class TodayPuzzle(Puzzle):
    def part_one(self, steps=40, first_look=None):
        if first_look is None:
            self.last_said = self.input
        else:
            self.last_said = first_look

        for _ in range(steps):
            self.last_said = look_and_say(self.last_said)
        return len(self.last_said)

    def part_two(self):
        return self.part_one(10, first_look=self.last_said)


if __name__ == "__main__":
    TodayPuzzle(solutions=(492982, 6989950)).solve()
