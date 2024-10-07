"""Day 11: Dumbo Octopus."""

from itertools import product
import numpy as np
from aoc.puzzle import Puzzle


class Octopuses:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.flash_count = 0

    def neighbors(self, position):
        for x, y in product(*((p - 1, p, p + 1) for p in position)):
            if (
                (x, y) != position
                and 0 <= x < self.grid.shape[0]
                and 0 <= y < self.grid.shape[1]
            ):
                yield x, y

    def step(self):
        """BFS applied to flashing octopuses. Only add position to
        flashing group if the energy is 10 after the +1 increase.
        A higher value means it has already flashed during this step.
        """
        self.grid += 1
        flashes = set(map(tuple, np.argwhere(self.grid == 10)))
        while flashes:
            position = flashes.pop()
            self.flash_count += 1
            for neighbor in self.neighbors(position):
                self.grid[neighbor] += 1
                if self.grid[neighbor] == 10:
                    flashes.add(neighbor)
        self.grid[self.grid > 9] = 0


class Today(Puzzle):
    def parser(self):
        self.grid = [list(map(int, line)) for line in self.input]

    def part_one(self, steps=100):
        dumbos = Octopuses(self.grid)
        for _ in range(steps):
            dumbos.step()
        return dumbos.flash_count

    def part_two(self):
        dumbos = Octopuses(self.grid)
        sync_step = 0
        while dumbos.grid.any():
            dumbos.step()
            sync_step += 1
        return sync_step


if __name__ == "__main__":
    Today().solve()
