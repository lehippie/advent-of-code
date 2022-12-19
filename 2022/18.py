"""Day 18: Boiling Boulders."""

from itertools import product
from aoc.puzzle import Puzzle


def adjacent(cube: tuple):
    x, y, z = cube
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def area(cubes: set):
    return sum(6 - len(cubes.intersection(adjacent(c))) for c in cubes)


class Today(Puzzle):
    def parser(self):
        self.droplet = set(tuple(map(int, line.split(","))) for line in self.input)

    def part_one(self):
        return area(self.droplet)

    def part_two(self):
        """Holes are cubes that are nor outside nor part of the
        droplet. Outside cubes are found using pathfinding from the
        corner of a volume surrounding the droplet.
        """
        span = [(min(d) - 1, max(d) + 2) for d in zip(*self.droplet)]
        volume = set(c for c in product(*(range(m, M) for m, M in span)))
        corner = tuple(m for m, _ in span)
        outside = {corner}
        frontier = [corner]
        while frontier:
            for cube in adjacent(frontier.pop()):
                if cube in volume and cube not in self.droplet and cube not in outside:
                    outside.add(cube)
                    frontier.append(cube)
        holes = volume.difference(outside).difference(self.droplet)
        return self.solutions[0] - area(holes)


solutions = (4320, 2456)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
