"""--- Day 18: RAM Run ---"""

from collections import deque
from itertools import product
from aoc.puzzle import Puzzle

DIRECTIONS = {1, -1, 1j, -1j}


class Today(Puzzle):
    def parser(self):
        self.bytes = [complex(*map(int, line.split(","))) for line in self.input]
        self.space = {x + y * 1j for x, y in product(range(71), repeat=2)}
        self.start = 0
        self.exit = 70 + 70 * 1j

    def part_one(self, corruption=1024):
        corrupted = set(self.bytes[: corruption + 1])
        reached = {self.start}
        frontier = deque([(self.start, 0)])
        while frontier:
            position, step = frontier.popleft()
            if position == self.exit:
                return step
            for d in DIRECTIONS:
                p = position + d
                if p in self.space and p not in corrupted and p not in reached:
                    reached.add(p)
                    frontier.append((p, step + 1))

    def part_two(self):
        for corruption in range(1025, len(self.bytes)):
            if self.part_one(corruption) is None:
                x, y = self.bytes[corruption].real, self.bytes[corruption].imag
                return f"{int(x)},{int(y)}"


if __name__ == "__main__":
    Today().solve()
