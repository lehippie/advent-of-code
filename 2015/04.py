"""Day 4: The Ideal Stocking Stuffer."""

from hashlib import md5

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self, n=1, z=5):
        while not md5(f"{self.input}{n}".encode()).hexdigest().startswith("0" * z):
            n += 1
        return n

    def part_two(self):
        return self.part_one(n=self.solution_one, z=6)


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        tests={"part_one": [("abcdef", 609043), ("pqrstuv", 1048970)]},
        solution_one=254575,
        solution_two=1038736,
    )

    if puzzle.test():
        puzzle.solve()
