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

    def active_neighbors(self, position):
        arounds = set(product(*((p, p-1, p+1) for p in position)))
        arounds.remove(position)
        return len(arounds.intersection(self.active))

    def run_one_cycle(self):
        coords = (set(range(min(p)-1, max(p)+2)) for p in zip(*self.active))
        self.active = {
            c for c in product(*coords)
            if ((c in self.active and self.active_neighbors(c) in {2, 3})
             or (c not in self.active and self.active_neighbors(c) == 3))
        }

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
