"""--- Day 21: Step Counter ---"""

from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j)


class Today(Puzzle):
    def parser(self):
        self.garden = set()
        for r, row in enumerate(self.input):
            for c, tile in enumerate(row):
                position = r + c * 1j
                if tile == "S":
                    self.start = position
                    self.garden.add(position)
                elif tile == ".":
                    self.garden.add(position)

    def part_one(self, steps=64):
        history = [set(), set([self.start])]
        for _ in range(steps):
            frontier = list(history[-1])
            reached = set()
            while frontier:
                position = frontier.pop()
                for direction in DIRECTIONS:
                    p = position + direction
                    if (
                        p in self.garden
                        and p not in history[-1]
                        and p not in history[-2]
                    ):
                        reached.add(p)
            history.append(reached)
        return sum(len(h) for h in history[-1::-2])

    def part_two(self):
        return super().part_two()


solutions = (3639, None)

if __name__ == "__main__":
    Today(infile="test.txt", solutions=(16, None)).solve()
    # Today(solutions=solutions).solve()
