"""--- Day 8: Playground ---"""

from itertools import combinations
from math import prod, sqrt
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.boxes = [list(map(int, box.split(","))) for box in self.input]

    def part_one(self):
        self.distances = sorted(
            (sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2), i, j)
            for (i, A), (j, B) in combinations(enumerate(self.boxes), r=2)
        )
        circuits = [{k} for k in range(len(self.boxes))]
        for k in range(1000):
            box1, box2 = self.distances[k][1:]
            c1 = next(c for c in circuits if box1 in c)
            i, c2 = next((i, c) for i, c in enumerate(circuits) if box2 in c)
            if c1 != c2:
                c1.update(c2)
                del circuits[i]
        return prod(sorted(map(len, circuits))[-3:])

    def part_two(self):
        circuits = [{k} for k in range(len(self.boxes))]
        for k in range(len(self.distances)):
            box1, box2 = self.distances[k][1:]
            c1 = next(c for c in circuits if box1 in c)
            i, c2 = next((i, c) for i, c in enumerate(circuits) if box2 in c)
            if c1 != c2:
                c1.update(c2)
                del circuits[i]
            if len(circuits) == 1:
                return self.boxes[box1][0] * self.boxes[box2][0]


if __name__ == "__main__":
    Today().solve()
