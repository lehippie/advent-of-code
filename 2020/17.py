"""Day 17: Conway Cubes."""

from itertools import product
from aoc.puzzle import Puzzle


class Grid:
    def __init__(self, initial_grid):
        self.active = initial_grid

    @staticmethod
    def neighbors(position):
        positions_around = set(product(*((p, p - 1, p + 1) for p in position)))
        positions_around.remove(position)
        return positions_around

    def run_one_cycle(self):
        next_active_cubes = set()
        inactive_cubes_to_check = set()
        for cube in self.active:
            neighbors = self.neighbors(cube)
            if len(neighbors.intersection(self.active)) in {2, 3}:
                next_active_cubes.add(cube)
            inactive_cubes_to_check.update(neighbors.difference(self.active))
        for cube in inactive_cubes_to_check:
            if len(self.neighbors(cube).intersection(self.active)) == 3:
                next_active_cubes.add(cube)
        self.active = next_active_cubes

    def boot(self, cycles=6):
        for _ in range(cycles):
            self.run_one_cycle()


class Puzzle17(Puzzle):
    def parser(self):
        data = set()
        for x, line in enumerate(self.input):
            ys = [i for i, c in enumerate(line) if c == "#"]
            data.update((x, y, 0) for y in ys)
        return data

    def part_one(self):
        grid = Grid(self.input)
        grid.boot()
        return len(grid.active)

    def part_two(self):
        grid4D = {(x, y, z, 0) for x, y, z in self.input}
        grid = Grid(grid4D)
        grid.boot()
        return len(grid.active)


if __name__ == "__main__":
    Puzzle17(solutions=(386, 2276)).solve()
