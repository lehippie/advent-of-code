"""Day 23: Crab Cups."""

from aoc.puzzle import Puzzle


class Puzzle23(Puzzle):
    def parser(self):
        return list(map(int, self.input))

    def part_one(self, moves=100):
        cups = self.input
        for _ in range(moves):
            try:
                cup = next(c for c in range(cups[0] - 1, 0, -1) if c not in cups[1:4])
                dest = cups.index(cup)
            except StopIteration:
                dest = cups.index(max(cups[4:]))
            cups = cups[4 : dest + 1] + cups[1:4] + cups[dest + 1 :] + [cups[0]]
        one = cups.index(1)
        return int("".join(str(c) for c in cups[one + 1 :] + cups[:one]))

    def part_two(self, moves=10000000, maxi=1000000):
        cups = self.input
        init = cups + list(range(max(cups) + 1, maxi + 1))
        cups = [None for _ in range(maxi + 1)]
        for c, n in zip(init, init[1:] + [init[0]]):
            cups[c] = n

        cur = init[0]
        for _ in range(moves):
            pick1 = cups[cur]
            pick2 = cups[pick1]
            pick3 = cups[pick2]
            picked = {pick1, pick2, pick3}
            try:
                dest = next(cup for cup in range(cur - 1, 0, -1) if cup not in picked)
            except StopIteration:
                dest = next(cup for cup in range(maxi, 0, -1) if cup not in picked)
            cups[cur] = cups[pick3]
            cups[pick3] = cups[dest]
            cups[dest] = pick1
            cur = cups[cur]

        return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    Puzzle23(solutions=(24987653, 442938711161)).solve()
