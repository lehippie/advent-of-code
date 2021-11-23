"""Day 20: Infinite Elves and Infinite Houses."""

import numpy as np
from aoc.puzzle import Puzzle


class Puzzle20(Puzzle):
    def parser(self):
        return int(self.input)

    def part_one(self):
        target = self.input // 10
        presents = np.zeros(target, dtype=int)
        for elf in range(1, target):
            presents[elf::elf] += elf
        return np.argwhere(presents > target)[0][0]

    def part_two(self):
        target = self.input // 11
        presents = np.zeros(target, dtype=int)
        for elf in range(1, target):
            presents[elf : 50 * elf + 1 : elf] += elf
        return np.argwhere(presents > target)[0][0]


if __name__ == "__main__":
    Puzzle20(solutions=(831600, 884520)).solve()
