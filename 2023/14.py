"""--- Day 14: Parabolic Reflector Dish ---"""

from itertools import takewhile
from aoc.puzzle import Puzzle

MOVE = {"N": 1j, "S": -1j, "E": 1, "W": -1}


class Platform:
    def __init__(self, grid):
        self.N = len(grid)
        self.rocks, self.cubes = set(), set()
        for r, row in enumerate(grid):
            for c, rtype in enumerate(row, 1):
                position = c + (self.N - r) * 1j
                if rtype == "O":
                    self.rocks.add(position)
                elif rtype == "#":
                    self.cubes.add(position)
        # Add edges of the platform as outer cubes
        self.cubes.update(i + (self.N + 1) * 1j for i in range(1, self.N + 1))
        self.cubes.update(i for i in range(1, self.N + 1))
        self.cubes.update(self.N + 1 + i * 1j for i in range(1, self.N + 1))
        self.cubes.update(i * 1j for i in range(1, self.N + 1))
        # Calculate spaces to check in each direction of the cubes
        self.cubes = {cube: self.freespace(cube) for cube in self.cubes}

    def freespace(self, cube):
        out = {}
        for direction, offset in MOVE.items():
            out[direction] = set(
                takewhile(
                    lambda pos: pos not in self.cubes
                    and 0 < pos.imag <= self.N
                    and 0 < pos.real <= self.N,
                    (cube - r * offset for r in range(1, self.N + 1)),
                )
            )
        return out

    def move(self, direction):
        rolled_rocks = set()
        for cube, spaces in self.cubes.items():
            nrocks = len(spaces[direction].intersection(self.rocks))
            rolled_rocks.update(
                cube - i * MOVE[direction] for i in range(1, nrocks + 1)
            )
        self.rocks = rolled_rocks


class Today(Puzzle):
    def part_one(self):
        platform = Platform(self.input)
        platform.move("N")
        return int(sum(r.imag for r in platform.rocks))

    def part_two(self):
        return NotImplemented

solutions = (102497, None)

if __name__ == "__main__":
    Today(infile="test.txt", solutions=(136, 64)).solve()
    # Today(solutions=solutions).solve()
