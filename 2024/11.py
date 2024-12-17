"""--- Day 11: Plutonian Pebbles ---"""

from collections import defaultdict
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.stones = list(map(int, self.input.split()))

    def part_one(self, blinks=25):
        stones = defaultdict(int)
        for stone in self.stones:
            stones[stone] += 1
        for _ in range(blinks):
            next_stones = defaultdict(int)
            for stone, n in stones.items():
                if not stone:
                    next_stones[1] += n
                elif not (l := len(s := str(stone))) % 2:
                    next_stones[int(s[: l // 2])] += n
                    next_stones[int(s[l // 2 :])] += n
                else:
                    next_stones[stone * 2024] += n
            stones = next_stones
        return sum(stones.values())

    def part_two(self):
        return self.part_one(75)


if __name__ == "__main__":
    Today().solve()
