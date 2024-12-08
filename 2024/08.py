"""--- Day 8: Resonant Collinearity ---"""

from collections import defaultdict
from itertools import combinations, count, takewhile
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.area = set()
        self.antennas = defaultdict(set)
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                position = r + c * 1j
                self.area.add(position)
                if cell != ".":
                    self.antennas[cell].add(position)

    def part_one(self):
        antinodes = set()
        for _, antennas in self.antennas.items():
            for a, b in combinations(antennas, r=2):
                positions = (2 * b - a, 2 * a - b)
                antinodes.update(p for p in positions if p in self.area)
        return len(antinodes)

    def part_two(self):
        antinodes = set()
        is_in = lambda position: position in self.area
        for _, antennas in self.antennas.items():
            for a, b in combinations(antennas, r=2):
                delta = b - a
                antinodes.update(takewhile(is_in, (b + i * delta for i in count())))
                antinodes.update(takewhile(is_in, (a - i * delta for i in count())))
        return len(antinodes)


if __name__ == "__main__":
    Today().solve()
