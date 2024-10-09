"""--- Day 8: Space Image Format ---"""

from collections import Counter
from hashlib import md5
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        n = 25 * 6
        self.layers = [self.input[k : k + n] for k in range(0, len(self.input), n)]
        zeros = [Counter(l)["0"] for l in self.layers]
        counts = Counter(self.layers[zeros.index(min(zeros))])
        return counts["1"] * counts["2"]

    def part_two(self):
        image = []
        for k in range(25 * 6):
            pixel = next(l[k] for l in self.layers if l[k] != "2")
            image.append("#" if pixel == "1" else " ")
        image = "\n".join("".join(image[k : k + 25]) for k in range(0, len(image), 25))
        # print(image)
        return md5(image.encode()).hexdigest()


if __name__ == "__main__":
    Today().solve()
