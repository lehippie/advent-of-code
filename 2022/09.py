"""Day 9: Rope Bridge."""

from aoc.puzzle import Puzzle


MOVE = {"U": 1j, "D": -1j, "L": -1, "R": 1}
SIGN = lambda n: (n > 0) - (n < 0)


class Today(Puzzle):
    def parser(self):
        self.motions = [(line[0], int(line[2:])) for line in self.input]

    def part_one(self):
        h, t = 0j, 0j
        visited = {t}
        for m, n in self.motions:
            for _ in range(n):
                h += MOVE[m]
                if abs(l := h - t) >= 2:
                    t += SIGN(l.real) + 1j * SIGN(l.imag)
                visited.add(t)
        return len(visited)

    def part_two(self):
        rope = [0j] * 10
        visited = {rope[-1]}
        for m, n in self.motions:
            for _ in range(n):
                rope[0] += MOVE[m]
                for k in range(1, len(rope)):
                    if abs(l := rope[k - 1] - rope[k]) >= 2:
                        rope[k] += SIGN(l.real) + 1j * SIGN(l.imag)
                visited.add(rope[-1])
        return len(visited)


solutions = (6354, 2651)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
