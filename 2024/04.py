"""--- Day 4: Ceres Search ---"""

from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)
DIAGONALS = (1 + 1j, 1 - 1j)


class Today(Puzzle):
    def parser(self):
        self.letters = {"X": set(), "M": set(), "A": set(), "S": set()}
        for r, row in enumerate(self.input):
            for c, letter in enumerate(row):
                self.letters[letter].add(r + c * 1j)

    def part_one(self):
        return sum(
            x + d in self.letters["M"]
            and x + 2 * d in self.letters["A"]
            and x + 3 * d in self.letters["S"]
            for d in DIRECTIONS
            for x in self.letters["X"]
        )

    def part_two(self):
        return sum(
            all(
                (x + d in self.letters["M"] and x - d in self.letters["S"])
                or (x + d in self.letters["S"] and x - d in self.letters["M"])
                for d in DIAGONALS
            )
            for x in self.letters["A"]
        )


if __name__ == "__main__":
    Today().solve()
