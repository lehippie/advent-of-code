"""Day 9: Smoke Basin."""

from itertools import product
from math import prod
from aoc.puzzle import Puzzle


class Floor:
    def __init__(self, heightmap):
        self.heightmap = heightmap
        self.nrows = len(heightmap)
        self.ncols = len(heightmap[0])

    def __getitem__(self, location):
        return self.heightmap[location[0]][location[1]]

    def adjacents(self, location):
        r, c = location
        for row, col in (r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c):
            if 0 <= row < self.nrows and 0 <= col < self.ncols:
                yield row, col


class Today(Puzzle):
    def parser(self):
        self.floor = Floor([list(map(int, line)) for line in self.input])

    def part_one(self):
        self.lows = set()
        risk = 0
        for location in product(range(self.floor.nrows), range(self.floor.ncols)):
            if all(
                self.floor[location] < self.floor[adjacent]
                for adjacent in self.floor.adjacents(location)
            ):
                self.lows.add(location)
                risk += 1 + self.floor[location]
        return risk

    def part_two(self):
        """Search from each low points to locations of height 9."""
        basin_sizes = []
        for low in self.lows:
            basin = {low}
            frontier = [low]
            while frontier:
                location = frontier.pop()
                for adjacent in self.floor.adjacents(location):
                    if adjacent not in basin and self.floor[adjacent] != 9:
                        basin.add(adjacent)
                        frontier.append(adjacent)
            basin_sizes.append(len(basin))
        return prod(sorted(basin_sizes)[-3:])


solutions = (468, 1280496)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
