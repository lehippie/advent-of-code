"""Day 4: Secure Container."""

import re
from aoc.puzzle import Puzzle

GROUPS = re.compile(r"((\d)\2+)")


def valid(password: str):
    if len(password) == 6 and "".join(sorted(password)) == password:
        for a, b in zip(password, password[1:]):
            if a == b:
                return True
    return False


def completely_valid(password: str):
    if len(password) == 6 and "".join(sorted(password)) == password:
        if any(len(g[0]) == 2 for g in GROUPS.findall(password)):
            return True
    return False


class Today(Puzzle):
    def parser(self):
        self.m, self.M = map(int, self.input.split("-"))

    def part_one(self):
        return sum(valid(str(pw)) for pw in range(self.m, self.M + 1))

    def part_two(self):
        return sum(completely_valid(str(pw)) for pw in range(self.m, self.M + 1))


solutions = (1729, 1172)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
