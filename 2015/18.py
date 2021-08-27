"""Day 18: Like a GIF For Your Yard."""

from itertools import product

from aoc.puzzle import Puzzle


class Grid:
    def __init__(self, initial_state, corners_stuck=False):
        self.size = len(initial_state)
        self.on = set()
        for i, line in enumerate(initial_state):
            self.on.update({(i, j) for j, s in enumerate(line) if s == "#"})
        if corners_stuck:
            self.stuck = set(product((0, self.size - 1), repeat=2))
            self.on.update(self.stuck)
        else:
            self.stuck = set()

    def neighbors(self, position):
        arounds = set(product(*((p, p - 1, p + 1) for p in position)))
        for pos in arounds.copy():
            if pos == position or not all(0 <= x < self.size for x in pos):
                arounds.remove(pos)
        return arounds

    def run_step(self, N=1):
        for _ in range(N):
            next_on = set(self.stuck)
            off_to_check = set()
            for light in self.on:
                neighbors = self.neighbors(light)
                if len(neighbors.intersection(self.on)) in {2, 3}:
                    next_on.add(light)
                off_to_check.update(neighbors.difference(self.on))
            for light in off_to_check:
                if len(self.neighbors(light).intersection(self.on)) == 3:
                    next_on.add(light)
            self.on = next_on


class TodayPuzzle(Puzzle):
    def part_one(self, steps=100):
        grid = Grid(self.input)
        grid.run_step(steps)
        return len(grid.on)

    def part_two(self, steps=100):
        grid = Grid(self.input, corners_stuck=True)
        grid.run_step(steps)
        return len(grid.on)


if __name__ == "__main__":
    TodayPuzzle(solutions=(768, 781)).solve()
