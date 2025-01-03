"""--- Day 16: Reindeer Maze ---"""

from heapq import heappop, heappush
from aoc.puzzle import Puzzle

DIRECTIONS = {1: (1, 1j, -1j), -1: (-1, 1j, -1j), 1j: (1j, 1, -1), -1j: (-1j, 1, -1)}


class Cplx(complex):
    def __lt__(self, other):
        """Order defined to use complexes in a heap."""
        return self.real < other.real


class Today(Puzzle):
    def parser(self):
        self.walls = set()
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                if cell == "#":
                    self.walls.add(r + c * 1j)
                elif cell == "S":
                    self.start = r + c * 1j
                elif cell == "E":
                    self.end = r + c * 1j

    def part_one(self):
        """Dijkstra in the maze."""
        scores = {(self.start, 1j): 0}
        frontier = [(0, Cplx(self.start), Cplx(1j))]
        while frontier:
            score, position, direction = heappop(frontier)

            if position == self.end:
                self.best_score = score
                return score

            for d in DIRECTIONS[direction]:
                step = position + d
                if step in self.walls:
                    continue
                s = score + (1 if d == direction else 1001)
                if (step, d) not in scores or s < scores[(step, d)]:
                    scores[(step, d)] = s
                    heappush(frontier, (s, Cplx(step), Cplx(d)))

    def part_two(self):
        """Same as part one but we keep the paths in the frontier and
        stop only when we reach a higher score than the best one.
        """
        tiles = set()
        scores = {(self.start, 1j): 0}
        frontier = [(0, Cplx(self.start), Cplx(1j), {self.start})]
        while frontier:
            score, position, direction, path = heappop(frontier)

            if position == self.end and score == self.best_score:
                tiles.update(path)
                continue
            if score > self.best_score:
                return len(tiles)

            for d in DIRECTIONS[direction]:
                step = position + d
                if step in self.walls:
                    continue
                s = score + (1 if d == direction else 1001)
                if (step, d) not in scores or s <= scores[(step, d)]:
                    scores[(step, d)] = s
                    heappush(frontier, (s, Cplx(step), Cplx(d), path.union({step})))


if __name__ == "__main__":
    Today().solve()
