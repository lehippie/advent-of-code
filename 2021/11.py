"""Day 11: Dumbo Octopus."""

from itertools import product
import numpy as np
from aoc.puzzle import Puzzle


class Octopuses:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.flash_count = 0

    def neighbors(self, position):
        return set(
            (x, y)
            for x, y in product(*((p, p - 1, p + 1) for p in position))
            if (x, y) != position
            and 0 <= x < self.grid.shape[0]
            and 0 <= y < self.grid.shape[1]
        )

    def do_step(self):
        self.grid += 1
        flashes = set(((x, y) for x, y in np.argwhere(self.grid == 10)))
        while flashes:
            fx, fy = flashes.pop()
            self.flash_count += 1
            for x, y in self.neighbors((fx, fy)):
                self.grid[x, y] += 1
                if self.grid[x, y] == 10:
                    flashes.add((x, y))
        self.grid[self.grid > 9] = 0


class Today(Puzzle):
    def parser(self):
        self.grid = [list(map(int, line)) for line in self.input]

    def part_one(self, steps=100):
        dumbos = Octopuses(self.grid)
        for _ in range(steps):
            dumbos.do_step()
        return dumbos.flash_count

    def part_two(self):
        dumbos = Octopuses(self.grid)
        sync_step = 0
        while dumbos.grid.any():
            sync_step += 1
            dumbos.do_step()
        return sync_step


solutions = (1665, 235)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
