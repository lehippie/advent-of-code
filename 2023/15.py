"""--- Day 15: Lens Library ---"""

from collections import defaultdict
from aoc.puzzle import Puzzle


def hashing(string):
    value = 0
    for s in string:
        value = ((value + ord(s)) * 17) % 256
    return value


class Today(Puzzle):
    def parser(self):
        self.sequence = self.input.split(",")

    def part_one(self):
        return sum(hashing(step) for step in self.sequence)

    def part_two(self):
        boxes = defaultdict(dict)
        for step in self.sequence:
            if step[-1] == "-":
                label = step[:-1]
                boxes.get(hashing(label), {}).pop(label, None)
            else:
                label, focal = step.split("=")
                boxes[hashing(label)][label] = int(focal)
        return sum(
            (b + 1) * slot * focal
            for b, lenses in boxes.items()
            for slot, focal in enumerate(lenses.values(), 1)
        )


solutions = (505459, 228508)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
