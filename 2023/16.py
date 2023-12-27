"""--- Day 16: The Floor Will Be Lava ---"""

from aoc.puzzle import Puzzle

DIRECTIONS = {
    ".": {1j: [1j], -1j: [-1j], 1: [1], -1: [-1]},
    "/": {1j: [-1], -1j: [1], 1: [-1j], -1: [1j]},
    "\\": {1j: [1], -1j: [-1], 1: [1j], -1: [-1j]},
    "-": {1j: [1j], -1j: [-1j], 1: [1j, -1j], -1: [1j, -1j]},
    "|": {1j: [1, -1], -1j: [1, -1], 1: [1], -1: [-1]},
}


class Contraption:
    def __init__(self, grid):
        self.N = len(grid)
        self.tiles = {}
        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                self.tiles[r + c * 1j] = tile

    def energize(self, start=(0, 1j)):
        beams = [start]
        energized = set(beams)
        while beams:
            position, direction = beams.pop()
            for new_dir in DIRECTIONS[self.tiles[position]][direction]:
                new_pos = position + new_dir
                if new_pos in self.tiles and (new_pos, new_dir) not in energized:
                    beams.append((new_pos, new_dir))
                    energized.add((new_pos, new_dir))
        return len(set(e[0] for e in energized))


class Today(Puzzle):
    def parser(self):
        self.contraption = Contraption(self.input)

    def part_one(self):
        return self.contraption.energize()

    def part_two(self):
        starts = []
        for i in range(self.contraption.N):
            starts.extend([(i, 1j), (i + (self.contraption.N - 1) * 1j, -1j)])
            starts.extend([(i * 1j, 1), ((self.contraption.N - 1) + i * 1j, -1)])
        return max(self.contraption.energize(s) for s in starts)


if __name__ == "__main__":
    Today().solve()
