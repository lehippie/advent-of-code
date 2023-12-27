"""--- Day 21: Step Counter ---"""

from aoc.puzzle import Puzzle

MOVES = (1, -1, 1j, -1j)


class Today(Puzzle):
    def parser(self):
        self.garden = set()
        for r, row in enumerate(self.input):
            for c, tile in enumerate(row):
                position = r + c * 1j
                if tile == "S":
                    self.start = position
                if tile != "#":
                    self.garden.add(position)

    def part_one(self, steps=64):
        plots = [1, 0]
        lasts = [set(), set([self.start])]
        for s in range(1, steps + 1):
            new = set()
            for position in lasts[s % 2]:
                for direction in MOVES:
                    p = position + direction
                    if p in self.garden and p not in lasts[0] and p not in lasts[1]:
                        new.add(p)
            plots[s % 2] += len(new)
            lasts[(s + 1) % 2] = new
        return plots[steps % 2]

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    Today().solve()
