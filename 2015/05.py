"""Day 5: Doesn't He Have Intern-Elves For This?"""

import re
from aoc.puzzle import Puzzle


VOWELS = re.compile(r"[aeiou]")
DOUBLES = re.compile(r"(.)\1")
DOUBLE_PAIRS = re.compile(r"(..).*\1")
ALTERNATED = re.compile(r"(.).\1")


def is_nice(string, forbidden=("ab", "cd", "pq", "xy")):
    if len(VOWELS.findall(string)) < 3:
        return False
    if not DOUBLES.search(string):
        return False
    if any(f in string for f in forbidden):
        return False
    return True


def is_better(string):
    if not DOUBLE_PAIRS.search(string):
        return False
    if not ALTERNATED.search(string):
        return False
    return True


class Today(Puzzle):
    def part_one(self):
        return sum(is_nice(s) for s in self.input)

    def part_two(self):
        return sum(is_better(s) for s in self.input)


solutions = (255, 55)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
