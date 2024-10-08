"""Day 12: Hill Climbing Algorithm."""

from collections import deque
from string import ascii_letters
from aoc.puzzle import Puzzle


class Hill:
    def __init__(self, heights, nrows, ncols):
        self.heights = heights
        self.nrows = nrows
        self.ncols = ncols

    def climbable_paths(self, pos):
        for adj in pos + 1, pos - 1, pos + 1j, pos - 1j:
            if (
                0 <= adj.real < self.nrows
                and 0 <= adj.imag < self.ncols
                and self.heights[adj] <= self.heights[pos] + 1
            ):
                yield adj


class Today(Puzzle):
    def parser(self):
        self.hill = Hill({}, len(self.input), len(self.input[0]))
        for r, row in enumerate(self.input):
            for c, height in enumerate(row):
                pos = r + 1j * c
                if height == "S":
                    self.start = pos
                    height = "a"
                elif height == "E":
                    self.goal = pos
                    height = "z"
                self.hill.heights[pos] = ascii_letters.index(height)

    def part_one(self, start=None):
        if start is None:
            start = [self.start]
        frontier = deque((s, 0) for s in start)
        reached = set(start)
        while frontier:
            position, steps = frontier.popleft()
            for destination in self.hill.climbable_paths(position):
                if destination == self.goal:
                    return steps + 1
                if destination not in reached:
                    reached.add(destination)
                    frontier.append((destination, steps + 1))

    def part_two(self):
        return self.part_one(
            [p for p, h in self.hill.heights.items() if h == ascii_letters.index("a")]
        )


if __name__ == "__main__":
    Today().solve()
