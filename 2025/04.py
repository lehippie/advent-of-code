"""--- Day 4: Printing Department ---"""

from aoc.puzzle import Puzzle

AROUNDS = (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)


class Today(Puzzle):
    def parser(self):
        self.rolls = set()
        for r, row in enumerate(self.input):
            for c, col in enumerate(row):
                if col == "@":
                    self.rolls.add(r + c * 1j)

    def part_one(self):
        return sum(
            sum((roll + a) in self.rolls for a in AROUNDS) < 4 for roll in self.rolls
        )

    def part_two(self):
        removed = set()
        remains = self.rolls
        while True:
            stays = set()
            for roll in remains:
                if sum((roll + a) in remains for a in AROUNDS) < 4:
                    removed.add(roll)
                else:
                    stays.add(roll)
            if stays == remains:
                break
            remains = stays
        return len(removed)


if __name__ == "__main__":
    Today().solve()
