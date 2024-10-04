"""Day 5: Binary Boarding."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        """Seat IDs are hidden binary numbers. Converting them
        to intergers allow direct manipulation.
        """
        transtable = str.maketrans("FBLR", "0101")
        self.seats = {int(p.translate(transtable), base=2) for p in self.input}

    def part_one(self):
        return max(self.seats)

    def part_two(self):
        seat = min(self.seats)
        while seat in self.seats:
            seat += 1
        return seat


if __name__ == "__main__":
    Today().solve()
