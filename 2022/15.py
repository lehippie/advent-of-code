"""Day 15: Beacon Exclusion Zone."""

import re
from aoc.puzzle import Puzzle


def scanned_ranges(sensors, y):
    """Return contiguous scanned ranges in row <y> by listing
    ranges of each scanner and removing intersections.
    """
    ranges = [
        [sx - radius + dy, sx + radius - dy]
        for (sx, sy), radius in sensors.items()
        if (dy := abs(y - sy)) <= radius
    ]
    ranges.sort()
    unions = [ranges.pop(0)]
    for start, stop in ranges:
        if start <= unions[-1][1]:
            unions[-1][1] = max(stop, unions[-1][1])
        else:
            unions.append([start, stop])
    return unions


class Today(Puzzle):
    def parser(self):
        self.sensors = {}
        self.beacons = set()
        for line in self.input:
            sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
            self.sensors[(sx, sy)] = abs(sx - bx) + abs(sy - by)
            self.beacons.add((bx, by))

    def part_one(self, y=2000000):
        scan = scanned_ranges(self.sensors, y)
        n_beacons = sum(by == y for _, by in self.beacons)
        return sum(M - m + 1 for m, M in scan) - n_beacons

    def part_two(self, ymax=4000000):
        for y in range(ymax, -1, -1):
            if len(s := scanned_ranges(self.sensors, y)) == 2:
                return 4000000 * (s[0][1] + 1) + y


solutions = (5403290, 10291582906626)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
