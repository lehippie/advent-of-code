"""Day 22: Monkey Map."""

import re
from aoc.puzzle import Puzzle


TURN = {
    "R": {1: 1j, 1j: -1, -1: -1j, -1j: 1},
    "L": {1: -1j, -1j: -1, -1: 1j, 1j: 1},
}
FACING = {1: 0, 1j: 1, -1: 2, -1j: 3}


class Board:
    def __init__(self, grid, path, start):
        self.grid = grid
        self.path = path
        self.pos = start
        self.face = 1

    def move(self):
        for p in self.path:
            if p in TURN:
                self.face = TURN[p][self.face]
            else:
                for _ in range(p):
                    destination = self.pos + self.face
                    if destination not in self.grid:
                        destination = self.wrap()
                    if self.grid[destination]:
                        self.pos = destination
                    else:
                        break

    def wrap(self):
        destination = self.pos
        while destination - self.face in self.grid:
            destination -= self.face
        return destination

    def password(self):
        return int(1000 * self.pos.imag + 4 * self.pos.real + FACING[self.face])


class Today(Puzzle):
    def parser(self):
        self.grid = {}
        self.start = None
        for r, row in enumerate(self.input[:-1]):
            for c, col in enumerate(row):
                if col in ".#":
                    self.grid[(c + 1) + (r + 1) * 1j] = col == "."
                    if self.start is None:
                        self.start = (c + 1) + (r + 1) * 1j
        self.path = re.split(r"([RL])", self.input[-1])
        self.path = [int(d) if d.isdigit() else d for d in self.path]

    def part_one(self):
        board = Board(self.grid, self.path, self.start)
        board.move()
        return board.password()

    def part_two(self):
        return super().part_two()


solutions = (26558, None)

if __name__ == "__main__":
    Today(solutions=solutions, infile="22.txt").solve()
    Today(solutions=solutions).solve()
