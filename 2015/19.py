"""Day 19: Medicine for Rudolph."""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.reactions = []
        for line in self.input:
            if "=>" in line:
                old, new = line.split(" => ")
                self.reactions.append((old, new))
            elif line:
                self.molecule = line

    def part_one(self):
        products = set()
        for old, new in self.reactions:
            for m in re.finditer(old, self.molecule):
                products.add(
                    self.molecule[: m.start()] + new + self.molecule[m.end() :]
                )
        return len(products)

    def part_two(self):
        """Run known reactions backward until getting a single electron."""
        molecule = self.molecule
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
    Today().solve()
