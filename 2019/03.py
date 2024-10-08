"""Day 3: Crossed Wires."""

from aoc.puzzle import Puzzle

DIRECTIONS = {"U": 1j, "D": -1j, "L": -1, "R": 1}


def wire_path(steps):
    path = [0]
    for step in steps.split(","):
        start, direction, n = path[-1], DIRECTIONS[step[0]], int(step[1:])
        path.extend(start + k * direction for k in range(1, n + 1))
    return path


class Today(Puzzle):
    def part_one(self):
        self.wire1 = wire_path(self.input[0])
        self.wire2 = wire_path(self.input[1])
        self.crosses = set(self.wire1).intersection(self.wire2)
        self.crosses.remove(0)
        return min(abs(c.real) + abs(c.imag) for c in self.crosses)

    def part_two(self):
        return min(self.wire1.index(c) + self.wire2.index(c) for c in self.crosses)


if __name__ == "__main__":
    Today().solve()
