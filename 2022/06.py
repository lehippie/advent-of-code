"""Day 6: Tuning Trouble."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, size=4):
        for m in range(size, len(self.input)):
            if len(set(self.input[m - size : m])) == size:
                return m

    def part_two(self):
        return self.part_one(size=14)


if __name__ == "__main__":
    Today().solve()
