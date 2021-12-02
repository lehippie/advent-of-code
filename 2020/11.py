"""Day 11: Seating System."""

from collections import Counter
from copy import deepcopy
from itertools import product
from aoc.puzzle import Puzzle


class Seats:
    def __init__(self, layout):
        self.layout = deepcopy(layout)

    def __str__(self):
        return "\n".join("".join(l) for l in self.layout)

    def occupied(self):
        return Counter(str(self)).get("#", 0)

    def count_around(self, row, col):
        occupation = Counter()
        for r in self.layout[max(row - 1, 0) : min(row + 2, len(self.layout))]:
            occupation.update(r[max(col - 1, 0) : min(col + 2, len(r))])
        occupation.subtract(self.layout[row][col])
        return occupation.get("#", 0)

    def count_seen(self, row, col):
        max_distance = max(len(self.layout), len(self.layout[0]))
        occupation = Counter()
        for dr, dc in product([-1, 0, 1], repeat=2):
            if (dr, dc) == (0, 0):
                continue
            direction_seats = (
                (row + k * dr, col + k * dc)
                for k in range(1, max_distance)
                if (
                    0 <= row + k * dr < len(self.layout)
                    and 0 <= col + k * dc < len(self.layout[0])
                )
            )
            try:
                occupation.update(
                    next(
                        self.layout[r][c]
                        for r, c in direction_seats
                        if self.layout[r][c] != "."
                    )
                )
            except StopIteration:
                pass
        return occupation.get("#", 0)

    def stabilize(self, limit, method):
        if method == "around":
            count = self.count_around
        elif method == "seen":
            count = self.count_seen

        while True:
            new_layout = deepcopy(self.layout)
            for r, c in product(
                range(len(new_layout)),
                range(len(new_layout[0])),
            ):
                if new_layout[r][c] == "L" and count(r, c) == 0:
                    new_layout[r][c] = "#"
                elif new_layout[r][c] == "#" and count(r, c) >= limit:
                    new_layout[r][c] = "L"
            if new_layout == self.layout:
                break
            else:
                self.layout = new_layout


class Puzzle11(Puzzle):
    def parser(self):
        return list(map(list, self.input))

    def part_one(self, limit=4, method="around"):
        seats = Seats(self.input)
        seats.stabilize(limit, method)
        return seats.occupied()

    def part_two(self):
        return self.part_one(limit=5, method="seen")


if __name__ == "__main__":
    Puzzle11(solutions=(2251, 2019)).solve()
