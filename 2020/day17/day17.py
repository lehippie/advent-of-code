"""Day 17: Conway Cubes."""

from itertools import product
from pathlib import Path


INPUT_FILE = "grid_init.txt"

def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    data = set()
    with filepath.open() as f:
        for x, line in enumerate(f):
            ys = [i for i, c in enumerate(line.rstrip()) if c == "#"]
            data.update((x, y, 0) for y in ys)
    return data


# --- Part One ---

class Grid:
    def __init__(self, initial_grid):
        self.active = initial_grid

    @staticmethod
    def neighbors(position):
        positions_around = set(product(*((p, p-1, p+1) for p in position)))
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


def part_one(initial_grid):
    grid = Grid(initial_grid)
    grid.boot()
    return len(grid.active)


# --- Part Two ---

def part_two(initial_grid):
    grid4D = {(x, y, z, 0) for x, y, z in initial_grid}
    grid = Grid(grid4D)
    grid.boot()
    return len(grid.active)


# --- Tests & Run ---

def tests():
    # Part One
    test = load_input("test.txt")
    assert part_one(test) == 112
    # Part Two
    assert part_two(test) == 848


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    result_one = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 386

    result_two = part_two(puzzle_input)
    print(f"Part Two answer: {result_two}")
    assert result_two == 2276
