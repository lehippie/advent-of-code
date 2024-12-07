"""--- Day 7: Bridge Repair ---"""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.equations = [tuple(map(int, re.findall(r"\d+", l))) for l in self.input]

    def part_one(self):
        self.calibration = 0
        self.incorrects = []
        for value, n1, *numbers in self.equations:
            results = {n1}
            for n in numbers:
                next_results = {r + n for r in results}
                next_results.update(r * n for r in results)
                results = next_results
            if value in results:
                self.calibration += value
            else:
                self.incorrects.append((value, n1, *numbers))
        return self.calibration

    def part_two(self):
        calibration = 0
        for value, n1, *numbers in self.incorrects:
            results = {n1}
            for n in numbers:
                next_results = {r + n for r in results}
                next_results.update(r * n for r in results)
                next_results.update(int(f"{r}{n}") for r in results)
                results = {r for r in next_results if r <= value}
            if value in results:
                calibration += value
        return self.calibration + calibration


if __name__ == "__main__":
    Today().solve()
