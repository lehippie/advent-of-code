"""Day 11: Seating System."""

from collections import Counter
from copy import deepcopy
from itertools import product
from pathlib import Path


INPUT_FILE = "seat_layout.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [list(line.strip()) for line in f]
    return data


# --- Part One ---

class Seats:
    def __init__(self, layout):
        self.layout = deepcopy(layout)

    def __str__(self):
        return '\n'.join("".join(l) for l in self.layout)

    @property
    def occupied(self):
        return Counter(str(self)).get("#", 0)

    def count_around(self, row, col):
        occupation = Counter()
        for r in self.layout[max(row-1, 0):min(row+2, len(self.layout))]:
            occupation.update(r[max(col-1, 0):min(col+2, len(r))])
        occupation.subtract(self.layout[row][col])
        return occupation.get("#", 0)

    def count_seen(self, row, col):
        max_distance = max(len(self.layout), len(self.layout[0]))
        occupation = Counter()
        for dr, dc in product([-1, 0, 1], repeat=2):
            if (dr, dc) == (0, 0):
                continue
            direction_seats = (
                (row + k*dr, col + k*dc)
                for k in range(1, max_distance)
                if (0 <= row + k*dr < len(self.layout)
                and 0 <= col + k*dc < len(self.layout[0]))
            )
            try:
                occupation.update(next(
                    self.layout[r][c]
                    for r, c in direction_seats
                    if self.layout[r][c] != "."
                ))
            except StopIteration:
                pass
        return occupation.get("#", 0)

    def stabilize(self, limit=4, method="around", print_steps=False):
        if method == "around":
            count = self.count_around
        elif method == "seen":
            count = self.count_seen
        else:
            raise IOError(f"Unknown method {method}.")
        
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


def part_one(seat_layout):
    """Part One solution."""
    seats = Seats(seat_layout)
    seats.stabilize()
    print(f"{seats.occupied} seats are occupied after stabilization.")
    assert seats.occupied == 2251


# --- Part Two ---

def part_two(seat_layout):
    """Part Two solution."""
    seats = Seats(seat_layout)
    seats.stabilize(5, "seen")
    print(f"{seats.occupied} seats are occupied after real stabilization.")
    assert seats.occupied == 2019


# --- Tests ---

def tests():
    # Part One
    test_input = load_input("test_input.txt")
    test = Seats(test_input)
    test.stabilize()
    assert test.occupied == 37
    # Part Two
    test = Seats(test_input)
    test.stabilize(5, "seen")
    assert test.occupied == 26


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
