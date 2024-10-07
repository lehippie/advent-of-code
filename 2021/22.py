"""Day 22: Reactor Reboot."""

import re
from collections import Counter
from itertools import product, takewhile
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        def parse_line(line):
            on, cuboid = line.split(" ")
            ranges = re.findall(r"-?\d+", cuboid)
            return on == "on", tuple(map(int, ranges))

        self.steps = [parse_line(l) for l in self.input]

    def part_one(self):
        """Lighted cubes are stored in a set. Cubes coordinates are
        generated from cuboids' ranges to be added or removed from
        the set.
        """
        on = set()
        for lit, cuboid in takewhile(lambda s: s[1][1] <= 50, self.steps):
            xm, xM, ym, yM, zm, zM = cuboid
            coords = product(range(xm, xM + 1), range(ym, yM + 1), range(zm, zM + 1))
            if lit:
                on.update(coords)
            else:
                on.difference_update(coords)
        return len(on)

    def part_two(self):
        """Obviously, the first method doesn't work for the full
        input. Here, cuboids are kept in a dict where the keys are
        tuples of their spans, and the values are their status flag.

        When a new cuboid is considered, to the flags of intersecting
        cuboids, we add their opposite. Then if the new cuboid
        is turned on, we add 1 to its own flag. Finally, cuboids with
        flag 0 are removed (happening when a cuboid is included in
        another one).

        Here are the different cases and the result:
        - on overlaping +1: intersection isn't counted twice.
        - off overlaping +1: intersection is compensated.
        - anything overlaping -1: cancel previous compensation.
        """

        def intersection(cuboid1, cuboid2):
            span = [
                min(c1, c2) if k % 2 else max(c1, c2)
                for k, (c1, c2) in enumerate(zip(cuboid1, cuboid2))
            ]
            if all(m <= M for m, M in zip(span[::2], span[1::2])):
                return tuple(span)

        cuboids = Counter([self.steps[0][1]])
        for action, span in self.steps[1:]:
            for cuboid, flag in cuboids.copy().items():
                intersect = intersection(cuboid, span)
                if intersect is not None:
                    cuboids[intersect] += -flag
            if action:
                cuboids[span] += 1
            cuboids = Counter({c: f for c, f in cuboids.items() if f})

        def volume(cuboid):
            return prod((M - m + 1 for m, M in zip(cuboid[::2], cuboid[1::2])))

        return sum(flag * volume(c) for c, flag in cuboids.items())


if __name__ == "__main__":
    Today().solve()
