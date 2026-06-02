"""Day 1: Calorie Counting."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.elves = [
            list(map(int, elf.split("|"))) for elf in "|".join(self.input).split("||")
        ]

    def part_one(self):
        return max(sum(e) for e in self.elves)

    def part_two(self):
        calories = sorted(sum(e) for e in self.elves)
        return sum(calories[-3:])


if __name__ == "__main__":
    Today().solve()
