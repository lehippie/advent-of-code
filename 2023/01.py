"""--- Day 1: Trebuchet?! ---"""

import re
from aoc.puzzle import Puzzle


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class Today(Puzzle):
    def part_one(self):
        """Create a list of all digits and use the first and last to
        get the calibration value.
        """
        calibration = 0
        for line in self.input:
            digits = re.findall(r"\d", line)
            calibration += int(digits[0] + digits[-1])
        return calibration

    def part_two(self):
        """Each line is checked character by character from both ends
        until we find both first and last digits.
        """
        calibration = 0
        possible_digits = set(DIGITS).union(DIGITS.values())
        for line in self.input:
            first, last = None, None
            for idx in range(len(line)):
                for d in possible_digits:
                    if not first and line[idx:].startswith(d):
                        first = DIGITS.get(d, d)
                    if not last and line[: len(line) - idx].endswith(d):
                        last = DIGITS.get(d, d)
                if first and last:
                    break
            calibration += int(first + last)
        return calibration


if __name__ == "__main__":
    Today().solve()
