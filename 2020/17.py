"""Day 17: Conway Cubes."""

from itertools import product
from aoc.puzzle import Puzzle


class PocketDimension:
    def __init__(self, init_active):
        self.active = init_active

    @staticmethod
    def neighbors(position):
        for pos in product(*((p - 1, p, p + 1) for p in position)):
            if pos != position:
                yield pos

    def run_one_cycle(self):
        """Active cubes are checked first while their inactive
        neighbors are added to a queue to be checked afterwards.
        This limits the amount of verifications to make as inactive
        cubes without active ones around them don't switch.
        """
        next_active = set()
        inactive_queue = set()
        for cube in self.active:
            neighbors = set(self.neighbors(cube))
            if len(self.active.intersection(neighbors)) in {2, 3}:
                next_active.add(cube)
            inactive_queue.update(neighbors.difference(self.active))
        for cube in inactive_queue:
            if len(self.active.intersection(self.neighbors(cube))) == 3:
                next_active.add(cube)
        self.active = next_active

    def boot(self, cycles=6):
        for _ in range(cycles):
            self.run_one_cycle()
        return len(self.active)


class Today(Puzzle):
    def parser(self):
        self.init_active = set()
        for x, line in enumerate(self.input):
            ys = [i for i, c in enumerate(line) if c == "#"]
            self.init_active.update((x, y, 0) for y in ys)

    def part_one(self):
        return PocketDimension(self.init_active).boot()

    def part_two(self):
        init_4D = {(x, y, z, 0) for x, y, z in self.init_active}
        return PocketDimension(init_4D).boot()


if __name__ == "__main__":
    Today().solve()
