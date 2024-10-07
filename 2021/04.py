"""Day 4: Giant Squid."""

import numpy as np
from aoc.puzzle import Puzzle


class Board:
    def __init__(self, grid):
        self.grid = np.array(grid)

    def mark(self, number):
        """Mark a number by switching it to '-1'."""
        self.grid[self.grid == number] = -1

    def wins(self):
        """Check if a row or a column is completely marked."""
        return any((self.grid < 0).all(axis=0)) or any((self.grid < 0).all(axis=1))

    def score(self, winning_draw):
        """Sum of unmarked numbers."""
        return sum(n for n in self.grid.flatten() if n != -1) * winning_draw


class Today(Puzzle):
    def parser(self):
        self.draws = list(map(int, self.input[0].split(",")))
        self.grids = []
        for k in range(2, len(self.input), 6):
            self.grids.append(
                [list(map(int, row.split())) for row in self.input[k : k + 5]]
            )

    def part_one(self):
        boards = [Board(grid) for grid in self.grids]
        for draw in self.draws:
            for board in boards:
                board.mark(draw)
            winners = [board.wins() for board in boards]
            if any(winners):
                return boards[winners.index(True)].score(draw)

    def part_two(self):
        boards = [Board(grid) for grid in self.grids]
        for draw in self.draws:
            for board in boards:
                board.mark(draw)
            if len(boards) == 1 and boards[0].wins():
                return boards[0].score(draw)
            boards = [board for board in boards if not board.wins()]


if __name__ == "__main__":
    Today().solve()
