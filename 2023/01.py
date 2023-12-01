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
        calibration_values = []
        for line in self.input:
            digits = re.findall(r"\d", line)
            calibration_values.append(int(digits[0] + digits[-1]))
        return sum(calibration_values)

    def part_two(self):
        calibration_values = []
        possible_digits = set(DIGITS).union(DIGITS.values())
        for line in self.input:
            first, last = None, None
            # First digit
            for idx in range(len(line)):
                for d in possible_digits:
                    if line[idx:].startswith(d):
                        first = DIGITS.get(d, d)
                        break
                if first is not None:
                    break
            # Last digit
            for idx in range(len(line), 0, -1):
                for d in possible_digits:
                    if line[:idx].endswith(d):
                        last = DIGITS.get(d, d)
                        break
                if last is not None:
                    break
            calibration_values.append(int(first + last))
        return sum(calibration_values)


solutions = (54390, 54277)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
