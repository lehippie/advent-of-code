"""Day 14: Regolith Reservoir."""

from itertools import product
from aoc.puzzle import Puzzle


def rock_line(pt1, pt2):
    """Return set of points between <pt1> and <pt2>."""
    x1, x2 = sorted((pt1[0], pt2[0]))
    y1, y2 = sorted((pt1[1], pt2[1]))
    return [x + 1j * y for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]


class Today(Puzzle):
    def parser(self):
        self.rocks = set()
        for line in self.input:
            path = line.split(" -> ")
            path = [list(map(int, p.split(","))) for p in path]
            for pt1, pt2 in zip(path, path[1:]):
                self.rocks = self.rocks.union(rock_line(pt1, pt2))

    def part_one(self):
        resting = set()
        floor = max(r.imag for r in self.rocks)
        sand = 500 + 0j
        while sand.imag < floor:
            obstacles = {
                p: p in self.rocks or p in resting
                for p in (sand + 1j, sand - 1 + 1j, sand + 1 + 1j)
            }
            if all(obstacles.values()):
                resting.add(sand)
                sand = 500 + 0j
            else:
                sand = next(p for p, blocked in obstacles.items() if not blocked)
        return len(resting)

    def part_two(self):
        """Limit redondant calculations by keeping track of the
        complete sand path and by going back one step when a resting
        position is found.
        """
        resting = set()
        floor = 2 + max(r.imag for r in self.rocks)
        sand = [500 + 0j]
        while sand:
            obstacles = {
                p: p in self.rocks or p in resting or p.imag == floor
                for p in (sand[-1] + 1j, sand[-1] - 1 + 1j, sand[-1] + 1 + 1j)
            }
            if all(obstacles.values()):
                resting.add(sand.pop())
            else:
                sand.append(next(p for p, blocked in obstacles.items() if not blocked))
        return len(resting)


solutions = (1199, 23925)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
