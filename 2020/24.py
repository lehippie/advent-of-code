"""Day 24: Lobby Layout."""

import re
from aoc.puzzle import Puzzle


def neighbors(x, y):
    return {
        (x + 1, y),
        (x + 1, y - 1),
        (x, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y + 1),
    }


class Puzzle24(Puzzle):
    def parser(self):
        return [re.findall(r"[ns]?[ew]", line) for line in self.input]

    def part_one(self):
        self.blacks = set()
        for tile in self.input:
            x, y = 0, 0
            for step in tile:
                if step == "e":
                    x += 1
                elif step == "se":
                    x += 1
                    y -= 1
                elif step == "sw":
                    y -= 1
                elif step == "w":
                    x -= 1
                elif step == "nw":
                    x -= 1
                    y += 1
                elif step == "ne":
                    y += 1
            if (x, y) in self.blacks:
                self.blacks.remove((x, y))
            else:
                self.blacks.add((x, y))
        return len(self.blacks)

    def part_two(self):
        for _ in range(100):
            next_blacks = set()
            whites_to_check = set()
            for black in self.blacks:
                around = neighbors(*black)
                if len(around.intersection(self.blacks)) in {1, 2}:
                    next_blacks.add(black)
                whites_to_check.update(around.difference(self.blacks))
            for white in whites_to_check:
                if len(neighbors(*white).intersection(self.blacks)) == 2:
                    next_blacks.add(white)
            self.blacks = next_blacks
        return len(self.blacks)


if __name__ == "__main__":
    Puzzle24(solutions=(436, 4133)).solve()
