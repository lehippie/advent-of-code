"""Day 11: Seating System."""

from itertools import product
from aoc.puzzle import Puzzle


class SeatsLayout:
    def __init__(self, seats, tolerance=4):
        self.seats = seats
        self.tolerance = tolerance
        self.occupied = set()

    def count(self, seat):
        """Count occupied adjacent seats."""
        adjacents = product(*((s - 1, s, s + 1) for s in seat))
        return len(self.occupied.intersection(adjacents).difference({seat}))

    def stabilize(self):
        """Perform rounds until the layout doesn't change
        and return the count of occupied seats.
        """
        while True:
            occupied = self.occupied.copy()
            for seat in self.seats:
                if seat not in self.occupied and self.count(seat) == 0:
                    occupied.add(seat)
                elif seat in self.occupied and self.count(seat) >= self.tolerance:
                    occupied.remove(seat)
            if occupied == self.occupied:
                return len(occupied)
            self.occupied = occupied


class VisibilityLayout(SeatsLayout):
    def __init__(self, seats, tolerance=5):
        super().__init__(seats, tolerance)
        self.size = (max(r for r, _ in seats), max(c for _, c in seats))

    def count(self, seat):
        """Count occupied nearest seats in each direction."""
        seen = 0
        row, col = seat
        for dr, dc in product([-1, 0, 1], repeat=2):
            if (dr, dc) == (0, 0):
                continue
            xy = (row + dr, col + dc)
            while 0 <= xy[0] <= self.size[0] and 0 <= xy[1] <= self.size[1]:
                if xy not in self.seats:
                    xy = (xy[0] + dr, xy[1] + dc)
                else:
                    if xy in self.occupied:
                        seen += 1
                    break
        return seen


class Today(Puzzle):
    def parser(self):
        self.seats = set(
            (r, c)
            for r, row in enumerate(self.input)
            for c, col in enumerate(row)
            if col == "L"
        )

    def part_one(self):
        return SeatsLayout(self.seats).stabilize()

    def part_two(self):
        return VisibilityLayout(self.seats).stabilize()


solutions = (2251, 2019)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
