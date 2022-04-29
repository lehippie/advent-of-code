"""Day 15: Rambunctious Recitation."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.starting_numbers = list(map(int, self.input.split(",")))

    def part_one(self, limit=2020):
        spoken = [None] * limit
        for i, n in enumerate(self.starting_numbers[:-1]):
            spoken[n] = i + 1
        last = self.starting_numbers[-1]
        for turn in range(len(self.starting_numbers), limit):
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


solutions = (468, 1801753)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
