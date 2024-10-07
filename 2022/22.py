"""Day 22: Monkey Map."""

import re
from collections import defaultdict
from itertools import product
from aoc.puzzle import Puzzle


FACING = {1: 0, 1j: 1, -1: 2, -1j: 3}
TURN = {
    "R": {1: 1j, 1j: -1, -1: -1j, -1j: 1},
    "L": {1: -1j, -1j: -1, -1: 1j, 1j: 1},
}


class Board:
    def __init__(self, grid, path, start):
        self.grid = grid
        self.path = path
        self.point = start
        self.face = 1

    def move(self):
        for p in self.path:
            if p in TURN:
                self.face = TURN[p][self.face]
            else:
                for _ in range(p):
                    destination = self.point + self.face
                    if destination not in self.grid:
                        destination = self.wrap()
                    if not self.grid[destination]:
                        break
                    self.point = destination
        return int(1000 * self.point.imag + 4 * self.point.real + FACING[self.face])

    def wrap(self):
        destination = self.point
        while destination - self.face in self.grid:
            destination -= self.face
        return destination


class Cube(Board):
    def __init__(self, grid, path, start):
        super().__init__(grid, path, start)
        self.find_links()

    def adjacents(self, point):
        point = int(point.real), int(point.imag)
        for adj in product(*((p - 1, p, p + 1) for p in point)):
            if adj != point:
                yield adj[0] + adj[1] * 1j

    def find_links(self):
        """Find the corners of the grid and follow the edges to link
        their points together. Stop when two vertices are found
        because it makes the edges go apart.
        Each point on the edge is linked to the destinations of each
        direction going out of the grid.
        """
        corners = {}
        vertices = set()
        for p in self.grid:
            adjacent = set(self.adjacents(p))
            outsides = adjacent.difference(self.grid)
            if len(outsides) == 1:
                corners[p] = outsides.pop()
            elif len(outsides) == 5:
                vertices.add(p)

        self.links = defaultdict(dict)
        while corners:
            corner, out = corners.popitem()
            pts = [corner, corner]
            dirs = [(out - corner).real, (out - corner).imag * 1j]
            edges = dirs[::-1]
            while True:
                pts = [p + d for p, d in zip(pts, dirs)]
                self.links[pts[0]][edges[0]] = [pts[1], -edges[1]]
                self.links[pts[1]][edges[1]] = [pts[0], -edges[0]]
                vidx = [k for k, p in enumerate(pts) if p in vertices]
                if not vidx:
                    continue
                elif len(vidx) == 2:
                    break
                v, p = vidx[0], not vidx[0]
                pts[p] += dirs[p]
                rot = next(t for t in "LR" if pts[v] + TURN[t][dirs[v]] in self.grid)
                dirs[v] = TURN[rot][dirs[v]]
                edges[v] = TURN[rot][edges[v]]
                self.links[pts[p]][edges[p]] = [pts[v], -edges[v]]
                self.links[pts[v]][edges[v]] = [pts[p], -edges[p]]

    def wrap(self):
        """Adjust position using links and adjust facing."""
        destination, new_face = self.links[self.point][self.face]
        if self.grid[destination]:
            self.face = new_face
            return destination
        return self.point


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
        return board.move()

    def part_two(self):
        cube = Cube(self.grid, self.path, self.start)
        return cube.move()


if __name__ == "__main__":
    Today().solve()
