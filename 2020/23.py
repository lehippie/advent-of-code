"""Day 23: Crab Cups."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.circle = list(map(int, self.input))

    def part_one(self, moves=100):
        """Naive approach constructing a new list after each move.
        Current cup is always kept as the first element of the list.
        """
        cups = self.circle
        for _ in range(moves):
            try:
                dest = next(c for c in range(cups[0] - 1, 0, -1) if c in cups[4:])
            except StopIteration:
                dest = max(cups[4:])
            dest = cups.index(dest)
            cups = cups[4 : dest + 1] + cups[1:4] + cups[dest + 1 :] + [cups[0]]
        one = cups.index(1)
        return int("".join(str(c) for c in cups[one + 1 :] + cups[:one]))

    def part_two(self, moves=10000000, ncups=1000000):
        """Constructing large lists is expensive. Instead, cups are
        the indexes of a list where the value is the cup that follows
        clockwise."""
        init = self.circle + list(range(max(self.circle) + 1, ncups + 1))
        cups = [None for _ in range(ncups + 1)]
        for c, n in zip(init, init[1:] + [init[0]]):
            cups[c] = n

        cup = init[0]
        for _ in range(moves):
            pick1 = cups[cup]
            pick2 = cups[pick1]
            pick3 = cups[pick2]
            picked = {pick1, pick2, pick3}
            try:
                dest = next(c for c in range(cup - 1, 0, -1) if c not in picked)
            except StopIteration:
                dest = next(c for c in range(ncups, 0, -1) if c not in picked)
            cups[cup] = cups[pick3]
            cups[pick3] = cups[dest]
            cups[dest] = pick1
            cup = cups[cup]

        return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    Today().solve()
