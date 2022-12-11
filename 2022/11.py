"""Day 11: Monkey in the Middle."""

import re
from copy import deepcopy
from math import prod
from aoc.puzzle import Puzzle


class Monkey:
    def __init__(self, items, op, div, targets):
        self.items = items
        self.op = op
        self.div = div
        self.targets = targets
        self.inspections = 0


class Today(Puzzle):
    def parser(self):
        self.monkeys = []
        for monkey in "\n".join(self.input).split("\n\n"):
            m = monkey.split("\n")
            items = list(map(int, re.findall(r"\d+", m[1])))
            op = eval(f"lambda old: {m[2].split('=')[1]}")
            div = int(m[3].split()[-1])
            targets = {True: int(m[4].split()[-1]), False: int(m[5].split()[-1])}
            self.monkeys.append(Monkey(items, op, div, targets))

    def part_one(self, rounds=20, relief=lambda n: n // 3):
        monkeys = deepcopy(self.monkeys)
        for _ in range(rounds):
            for m in monkeys:
                m.inspections += len(m.items)
                for i in m.items:
                    i = relief(m.op(i))
                    monkeys[m.targets[i % m.div == 0]].items.append(i)
                m.items = []
        inspections = sorted(m.inspections for m in monkeys)
        return inspections[-1] * inspections[-2]

    def part_two(self):
        """The product of monkeys' divisors will be divisible by any
        monkey so the modulo of this number contains all information
        we need.
        """
        mod = prod(m.div for m in self.monkeys)
        return self.part_one(rounds=10000, relief=lambda n: n % mod)


solutions = (316888, 35270398814)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
