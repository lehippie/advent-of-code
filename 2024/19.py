"""--- Day 19: Linen Layout ---"""

from functools import lru_cache
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.towels = tuple(self.input[0].split(", "))
        self.designs = self.input[2:]
        self.lengths = sorted({len(t) for t in self.towels}, reverse=True)

    def part_one(self):
        @lru_cache
        def is_possible(design):
            if design in self.towels:
                return True
            for l in self.lengths:
                if design[:l] in self.towels and is_possible(design[l:]):
                    return True
            return False

        self.possible_designs = [d for d in self.designs if is_possible(d)]
        return len(self.possible_designs)

    def part_two(self):
        @lru_cache
        def count_possible(design):
            count = 0
            if design in self.towels:
                count += 1
            for l in self.lengths:
                if design[:l] != design and design[:l] in self.towels:
                    count += count_possible(design[l:])
            return count

        return sum(count_possible(d) for d in self.possible_designs)


if __name__ == "__main__":
    Today().solve()
