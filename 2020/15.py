"""Day 15: Rambunctious Recitation."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.starting_numbers = list(map(int, self.input.split(",")))

    def part_one(self, limit=2020):
        """Spoken numbers are the indexes of a list storing the most
        recent turn where they were spoken.
        """
        spoken = [0] * limit
        for i, n in enumerate(self.starting_numbers[:-1]):
            spoken[n] = i + 1
        last = self.starting_numbers[-1]
        for turn in range(len(self.starting_numbers), limit):
            if spoken[last]:
                age = turn - spoken[last]
                spoken[last] = turn
                last = age
            else:
                spoken[last] = turn
                last = 0
        return last

    def part_two(self):
        return self.part_one(limit=30000000)


if __name__ == "__main__":
    Today().solve()
