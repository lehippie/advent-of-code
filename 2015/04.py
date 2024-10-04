"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, start=1, leading_zeroes=5):
        self.n = start
        head = "0" * leading_zeroes
        while not md5(f"{self.input}{self.n}".encode()).hexdigest().startswith(head):
            self.n += 1
        return self.n

    def part_two(self):
        return self.part_one(start=self.n, leading_zeroes=6)


if __name__ == "__main__":
    Today().solve()
