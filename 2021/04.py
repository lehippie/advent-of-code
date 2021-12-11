"""Day 4: Giant Squid."""

import numpy as np
from aoc.puzzle import Puzzle


class Board:
    def __init__(self, grid):
        self.grid = np.array(grid)

    def mark(self, number):
        self.grid[self.grid == number] = -self.grid[self.grid == number]

    def wins(self):
        if any((self.grid < 0).all(axis=0)) or any((self.grid < 0).all(axis=1)):
            return True
        return False

    def score(self):
        return sum(n for n in self.grid.flatten() if n > 0)


class Puzzle04(Puzzle):
    def parser(self):
        self.draws = list(map(int, self.input[0].split(",")))
        self.grids = []
        for k in range(2, len(self.input), 6):
            self.grids.append(
                [list(map(int, row.split())) for row in self.input[k : k + 5]]
            )

    def part_one(self, get="winner"):
        boards = [Board(grid) for grid in self.grids]
        for draw in self.draws:
            [board.mark(draw) for board in boards]
            winners = [board.wins() for board in boards]
            if any(winners):
                if get == "winner":
                    return boards[winners.index(True)].score() * draw
                elif get == "loser":
                    if len(boards) > 1:
                        boards = [board for board, win in zip(boards, winners) if not win]
                    else:
                        return boards[0].score() * draw

    def part_two(self):
        return self.part_one("loser")


if __name__ == "__main__":
    Puzzle04(solutions=(87456, 15561)).solve()
