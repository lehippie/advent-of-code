"""Day 8: Treetop Tree House."""

from itertools import product
import numpy as np
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.trees = np.array([list(line) for line in self.input], dtype=int)
        self.R = len(self.trees)
        self.C = len(self.trees[0])

    def part_one(self):
        visibles = 2 * (self.R + self.C) - 4
        for r, c in product(range(1, self.R - 1), range(1, self.C - 1)):
            up = self.trees[:r, c]
            down = self.trees[r + 1 :, c]
            left = self.trees[r, :c]
            right = self.trees[r, c + 1 :]
            for direction in (up, down, left, right):
                if all(direction < self.trees[r, c]):
                    visibles += 1
                    break
        return visibles

    def part_two(self):
        best_score = 0
        for r, c in product(range(1, self.R - 1), range(1, self.C - 1)):
            up = np.flip(self.trees[:r, c])
            down = self.trees[r + 1 :, c]
            left = np.flip(self.trees[r, :c])
            right = self.trees[r, c + 1 :]
            score = 1
            for direction in (up, down, left, right):
                highers = direction >= self.trees[r, c]
                score *= np.argmax(highers) + 1 if any(highers) else len(direction)
            best_score = max(best_score, score)
        return best_score


if __name__ == "__main__":
    Today().solve()
