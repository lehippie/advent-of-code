"""Day 1: Calorie Counting."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.elves = ",".join(self.input).split(",,")
        self.elves = [list(map(int, e.split(","))) for e in self.elves]

    def part_one(self):
        return max(sum(e) for e in self.elves)

    def part_two(self):
        calories = sorted(sum(e) for e in self.elves)
        return sum(calories[-3:])


solutions = (71924, 210406)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
