"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Puzzle04(Puzzle):
    def part_one(self, z=5):
        n = 1
        while not md5(f"{self.input}{n}".encode()).hexdigest().startswith("0" * z):
            n += 1
        return n

    def part_two(self):
        return self.part_one(6)


if __name__ == "__main__":
    Puzzle04(solutions=(254575, 1038736)).solve()
