"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, start=1, leading_zeroes=5):
        n = start
        head = "0" * leading_zeroes
        while not md5(f"{self.input}{n}".encode()).hexdigest().startswith(head):
            n += 1
        return n

    def part_two(self):
        return self.part_one(start=self.solutions[0], leading_zeroes=6)


solutions = (254575, 1038736)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
