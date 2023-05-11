"""Day 3: Crossed Wires."""

from aoc.puzzle import Puzzle

STEPS = {"U": 1j, "D": -1j, "L": -1, "R": 1}


class Wire:
    def __init__(self, steps):
        self.path = [0]
        for d, n in ((p[0], int(p[1:])) for p in steps.split(",")):
            for _ in range(n):
                self.path.append(self.path[-1] + STEPS[d])


class Today(Puzzle):
    def parser(self):
        self.wire1 = Wire(self.input[0])
        self.wire2 = Wire(self.input[1])

    def part_one(self):
        self.crosses = set(self.wire1.path).intersection(self.wire2.path)
        return min(abs(c.real) + abs(c.imag) for c in self.crosses if c != 0)

    def part_two(self):
        return min(
            self.wire1.path.index(c) + self.wire2.path.index(c)
            for c in self.crosses
            if c != 0
        )


solutions = (446, 9006)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
