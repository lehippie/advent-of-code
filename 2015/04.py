"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self, n=1, z=5):
        while not md5(f"{self.input}{n}".encode()).hexdigest().startswith("0" * z):
            n += 1
        return n

    def part_two(self):
        return self.part_one(n=self.solutions[0], z=6)


if __name__ == "__main__":
    TodayPuzzle(solutions=(254575, 1038736)).solve()
