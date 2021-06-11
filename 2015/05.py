"""Day 5: Doesn't He Have Intern-Elves For This?"""

import re

from aoc.puzzle import Puzzle


def is_nice(string, forbidden=("ab", "cd", "pq", "xy")):
    if len(re.findall(r"[aeiou]", string)) < 3:
        return False
    if not re.search(r"(.)\1", string):
        return False
    if any(f in string for f in forbidden):
        return False
    return True


def is_better(string):
    if not re.search(r"(..).*\1", string):
        return False
    if not re.search(r"(.).\1", string):
        return False
    return True


class TodayPuzzle(Puzzle):
    def part_one(self):
        return sum(is_nice(s) for s in self.input)

    def part_two(self):
        return sum(is_better(s) for s in self.input)


if __name__ == "__main__":
    TodayPuzzle(solutions=(255, 55)).solve()
