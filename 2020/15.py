"""Day 15: Rambunctious Recitation."""

from aoc.puzzle import Puzzle


class Puzzle15(Puzzle):
    def parser(self):
        return list(map(int, self.input.split(",")))

    def part_one(self, limit=2020):
        spoken = [None] * limit
        for i, n in enumerate(self.input[:-1]):
            spoken[n] = i + 1
        last = self.input[-1]
        for turn in range(len(self.input), limit):
            if spoken[last] is None:
                spoken[last] = turn
                last = 0
            else:
                age = turn - spoken[last]
                spoken[last] = turn
                last = age
        return last

    def part_two(self):
        return self.part_one(limit=30000000)


if __name__ == "__main__":
    Puzzle15(solutions=(468, 1801753)).solve()
