"""--- Day 13: Claw Contraption ---"""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.machines = [
            list(map(int, re.findall(r"\d+", machine)))
            for machine in "\n".join(self.input).split("\n\n")
        ]

    def part_one(self):
        """We need to solve the system of two equations:
            | m * Ax + n * Bx = Px
            | m * Ay + n * By = Py
        If the results are not integers, the prize cannot be won.

        After verification, there is no machine where the system's
        determinant is zero in the input. No need to handle this.
        """
        tokens = 0
        for Ax, Ay, Bx, By, Px, Py in self.machines:
            m = (Bx * Py - By * Px) / (Bx * Ay - By * Ax)
            n = (Px - m * Ax) / Bx
            if (M := int(m)) == m and (N := int(n)) == n:
                tokens += 3 * M + N
        return tokens

    def part_two(self):
        tokens = 0
        for Ax, Ay, Bx, By, Px, Py in self.machines:
            Px += 10000000000000
            Py += 10000000000000
            m = (Bx * Py - By * Px) / (Bx * Ay - By * Ax)
            n = (Px - m * Ax) / Bx
            if (M := int(m)) == m and (N := int(n)) == n:
                tokens += 3 * M + N
        return tokens


if __name__ == "__main__":
    Today().solve()
