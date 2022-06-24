"""Day 18: Like a GIF For Your Yard."""

from itertools import product
from aoc.puzzle import Puzzle


class Grid:
    def __init__(self, initial_on, grid_size):
        self.on = initial_on
        self.size = grid_size

    def neighbors(self, position):
        for pos in product(*((p - 1, p, p + 1) for p in position)):
            if pos != position and all(0 <= p < self.size for p in pos):
                yield pos

    def step(self):
        """Lights that are on are checked first. While doing this,
        off neighbors are added to a queue to be checked afterwards.
        This limits the amount of verifications to make as off-lights
        surrounded only by other off-lights are skipped.
        """
        next_on = set()
        off_queue = set()
        for light in self.on:
            neighbors = set(self.neighbors(light))
            if len(neighbors.intersection(self.on)) in {2, 3}:
                next_on.add(light)
            off_queue.update(neighbors.difference(self.on))
        for light in off_queue:
            neighbors = set(self.neighbors(light))
            if len(neighbors.intersection(self.on)) == 3:
                next_on.add(light)
        self.on = next_on


class DefectiveGrid(Grid):
    """A defective grid has its corners stucked on, added
    to the set of on lights after each step.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stuck = set(product((0, self.size - 1), repeat=2))
        self.on.update(self.stuck)

    def step(self):
        super().step()
        self.on.update(self.stuck)


class Today(Puzzle):
    def parser(self):
        self.init_on = set(
            (r, c)
            for r, row in enumerate(self.input)
            for c, col in enumerate(row)
            if col == "#"
        )

    def part_one(self, steps=100, grid_class=Grid):
        grid = grid_class(self.init_on, len(self.input))
        for _ in range(steps):
            grid.step()
        return len(grid.on)

    def part_two(self, steps=100):
        return self.part_one(steps, DefectiveGrid)


solutions = (768, 781)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
