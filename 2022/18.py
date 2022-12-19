"""Day 18: Boiling Boulders."""

from itertools import product
from aoc.puzzle import Puzzle


def around(cube: tuple):
    x, y, z = cube
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


def area(cubes: set):
    return sum(6 - len(cubes.intersection(around(c))) for c in cubes)


class Today(Puzzle):
    def parser(self):
        self.droplet = set(tuple(map(int, line.split(","))) for line in self.input)

    def part_one(self):
        return area(self.droplet)

    def part_two(self):
        """Holes inside the droplet are cubes that are nor outside,
        nor part of it. The exterior is found using pathfinding from
        the corner of a megacube surrounding the whole droplet.
        """
        span = [list(map(min, zip(*self.droplet))), list(map(max, zip(*self.droplet)))]
        span[0] = [mini - 1 for mini in span[0]]
        span[1] = [maxi + 2 for maxi in span[1]]
        megacube = set(c for c in product(*(range(m, M) for m, M in zip(*span))))
        frontier = [tuple(span[0])]
        exterior = {tuple(span[0])}
        while frontier:
            cube = frontier.pop()
            for c in around(cube):
                if c in megacube and c not in self.droplet and c not in exterior:
                    exterior.add(c)
                    frontier.append(c)
        holes = megacube.difference(exterior).difference(self.droplet)
        return self.solutions[0] - area(holes)


solutions = (4320, 2456)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
