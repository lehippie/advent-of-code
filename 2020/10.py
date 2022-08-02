"""Day 10: Adapter Array."""

from collections import Counter
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.jolts = set([0]).union(map(int, self.input))

    def part_one(self):
        """Best way to use all adapters is to sort them. As our device
        is exactly 3 jolts above the highest adapter, it can only be
        reached by the latter so we add 1 to the count of 3-jolt
        differences.
        """
        chain = sorted(self.jolts)
        differences = Counter(a - b for a, b in zip(chain[1:], chain))
        return differences[1] * (differences[3] + 1)

    def part_two(self):
        """Starting with the unique outlet, replace recursively each
        joltage by the adapters that can be plugged in. The amount of
        arrangements is counted by removing from the joltages queue
        all path that reached the last adapter.
        """
        joltages = Counter({0: 1})
        arrangements = 0
        while joltages:
            jolt = min(joltages)
            n = joltages.pop(jolt)
            plugs = range(jolt + 1, jolt + 4)
            joltages.update({j: n for j in self.jolts.intersection(plugs)})
            arrangements += joltages.pop(max(self.jolts), 0)
        return arrangements


solutions = (2201, 169255295254528)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
