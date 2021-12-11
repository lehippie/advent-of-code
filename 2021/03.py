"""Day 3: Binary Diagnostic."""

from collections import Counter
from aoc.puzzle import Puzzle


def filtering(numbers, method):
    k = 0
    while len(numbers) > 1:
        count = Counter(n[k] for n in numbers)
        if count[0] == count[1]:
            count.update("1")
        numbers = [n for n in numbers if n[k] == method(count, key=count.get)]
        k += 1
    return numbers[0]


class Puzzle03(Puzzle):
    def part_one(self):
        counts = [Counter() for _ in range(len(self.input[0]))]
        for number in self.input:
            [counts[k].update(n) for k, n in enumerate(number)]
        gamma = "".join(max(count, key=count.get) for count in counts)
        epsilon = "".join(min(count, key=count.get) for count in counts)
        return int(gamma, base=2) * int(epsilon, base=2)

    def part_two(self):
        ox = filtering(self.input, method=max)
        co2 = filtering(self.input, method=min)
        return int(ox, base=2) * int(co2, base=2)


if __name__ == "__main__":
    Puzzle03(solutions=(1082324, 1353024)).solve()
