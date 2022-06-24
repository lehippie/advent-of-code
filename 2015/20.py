"""Day 20: Infinite Elves and Infinite Houses."""

import numpy as np
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.target = int(self.input)

    def part_one(self):
        """It is sure that the house which number is our target
        amount of presents divided by 10 will have enough presents.
        We only have to check all houses up to it.
        """
        presents = np.zeros(self.target // 10, dtype=int)
        for elf in range(1, self.target // 10):
            presents[elf::elf] += 10 * elf
        return np.where(presents >= self.target)[0][0]

    def part_two(self):
        """Same as before but with the number divided by 11."""
        presents = np.zeros(self.target // 11, dtype=int)
        for elf in range(1, self.target // 11):
            presents[elf : 50 * elf + 1 : elf] += 11 * elf
        return np.where(presents > self.target)[0][0]


solutions = (831600, 884520)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
