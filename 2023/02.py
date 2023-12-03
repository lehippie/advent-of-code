"""--- Day 2: Cube Conundrum ---"""

import re
from aoc.puzzle import Puzzle


def is_possible(game, max_cubes):
    """A game is possible if the maximum amount of cubes seen is not
    higher than the input limit.
    """
    for color, maxi in max_cubes.items():
        max_seen = max(map(int, re.findall(rf"(\d+) {color}", game)))
        if max_seen > maxi:
            return 0
    return int(game.split(":")[0].split(" ")[-1])


def power(game):
    """The power of a game is the product of the maximum amount of
    cubes seen.
    """
    p = 1
    for color in ("red", "green", "blue"):
        max_seen = max(map(int, re.findall(rf"(\d+) {color}", game)))
        p *= max_seen
    return p


class Today(Puzzle):
    def part_one(self):
        max_cubes = {"red": 12, "green": 13, "blue": 14}
        return sum(is_possible(game, max_cubes) for game in self.input)

    def part_two(self):
        return sum(power(game) for game in self.input)


solutions = (2237, 66681)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
