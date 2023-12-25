"""Day 25: Sea Cucumber."""

from aoc.puzzle import Puzzle
from itertools import product


class CucumberTrench:
    def __init__(self, east: set, south: set, nrow, ncol):
        self.east = east
        self.south = south
        self.nrow = nrow
        self.ncol = ncol

    def step(self):
        new_east = set()
        for pos in self.east:
            new_pos = pos[0], (pos[1] + 1) % self.ncol
            if new_pos in self.east or new_pos in self.south:
                new_east.add(pos)
            else:
                new_east.add(new_pos)
        self.east = new_east
        new_south = set()
        for pos in self.south:
            new_pos = (pos[0] + 1) % self.nrow, pos[1]
            if new_pos in self.east or new_pos in self.south:
                new_south.add(pos)
            else:
                new_south.add(new_pos)
        self.south = new_south


class Today(Puzzle):
    def parser(self):
        self.nrow = len(self.input)
        self.ncol = len(self.input[0])
        self.east = set()
        self.south = set()
        for i, j in product(range(self.nrow), range(self.ncol)):
            if self.input[i][j] == ">":
                self.east.add((i, j))
            elif self.input[i][j] == "v":
                self.south.add((i, j))

    def part_one(self):
        trench = CucumberTrench(self.east, self.south, self.nrow, self.ncol)
        steps = 0
        while True:
            old_east = trench.east.copy()
            old_south = trench.south.copy()
            steps += 1
            trench.step()
            if trench.east == old_east and trench.south == old_south:
                break
        return steps


solutions = 435

if __name__ == "__main__":
    Today(solutions=solutions).solve()
