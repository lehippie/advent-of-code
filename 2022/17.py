"""Day 17: Pyroclastic Flow."""

from itertools import cycle
from aoc.puzzle import Puzzle

ROCKS = [
    [3 + 4j, 4 + 4j, 5 + 4j, 6 + 4j],  # horizontal line
    [4 + 4j, 3 + 5j, 4 + 5j, 5 + 5j, 4 + 6j],  # plus
    [3 + 4j, 4 + 4j, 5 + 4j, 5 + 5j, 5 + 6j],  # inverted L
    [3 + 4j, 3 + 5j, 3 + 6j, 3 + 7j],  # vertical line
    [3 + 4j, 4 + 4j, 3 + 5j, 4 + 5j],  # square
]
JET = {"<": -1, ">": 1}
WIDTH = {1, 2, 3, 4, 5, 6, 7}


class Today(Puzzle):
    def parser(self):
        self.jets = [JET[c] for c in self.input]

    def part_one(self, nrocks=2022):
        rocks = cycle(ROCKS)
        jets = cycle(self.jets)
        height = 0
        blocked = WIDTH.copy()
        while nrocks:
            rock = [r + height * 1j for r in next(rocks)]
            while True:
                jet = next(jets)
                new_rock = [r + jet for r in rock]
                if all(r.real in WIDTH and r not in blocked for r in new_rock):
                    rock = new_rock
                new_rock = [r - 1j for r in rock]
                if any(r in blocked for r in new_rock):
                    blocked.update(rock)
                    if (H := max(r.imag for r in rock)) > height:
                        height = H
                    break
                rock = new_rock
            nrocks -= 1
        return int(height)

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    Today().solve()
