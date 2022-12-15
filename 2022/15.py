"""Day 15: Beacon Exclusion Zone."""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.sensors = {}
        self.beacons = set()
        for line in self.input:
            sx, sy, bx, by = map(int, re.findall(r"-?\d+", line))
            self.sensors[(sx, sy)] = abs(sx - bx) + abs(sy - by)
            self.beacons.add((bx, by))

    def scanned_ranges(self, y):
        """Return contiguous scanned positions in row <y>."""
        # List scanners' ranges
        ranges = []
        for (sx, sy), radius in self.sensors.items():
            if (dy := abs(y - sy)) <= radius:
                xmin, xmax = sx - radius + dy, sx + radius - dy
                ranges.append([xmin, xmax])
        # Remove intersections
        unions = []
        for start, stop in sorted(ranges):
            if not unions:
                unions.append([start, stop])
                continue
            ustart, ustop = unions[-1]
            if start <= ustop and ustart <= stop:
                unions[-1] = [min(start, ustart), max(stop, ustop)]
            else:
                unions.append([start, stop])
        return unions

    def part_one(self, y=2000000):
        scanned = self.scanned_ranges(y)
        n_beacons = sum(by == y for _, by in self.beacons)
        return sum(M - m + 1 for m, M in scanned) - n_beacons

    def part_two(self, ymax=4000000):
        for y in range(ymax, -1, -1):
            if len(s := self.scanned_ranges(y)) == 2:
                return 4000000 * (s[0][1] + 1) + y


solutions = (5403290, 10291582906626)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
