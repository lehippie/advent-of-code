"""Day 20: Grove Positioning System."""

from collections import deque
from aoc.puzzle import Puzzle

SIGN = lambda n: (n > 0) - (n < 0)


def mix(numbers, order):
    for i, n in order:
        while numbers[-1] != (i, n):
            numbers.rotate()
        numbers.pop()
        numbers.rotate(-SIGN(n) * (abs(n) % len(numbers)))
        numbers.append((i, n))
    return numbers


def decrypt(numbers):
    while numbers[0][1] != 0:
        numbers.rotate()
    return sum(numbers[i % len(numbers)][1] for i in (1000, 2000, 3000))


class Today(Puzzle):
    def parser(self):
        self.order = list(enumerate(map(int, self.input)))

    def part_one(self):
        numbers = deque(self.order)
        numbers = mix(numbers, self.order)
        return decrypt(numbers)

    def part_two(self):
        new_order = [(i, 811589153 * n) for i, n in self.order]
        numbers = deque(new_order)
        for _ in range(10):
            numbers = mix(numbers, new_order)
        return decrypt(numbers)


solutions = (5498, 3390007892081)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
