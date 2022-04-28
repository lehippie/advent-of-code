"""Day 15: Science for Hungry People."""

import re
from math import prod
from aoc.puzzle import Puzzle


def combi_sum(total, size):
    if size == 1:
        yield (total,)
    else:
        for spoon in range(total + 1):
            for remaining in combi_sum(total - spoon, size - 1):
                yield (spoon,) + remaining


class Today(Puzzle):
    def parser(self):
        def parse(line):
            name, rest = line.split(":")
            return (name, *map(int, re.findall(r"-?\d+", rest)))

        self.ingredients = list(map(parse, self.input))

    def part_one(self, teaspoons=100, calories=None):
        best_cookie = 0
        for spoons in combi_sum(teaspoons, len(self.ingredients)):
            stats = [0] * 5
            for spoon, ingredient in zip(spoons, self.ingredients):
                for k in range(5):
                    stats[k] += spoon * ingredient[k + 1]
            cookie_cal = stats.pop()
            if calories is None or cookie_cal == calories:
                if all(s > 0 for s in stats) and prod(stats) > best_cookie:
                    best_cookie = prod(stats)
        return best_cookie

    def part_two(self):
        return self.part_one(calories=500)


solutions = (13882464, 11171160)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
