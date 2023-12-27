"""--- Day 23: A Long Walk ---"""

from aoc.puzzle import Puzzle

MOVES = {"^": -1, ">": 1j, "v": 1, "<": -1j}


class Today(Puzzle):
    def parser(self):
        self.trails = {}
        self.start = self.input[0].index(".") * 1j
        self.goal = (len(self.input) - 1) + self.input[-1].index(".") * 1j
        for r, row in enumerate(self.input):
            for c, tile in enumerate(row):
                if tile != "#":
                    self.trails[r + c * 1j] = tile

    def part_one(self):
        paths = [(self.start, set([self.start]), 0)]
        maxsteps = 0
        while paths:
            new_paths = []
            for pos, reached, steps in paths:
                if pos == self.goal:
                    maxsteps = max(maxsteps, steps)
                    continue
                # Get valid directions
                if self.trails[pos] in MOVES:
                    directions = [MOVES[self.trails[pos]]]
                else:
                    directions = MOVES.values()
                # Create new paths for each direction
                for d in directions:
                    new_pos = pos + d
                    if new_pos in self.trails and new_pos not in reached:
                        new_reached = reached.union([new_pos])
                        new_paths.append((new_pos, new_reached, steps + 1))
            paths = new_paths
        return maxsteps

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    # Today(test_input="test.txt").solve((94, 154))
    Today().solve()
