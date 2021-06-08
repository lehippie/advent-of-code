"""Day 5: Doesn't He Have Intern-Elves For This?"""

import re
from collections import Counter

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
        return Counter(is_nice(s) for s in self.input)[True]

    def part_two(self):
        return Counter(is_better(s) for s in self.input)[True]


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        tests={
            "part_one": [
                (["ugknbfddgicrmopn"], 1),
                (["aaa"], 1),
                (["jchzalrnumimnmhp"], 0),
                (["haegwjzuvuyypxyu"], 0),
                (["dvszwmarrgswjxmb"], 0),
            ],
            "part_two": [
                (["qjhvhtzxzqqjkmpb"], 1),
                (["xxyxx"], 1),
                (["uurcxstgmygtbstg"], 0),
                (["ieodomkazucvgmuy"], 0),
            ],
        },
        solution_one=255,
        solution_two=55,
    )
    if puzzle.test():
        puzzle.solve()
