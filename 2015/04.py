"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, z=5):
        n = 1
        while not md5(f"{self.input}{n}".encode()).hexdigest().startswith("0" * z):
            n += 1
        return n

    def part_two(self):
        return self.part_one(6)


solutions = (254575, 1038736)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
