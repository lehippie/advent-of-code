"""Day 13: Transparent Origami."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Origami:
    def __init__(self, dots):
        self.dots = dots

    def folds(self, ax, n):
        ax = 0 if ax == "x" else 1
        dots = set()
        for dot in self.dots:
            if dot[ax] < n:
                dots.add(dot)
            else:
                dot = list(dot)
                dot[ax] = 2 * n - dot[ax]
                dots.add(tuple(dot))
        self.dots = dots

    def __str__(self):
        maxx = max(x for x, _ in self.dots)
        maxy = max(y for _, y in self.dots)
        return "\n".join(
            "".join("#" if (x, y) in self.dots else " " for x in range(maxx + 1))
            for y in range(maxy + 1)
        )


class Today(Puzzle):
    def parser(self):
        self.dots = set()
        self.folds = []
        for line in self.input:
            if line[0:1].isnumeric():
                self.dots.add(tuple(map(int, line.split(","))))
            elif line.startswith("fold"):
                ax, n = line.split("=")
                self.folds.append((ax[-1], int(n)))

    def part_one(self):
        paper = Origami(self.dots)
        paper.folds(*self.folds[0])
        return len(paper.dots)

    def part_two(self):
        paper = Origami(self.dots)
        for fold in self.folds:
            paper.folds(*fold)
        code = str(paper)
        # print(code)
        return md5(code.encode()).hexdigest()


solutions = (664, "185cfe412e2e8fd08c2eecfc9d96a469")

if __name__ == "__main__":
    Today(solutions=solutions).solve()
