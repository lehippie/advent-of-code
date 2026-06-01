"""--- Day 9: Movie Theater ---"""

from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.tiles = [list(map(int, line.split(","))) for line in self.input]

    def part_one(self):
        return max(
            (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
            for (xi, yi), (xj, yj) in combinations(self.tiles, r=2)
        )

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    # test = Today(test_input="""parse_lines_here""")
    # r1 = test.part_one()
    # assert r1 == expected_result, r1
    # r2 = test.part_two()
    # assert r2 == expected_result, r2

    Today().solve()
