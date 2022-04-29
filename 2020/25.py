"""Day 25: Combo Breaker."""

from aoc.puzzle import Puzzle


def transform(subject_number, loop):
    value = 1
    for _ in range(loop):
        value = (value * subject_number) % 20201227
    return value


class Today(Puzzle):
    def parser(self):
        self.keys = list(map(int, self.input))

    def part_one(self):
        value = 1
        loop = 0
        while value not in self.keys:
            value = (value * 7) % 20201227
            loop += 1
        return transform(self.keys[(self.keys.index(value) + 1) % 2], loop)


solutions = (17673381, NotImplemented)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
