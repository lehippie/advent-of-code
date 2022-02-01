"""Day 6: Lanternfish."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, days=80):
        ages = [self.input.count(str(k)) for k in range(9)]
        for _ in range(days):
            ages = ages[1:] + [ages[0]]
            ages[6] += ages[-1]
        return sum(ages)

    def part_two(self):
        return self.part_one(256)


solutions = (379414, 1705008653296)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
