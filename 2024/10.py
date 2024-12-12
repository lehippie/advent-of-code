"""--- Day 10: Hoof It ---"""

from collections import defaultdict
from itertools import product
from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j)


class Today(Puzzle):
    def parser(self):
        self.map = defaultdict(set)
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                self.map[int(cell)].add(r + c * 1j)

    def part_one(self):
        scores = 0
        for trailhead in self.map[0]:
            positions = {trailhead}
            for height in range(1, 10):
                next_positions = {
                    p + d
                    for p, d in product(positions, DIRECTIONS)
                    if p + d in self.map[height]
                }
                positions = next_positions
            scores += len(positions)
        return scores

    def part_two(self):
        """Trails are kept track of by keeping the positions of
        successive heights with the count of paths leading to it.
        """
        ratings = 0
        for trailhead in self.map[0]:
            paths = {trailhead: 1}
            for height in range(1, 10):
                new_paths = defaultdict(int)
                for position, count in paths.items():
                    for d in DIRECTIONS:
                        p = position + d
                        if p in self.map[height]:
                            new_paths[p] += count
                paths = new_paths
            ratings += sum(paths.values())
        return ratings


if __name__ == "__main__":
    Today().solve()
