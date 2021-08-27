"""Day 15: Science for Hungry People."""

import re
from math import prod

from aoc.puzzle import Puzzle


def parser(puzzle_line):
    name, rest = puzzle_line.split(":")
    return (name, *map(int, re.findall(r"-?\d+", rest)))


def combi_sum(total, size):
    if size == 1:
        yield (total,)
    else:
        for spoon in range(total + 1):
            for remaining in combi_sum(total - spoon, size - 1):
                yield (spoon,) + remaining


class TodayPuzzle(Puzzle):
    def part_one(self, teaspoons=100, calories=None):
        best_cookie = 0
        for spoons in combi_sum(teaspoons, len(self.input)):
            stats = [0] * 5
            for spoon, ingredient in zip(spoons, self.input):
                for k in range(5):
                    stats[k] += spoon * ingredient[k + 1]
            cookie_cal = stats.pop()
            if calories is None or cookie_cal == calories:
                if all(s > 0 for s in stats) and prod(stats) > best_cookie:
                    best_cookie = prod(stats)
        return best_cookie

    def part_two(self, teaspoons=100, calories=500):
        return self.part_one(teaspoons, calories)


if __name__ == "__main__":
    TodayPuzzle(parser=parser, parse_lines=True, solutions=(13882464, 11171160)).solve()