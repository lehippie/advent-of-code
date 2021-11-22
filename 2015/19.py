"""Day 19: Medicine for Rudolph."""

import re
from aoc.puzzle import Puzzle


class Puzzle19(Puzzle):
    def parser(self):
        self.reactions = []
        for line in self.input:
            if "=>" in line:
                old, new = line.split(" => ")
                self.reactions.append((old, new))
            elif line:
                self.medicine = line

    def part_one(self):
        calibration = set()
        for old, new in self.reactions:
            for m in re.finditer(old, self.medicine):
                calibration.add(
                    self.medicine[: m.start()] + new + self.medicine[m.end() :]
                )
        return len(calibration)

    def part_two(self):
        molecule = self.medicine
        n = 0
        while molecule != "e":
            for old, new in self.reactions:
                if old == "e" and new != molecule:
                    continue
                if new in molecule:
                    molecule = molecule.replace(new, old, 1)
                    n = n + 1
        return n


if __name__ == "__main__":
    Puzzle19(solutions=(518, 200)).solve()
