"""Day 22: Reactor Reboot."""

import re
from collections import Counter
from itertools import product, takewhile
from math import prod
from aoc.puzzle import Puzzle


def intersection(cuboid1, cuboid2):
    inter = [
        min(c1, c2) if k % 2 else max(c1, c2)
        for k, (c1, c2) in enumerate(zip(cuboid1, cuboid2))
    ]
    if all(m <= M for m, M in zip(inter[::2], inter[1::2])):
        return tuple(inter)


def volume(cuboid):
    return prod((M - m + 1 for m, M in zip(cuboid[::2], cuboid[1::2])))


class Puzzle22(Puzzle):
    def parser(self):
        def parse_line(line):
            on, cuboid = line.split(" ")
            ranges = re.findall(r"-?\d+", cuboid)
            return on == "on", tuple(map(int, ranges))

        return [parse_line(l) for l in self.input]

    def part_one(self):
        on = set()
        for lit, cuboid in takewhile(lambda s: s[1][1] <= 50, self.input):
            xm, xM, ym, yM, zm, zM = cuboid
            coords = product(range(xm, xM + 1), range(ym, yM + 1), range(zm, zM + 1))
            if lit:
                on.update(coords)
            else:
                on.difference_update(coords)
        return len(on)

    def part_two(self):
        cuboids = Counter([self.input[0][1]])
        for action, span in self.input[1:]:
            for cuboid, flag in cuboids.copy().items():
                intersect = intersection(cuboid, span)
                if intersect is not None:
                    cuboids[intersect] += -flag
            if action:
                cuboids[span] += 1
            cuboids = Counter({c: f for c, f in cuboids.items() if f})
        return sum(flag * volume(c) for c, flag in cuboids.items())


if __name__ == "__main__":
    Puzzle22(solutions=(601104, 1262883317822267)).solve()
