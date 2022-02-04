"""Day 1: Sonar Sweep."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.depths = list(map(int, self.input))

    def part_one(self, n=1):
        return sum(x < y for x, y in zip(self.depths, self.depths[n:]))

    def part_two(self):
        """We must calculate (A1 + A2 + A3) - (B1 + B2 + B3). As
        B1 = A2 and B2 = A3, it reduces to A1 - B3. Thus, we only
        need to compare a depth with the value 3 steps after.
        """
        return self.part_one(3)


solutions = (1448, 1471)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
