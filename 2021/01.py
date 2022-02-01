"""Day 1: Sonar Sweep."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.depths = list(map(int, self.input))

    def part_one(self, n=1):
        return sum(x < y for x, y in zip(self.depths, self.depths[n:]))

    def part_two(self):
        return self.part_one(3)


solutions = (1448, 1471)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
