"""Day 5: Binary Boarding."""

from aoc.puzzle import Puzzle


TRANSTABLE = str.maketrans("BFRL", "1010")


class Puzzle05(Puzzle):
    def part_one(self):
        self.seats = [int(p.translate(TRANSTABLE), base=2) for p in self.input]
        return max(self.seats)

    def part_two(self):
        return next(
            seat
            for seat in range(min(self.seats) + 1, max(self.seats))
            if seat not in self.seats
        )


if __name__ == "__main__":
    Puzzle05(solutions=(928, 610)).solve()
