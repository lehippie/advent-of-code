"""Day 17: Trick Shot."""

import re
from itertools import product
from aoc.puzzle import Puzzle


class Probe:
    def __init__(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.positions = {(self.x, self.y)}

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx = max(self.vx - 1, 0)
        self.vy -= 1
        self.positions.add((self.x, self.y))


class Puzzle17(Puzzle):
    def parser(self):
        self.target = list(map(int, re.findall(r"-?\d+", self.input)))

    def part_one(self):
        """No need to worry about x because the best height
        is the same for any vx value ending up stabilizing
        the probe in target xrange.

        Best height is vy * (vy + 1) / 2 so we need to max
        vy. As the probe always comes back to y = 0, its
        first depth is -(vy + 1) that is limeted by target
        low bound.
        """
        self.vymax = -self.target[2] - 1
        return self.vymax * (self.vymax + 1) // 2

    def part_two(self):
        """Part_one result is vy upper bound."""
        count = 0
        xmin, xmax, ymin, ymax = self.target
        target = set(product(range(xmin, xmax + 1), range(ymin, ymax + 1)))
        vxmin = next(vx for vx in range(xmin) if xmin <= vx * (vx + 1) / 2 <= xmax)
        for vx in range(vxmin, xmax + 1):
            for vy in range(ymin, self.vymax + 1):
                probe = Probe(vx, vy)
                while probe.x <= xmax and probe.y >= ymin:
                    probe.move()
                if probe.positions.intersection(target):
                    count += 1
        return count


if __name__ == "__main__":
    Puzzle17(solutions=(15400, 5844)).solve()
