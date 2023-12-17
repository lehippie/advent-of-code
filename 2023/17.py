"""--- Day 17: Clumsy Crucible ---"""

from heapq import heappush, heappop
from aoc.puzzle import Puzzle


DIRECTIONS = {1, -1, 1j, -1j}


def distance(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


class Today(Puzzle):
    def parser(self):
        self.city = {}
        for r, row in enumerate(self.input):
            for c, heat in enumerate(row):
                self.city[r + c * 1j] = int(heat)
        self.factory = (len(self.input) - 1) * (1 + 1j)

    def part_one(self):
        """Dijkstra applied to the heatmap.
        The status of a path contains the total heat loss, the
        position and the last direction taken with its count.

        The direction and count have to be saved when passing throught
        same city blocks because a longer path getting there can leads
        to shorter one globally (see example: row 1, column 6).
        """
        reached = {(0, 0, 0)}
        frontier = [(0, (0, 0), (0, 0), 0)]
        while frontier:
            heat, (pr, pc), (dr, dc), count = heappop(frontier)
            position = pr + pc * 1j
            direction = dr + dc * 1j
            for d in DIRECTIONS:
                if d == -direction or (d == direction and count == 3):
                    continue
                c = count + 1 if d == direction else 1
                p = position + d
                if p in self.city and (p, d, c) not in reached:
                    h = heat + self.city[p]
                    if p == self.factory:
                        return h
                    reached.add((p, d, c))
                    heappush(frontier, (h, (p.real, p.imag), (d.real, d.imag), c))

    def part_two(self):
        """Same logic as part one with the new limitations."""
        reached = {(0, 0, 0)}
        frontier = [(0, (0, 0), (0, 0), 0)]
        while frontier:
            heat, (pr, pc), (dr, dc), count = heappop(frontier)
            position = pr + pc * 1j
            direction = dr + dc * 1j
            for d in DIRECTIONS:
                if d == -direction or (d == direction and count == 10):
                    continue
                c = count + 1 if d == direction else 4
                p = position + d if c > 4 else position + 4 * d
                if p in self.city and (p, d, c) not in reached:
                    h = heat + sum(
                        self.city[position + (i + 1) * d]
                        for i in range(int(abs(position - p)))
                    )
                    if p == self.factory:
                        return h
                    reached.add((p, d, c))
                    heappush(frontier, (h, (p.real, p.imag), (d.real, d.imag), c))


solutions = (755, 881)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
