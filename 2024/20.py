"""--- Day 20: Race Condition ---"""

from itertools import product
from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j)


class Today(Puzzle):
    def parser(self):
        self.track = set()
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                if cell != "#":
                    self.track.add(r + c * 1j)
                    if cell == "S":
                        self.start = r + c * 1j
                    elif cell == "E":
                        self.end = r + c * 1j

    def part_one(self):
        """For each point along the track, positions at distance 2
        are checked for a cheat better than 100 ps.
        """
        self.pico = {self.start: 0}
        position = self.start
        while position != self.end:
            for direction in DIRECTIONS:
                step = position + direction
                if step in self.track and step not in self.pico:
                    self.pico[step] = self.pico[position] + 1
                    break
            position = step

        cheats_count = 0
        for position, ps in self.pico.items():
            for direction in DIRECTIONS:
                cheat = position + 2 * direction
                if cheat in self.track and self.pico[cheat] - ps >= 102:
                    cheats_count += 1
        return cheats_count

    def part_two(self):
        """Same logic as part one but for each position, we check
        points on track within a Manhattan distance between 2 and 20
        picoseconds.
        """
        area = set(
            r + c * 1j
            for r, c in product(range(-20, 21), repeat=2)
            if 2 <= abs(r) + abs(c) <= 20
        )

        def manhattan(a: complex, b: complex = 0):
            return abs(a.real - b.real) + abs(a.imag - b.imag)

        cheats_count = 0
        for position, ps in self.pico.items():
            for cheat in self.track.intersection(position + a for a in area):
                if self.pico[cheat] - ps >= 100 + manhattan(position, cheat):
                    cheats_count += 1
        return cheats_count


if __name__ == "__main__":
    Today().solve()
