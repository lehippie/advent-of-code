"""Day 15: Chiton."""

from heapq import heappush, heappop
from aoc.puzzle import Puzzle


class RiskLevelMap:
    """Part one use the input directly as the risk level map.
    The <extension_factor> is used for part two and its extended
    grid. It modifies the more distant goal and the way risk level
    is calculated outside of the base tile.
    """

    def __init__(self, tile, extension_factor):
        self.tile = tile
        self.nrows = len(tile)
        self.ncols = len(tile[0])
        self.goal = (
            self.nrows * extension_factor - 1,
            self.ncols * extension_factor - 1,
        )

    def neighbors(self, position):
        r, c = position
        for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= row <= self.goal[0] and 0 <= col <= self.goal[1]:
                yield row, col

    def __getitem__(self, position):
        r, c = position
        base_risk = self.tile[r % self.nrows][c % self.ncols]
        row_offset = r // self.nrows
        col_offset = c // self.ncols
        return (base_risk + row_offset + col_offset) % 9 or 9


class Today(Puzzle):
    def parser(self):
        self.risk_level = [list(map(int, line)) for line in self.input]

    def part_one(self, extension_factor=1):
        """Dijkstra applied on the risk level grid."""
        risks = RiskLevelMap(self.risk_level, extension_factor)
        reached = {(0, 0)}
        frontier = [(0, (0, 0))]
        while frontier:
            risk, position = heappop(frontier)
            for neighbor in risks.neighbors(position):
                if neighbor == risks.goal:
                    return risk + risks[neighbor]
                if neighbor not in reached:
                    reached.add(neighbor)
                    heappush(frontier, (risk + risks[neighbor], neighbor))

    def part_two(self):
        """Same algorithm as part one but with an extended grid."""
        return self.part_one(extension_factor=5)


solutions = (390, 2814)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
