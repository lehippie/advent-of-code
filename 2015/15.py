"""Day 15: Science for Hungry People."""

import re
from math import prod
from aoc.puzzle import Puzzle


def combi_sum(total, n):
    """Combinations of <n> numbers summing to <total>."""
    if n == 1:
        yield (total,)
    else:
        for spoon in range(total + 1):
            for remaining in combi_sum(total - spoon, n - 1):
                yield (spoon,) + remaining


class Today(Puzzle):
    def parser(self):
        def parse(line):
            return tuple(map(int, re.findall(r"-?\d+", line)))

        self.ingredients = list(map(parse, self.input))

    def part_one(self, teaspoons=100, target_calories=None):
        best_cookie = 0
        for spoons in combi_sum(teaspoons, len(self.ingredients)):
            stats = [0] * 5
            for spoon, ingredient in zip(spoons, self.ingredients):
                for k in range(5):
                    stats[k] += spoon * ingredient[k]
            cookie_calories = stats.pop()
            if target_calories is None or cookie_calories == target_calories:
                if all(s > 0 for s in stats) and prod(stats) > best_cookie:
                    best_cookie = prod(stats)
        return best_cookie

    def part_two(self):
        return self.part_one(target_calories=500)


if __name__ == "__main__":
    Today().solve()
