"""Day 17: Trick Shot."""

import re
from itertools import product
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.target = list(map(int, re.findall(r"-?\d+", self.input)))

    def part_one(self):
        """No need to worry about x because the maximum height is
        reached for any vx value ending up stabilizing the probe in
        target range.

        Maximum height is vy * (vy + 1) / 2 so we simply need to
        maximize vy. As the probe always comes back to y = 0, its
        first depth is -(vy + 1). This gives us the maximum vy
        because any higher value would overshoot by exceeding target's
        lower bound.
        """
        self.vymax = -self.target[2] - 1
        return self.vymax * (self.vymax + 1) // 2

    def part_two(self):
        """Brute force with reduced search space:
        - Minimum vx is the first value that stabilizes the probe
            further than target nearest bound.
        - Maximum vx is target further bound (vx + 1 overshoots at
            first step).
        - Minimum vy is target lower bound (vy - 1 overshoots at
            first step).
        - Maximum vy has been calculated in part_one.

        To see if the probe gets within the target area, its positions
        are checked until it gets further than xmax or deeper than
        ymin.
        """

        class Probe:
            def __init__(self, vx, vy):
                self.x = 0
                self.y = 0
                self.vx = vx
                self.vy = vy
                self.positions = {(self.x, self.y)}

            def step(self):
                self.x += self.vx
                self.y += self.vy
                self.vx = max(self.vx - 1, 0)
                self.vy -= 1
                self.positions.add((self.x, self.y))

        count = 0
        xmin, xmax, ymin, ymax = self.target
        target = set(product(range(xmin, xmax + 1), range(ymin, ymax + 1)))
        vxmin = next(vx for vx in range(xmin) if vx * (vx + 1) / 2 >= xmin)
        for vx in range(vxmin, xmax + 1):
            for vy in range(ymin, self.vymax + 1):
                probe = Probe(vx, vy)
                while probe.x <= xmax and probe.y >= ymin:
                    probe.step()
                if probe.positions.intersection(target):
                    count += 1
        return count


if __name__ == "__main__":
    Today().solve()
