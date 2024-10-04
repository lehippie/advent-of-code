"""Day 12: JSAbacusFramework.io."""

import json
import re
from aoc.puzzle import Puzzle


def almost_sum(data, discard="red"):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(almost_sum(v) for v in data)
    if isinstance(data, dict):
        if discard not in data.values():
            return almost_sum(list(data.values()))
    return 0


class Today(Puzzle):
    def part_one(self):
        return sum(map(int, re.findall(r"-?\d+", self.input)))

    def part_two(self):
        return almost_sum(json.loads(self.input))


if __name__ == "__main__":
    Today().solve()
