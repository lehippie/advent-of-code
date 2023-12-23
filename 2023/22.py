"""--- Day 22: Sand Slabs ---"""

from aoc.puzzle import Puzzle


class Brick:
    def __init__(self, i, start, end):
        self.i = i
        self.xy = set(
            x + y * 1j
            for x in range(start[0], end[0] + 1)
            for y in range(start[1], end[1] + 1)
        )
        self.z = [start[2], end[2]]
        self.up = []
        self.down = []

    def __str__(self):
        return str(self.i)

    def __hash__(self):
        return self.i


def stabilize(falling: list[Brick]) -> list:
    """Make bricks falls and save their contacts."""
    stables = []
    for brick in sorted(falling, key=lambda b: b.z):
        below = [b for b in stables if brick.xy.intersection(b.xy)]
        if below:
            maxz = max(b.z[1] for b in below)
            below = [b for b in below if b.z[1] == maxz]
            for b in below:
                brick.down.append(b)
                b.up.append(brick)
        else:
            maxz = 0
        brick.z = [h - brick.z[0] + maxz + 1 for h in brick.z]
        stables.append(brick)
    return stables


class Today(Puzzle):
    def parser(self):
        self.falling = []
        for i, line in enumerate(self.input):
            start, end = line.split("~")
            start = list(map(int, start.split(",")))
            end = list(map(int, end.split(",")))
            self.falling.append(Brick(i, start, end))

    def part_one(self):
        self.bricks = stabilize(self.falling)
        return sum(all(len(b.down) > 1 for b in brick.up) for brick in self.bricks)

    def part_two(self):
        return super().part_two()


solutions = (477, None)

if __name__ == "__main__":
    Today(infile="test.txt", solutions=(5, None)).solve()
    # Today(solutions=solutions).solve()
