"""Day 3: Rucksack Reorganization."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        pass

    def part_one(self):
        priority = 0
        for sack in self.input:
            l = len(sack) // 2
            item = set(sack[:l]).intersection(sack[l:]).pop()
            priority += ord(item) - (96 if item.islower() else 38)
        return priority

    def part_two(self):
        priority = 0
        for k in range(0, len(self.input), 3):
            e1, e2, e3 = self.input[k : k + 3]
            badge = set(e1).intersection(e2).intersection(e3).pop()
            priority += ord(badge) - (96 if badge.islower() else 38)
        return priority


solutions = (7795, None)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
