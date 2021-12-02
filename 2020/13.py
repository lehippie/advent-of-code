"""Day 13: Shuttle Search."""

from math import prod
from aoc.puzzle import Puzzle


class Puzzle13(Puzzle):
    def parser(self):
        start = int(self.input[0])
        buses = [int(b) if b != "x" else None for b in self.input[1].split(",")]
        return start, buses

    def part_one(self):
        start, buses = self.input
        ts = {}
        for bus in buses:
            if bus is None:
                continue
            ts[bus] = next(t for t in range(start, start + bus + 1) if t % bus == 0)
        earliest = min(ts, key=ts.get)
        return earliest * (ts[earliest] - start)

    def part_two(self):
        buses = [[b, k] for k, b in enumerate(self.input[1]) if b is not None]
        buses = sorted(buses, key=lambda x: x[0], reverse=True)
        cycle = buses[0][0]
        ts = buses[0][0] - buses[0][1]
        for k in range(2, len(buses) + 1):
            road = buses[:k]
            while not all((ts + k) % b == 0 for b, k in road):
                ts += cycle
            cycle = prod(b[0] for b in road)
        return ts


if __name__ == "__main__":
    Puzzle13(solutions=(3789, 667437230788118)).solve()
