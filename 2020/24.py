"""Day 24: Lobby Layout."""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.tiles = [re.findall(r"[ns]?[ew]", line) for line in self.input]

    def part_one(self):
        """An hex grid only need two coordinates. The x axis
        spans from west to east and the y axis from south-west
        to north-east.
        """
        self.blacks = set()
        for tile in self.tiles:
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
        def neighbors(x, y):
            return {
                (x + 1, y),
                (x + 1, y - 1),
                (x, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y + 1),
            }

        blacks = set(self.blacks)
        stay_black = {1, 2}
        for _ in range(100):
            next_blacks = set()
            whites_queue = set()
            for black in blacks:
                around = neighbors(*black)
                if len(around.intersection(blacks)) in stay_black:
                    next_blacks.add(black)
                whites_queue.update(around.difference(blacks))
            for white in whites_queue:
                if len(neighbors(*white).intersection(blacks)) == 2:
                    next_blacks.add(white)
            blacks = next_blacks
        return len(blacks)


if __name__ == "__main__":
    Today().solve()
