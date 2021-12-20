"""Day 20: Trench Map."""

import numpy as np
from aoc.puzzle import Puzzle


class Image:
    def __init__(self, algo, img):
        self.algo = algo
        self.img = img
        self.outside = 0

    def step(self):
        self.img = np.pad(self.img, 1, constant_values=self.outside)
        pad = np.pad(self.img, 1, constant_values=self.outside)
        for (r, c), _ in np.ndenumerate(self.img):
            binary = "".join(str(p) for p in pad[r: r + 3, c: c + 3].flatten())
            self.img[r,c] = self.algo[int(binary, base=2)]
        self.outside = self.algo[int(str(self.outside) * 9, base=2)]


class Puzzle20(Puzzle):
    def parser(self):
        self.input = [
            list(map(int, l.replace("#", "1").replace(".", "0"))) for l in self.input
        ]
        self.algo = self.input[0]
        self.img = np.array(self.input[2:])

    def part_one(self, steps=2):
        trench = Image(self.algo, self.img)
        for _ in range(steps):
            trench.step()
        return trench.img.sum()

    def part_two(self):
        return self.part_one(steps=50)


if __name__ == "__main__":
    Puzzle20(solutions=(5347, 17172)).solve()
