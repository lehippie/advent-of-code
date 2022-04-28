"""Day 16: Aunt Sue."""

import re
from aoc.puzzle import Puzzle


THE_SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Today(Puzzle):
    def parser(self):
        def parse(line):
            name, things = line.split(":", maxsplit=1)
            sue = {"number": int(re.findall(r"\d+", name)[0])}
            sue.update({k: int(v) for k, v in re.findall(r"(\w+): (\d+)", things)})
            return sue

        self.sues = [parse(line) for line in self.input]

    def part_one(self):
        for sue in self.sues:
            if all(sue[k] == THE_SUE[k] for k in sue if k != "number"):
                return sue["number"]

    def part_two(self):
        greater = {"cats", "trees"}
        fewer = {"pomeranians", "goldfish"}
        equals = set(THE_SUE).difference(greater.union(fewer))
        for sue in self.sues:
            if (
                all(sue[k] == THE_SUE[k] for k in equals.intersection(sue))
                and all(sue[k] > THE_SUE[k] for k in greater.intersection(sue))
                and all(sue[k] < THE_SUE[k] for k in fewer.intersection(sue))
            ):
                return sue["number"]


solutions = (373, 260)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
