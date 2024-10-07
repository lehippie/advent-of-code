"""Day 20: Trench Map."""

import numpy as np
from aoc.puzzle import Puzzle


class Image:
    def __init__(self, algo, img):
        self.algo = algo
        self.img = img
        self.padding = 0

    def step(self):
        """The padding pixels could (will) switch from dark to lit, so
        their state is stored independently of the image.
        The latter is padded twice: once for storing the next step
        image, and once again to get the 9 surrounding pixels of the
        new image's border.
        Finally, the new padding becomes the algorithm value at index
        511 or 0, depending of the current padding.
        """
        self.img = np.pad(self.img, 1, constant_values=self.padding)
        pad = np.pad(self.img, 1, constant_values=self.padding)
        for (r, c), _ in np.ndenumerate(self.img):
            binary = "".join("1" if p else "0" for p in pad[r : r + 3, c : c + 3].flat)
            self.img[r, c] = self.algo[int(binary, base=2)]
        self.padding = self.algo[511 if self.padding else 0]


class Today(Puzzle):
    def parser(self):
        binary = [[int(l == "#") for l in line] for line in self.input]
        self.algo = binary[0]
        self.img = np.array(binary[2:])

    def part_one(self, steps=2):
        trench = Image(self.algo, self.img)
        for _ in range(steps):
            trench.step()
        return trench.img.sum()

    def part_two(self):
        return self.part_one(steps=50)


if __name__ == "__main__":
    Today().solve()
