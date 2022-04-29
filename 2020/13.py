"""Day 13: Shuttle Search."""

from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.start = int(self.input[0])
        self.buses = [int(b) if b != "x" else None for b in self.input[1].split(",")]

    def part_one(self):
        ts = {}
        for bus in self.buses:
            if bus is None:
                continue
            ts[bus] = next(
                t for t in range(self.start, self.start + bus + 1) if t % bus == 0
            )
        earliest = min(ts, key=ts.get)
        return earliest * (ts[earliest] - self.start)

    def part_two(self):
        buses = [[b, k] for k, b in enumerate(self.buses) if b is not None]
        buses = sorted(buses, key=lambda x: x[0], reverse=True)
        cycle = buses[0][0]
        ts = buses[0][0] - buses[0][1]
        for k in range(2, len(buses) + 1):
            road = buses[:k]
            while not all((ts + k) % b == 0 for b, k in road):
                ts += cycle
            cycle = prod(b[0] for b in road)
        return ts


solutions = (3789, 667437230788118)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
