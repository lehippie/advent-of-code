"""Day 10: Adapter Array."""

from collections import Counter
from aoc.puzzle import Puzzle


class Puzzle10(Puzzle):
    def parser(self):
        return list(map(int, self.input))

    def part_one(self):
        joltages = sorted(self.input + [0, max(self.input) + 3])
        differences = Counter(a - b for a, b in zip(joltages[1:], joltages[:-1]))
        return differences[1] * differences[3]

    def part_two(self):
        end_jolt = max(self.input) + 3
        jolts = set(self.input + [0, end_jolt])
        tree = Counter({0: 1})
        arrangements_count = 0
        while tree:
            new_tree = Counter()
            for n, q in tree.items():
                new_tree.update({j: q for j in jolts.intersection(range(n + 1, n + 4))})
            arrangements_count += new_tree.pop(end_jolt, 0)
            tree = new_tree
        return arrangements_count


if __name__ == "__main__":
    Puzzle10(solutions=(2201, 169255295254528)).solve()
