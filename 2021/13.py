"""Day 13: Transparent Origami."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Origami:
    def __init__(self, dots):
        self.dots = dots

    def fold(self, ax, n):
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
        self.fold_instructions = []
        for line in self.input:
            if "," in line:
                self.dots.add(tuple(map(int, line.split(","))))
            elif line.startswith("fold"):
                ax, n = line.split("=")
                self.fold_instructions.append((ax[-1], int(n)))

    def part_one(self):
        self.paper = Origami(self.dots)
        self.paper.fold(*self.fold_instructions[0])
        return len(self.paper.dots)

    def part_two(self):
        for fold in self.fold_instructions[1:]:
            self.paper.fold(*fold)
        code = str(self.paper)
        # print(code)
        return md5(code.encode()).hexdigest()


solutions = (664, "185cfe412e2e8fd08c2eecfc9d96a469")

if __name__ == "__main__":
    Today(solutions=solutions).solve()
