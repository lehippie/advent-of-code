"""Day 15: Chiton."""

from heapq import heappush, heappop
from aoc.puzzle import Puzzle


class RiskGrid:
    def __init__(self, risk, extended):
        self.risk = risk
        self.extended = extended
        self.h = len(risk)
        self.w = len(risk[0])
        self.start = (0, 0)
        if extended is None:
            self.end = (self.h - 1, self.w - 1)
        else:
            self.end = (extended * self.h - 1, extended * self.w - 1)

    def neighbors(self, position):
        r, c = position
        for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= row <= self.end[0] and 0 <= col <= self.end[1]:
                yield row, col

    def __getitem__(self, position):
        r, c = position
        if self.extended is None:
            return self.risk[r][c]
        base_risk = self.risk[r % self.h][c % self.w]
        row_mult = r // self.h
        col_mult = c // self.w
        return 1 + (base_risk + row_mult + col_mult - 1) % 9


class Puzzle15(Puzzle):
    def parser(self):
        return [list(map(int, line)) for line in self.input]

    def part_one(self, extended=None):
        risk = RiskGrid(self.input, extended)
        exploration = [(0, risk.start)]
        visited = {risk.start}
        while exploration:
            local_risk, position = heappop(exploration)
            for p in risk.neighbors(position):
                if p == risk.end:
                    return local_risk + risk[p]
                if p not in visited:
                    heappush(exploration, (local_risk + risk[p], p))
                    visited.add(p)

    def part_two(self):
        return self.part_one(extended=5)


if __name__ == "__main__":
    Puzzle15(solutions=(390, 2814)).solve()
