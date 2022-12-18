"""Day 18: Boiling Boulders."""

from aoc.puzzle import Puzzle


def around(cube):
    x, y, z = cube
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)


class Today(Puzzle):
    def parser(self):
        self.cubes = set(tuple(map(int, line.split(","))) for line in self.input)

    def part_one(self):
        return sum(
            6 - len(self.cubes.intersection(around(cube)))
            for cube in self.cubes
        )

    def part_two(self):
        return super().part_two()


solutions = (4320, None)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
