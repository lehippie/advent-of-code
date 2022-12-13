"""Day 13: Distress Signal."""

from functools import cmp_to_key
from json import loads
from aoc.puzzle import Puzzle


def compare(left, right):
    """If left and right are integers, return their difference. Else,
    ensure both arguments are lists and compare elements one by one,
    returning the first integers/list-lengths difference found.
    """
    left_int = isinstance(left, int)
    right_int = isinstance(right, int)
    if left_int and right_int:
        return left - right
    if left_int != right_int:
        left = [left] if left_int else left
        right = [right] if right_int else right
    try:
        for l, r in zip(left, right, strict=True):
            if (c := compare(l, r)) != 0:
                return c
    except ValueError:
        return len(left) - len(right)
    return 0


class Today(Puzzle):
    def parser(self):
        self.pairs = "|".join(self.input).split("||")
        self.pairs = [list(map(loads, pair.split("|"))) for pair in self.pairs]

    def part_one(self):
        correct = []
        for p, (left, right) in enumerate(self.pairs):
            if compare(left, right) < 0:
                correct.append(p + 1)
        return sum(correct)

    def part_two(self):
        """Using integers/list-lengths differences as comparison
        outputs, we can use 'sorted' with our function as key.
        """
        d1, d2 = [[2]], [[6]]
        packets = [d1, d2]
        for pairs in self.pairs:
            packets.extend(pairs)
        packets = sorted(packets, key=cmp_to_key(compare))
        return (packets.index(d1) + 1) * (packets.index(d2) + 1)


solutions = (5843, 26289)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
