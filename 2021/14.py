"""Day 14: Extended Polymerization."""

from collections import Counter
from aoc.puzzle import Puzzle


class Polymer:
    def __init__(self, template, rules):
        """As for lanternfishes in day 6, only the amount of pairs in
        the polymer matters, not their positions. Another counter
        keeps track of the polymer's constitutive elements.
        """
        self.pairs = Counter(a + b for a, b in zip(template, template[1:]))
        self.elements = Counter(template)
        self.rules = rules

    def step(self):
        """Each pair of elements is converted in two new pairs and
        the element created in the middle is added to the polymer's
        elements counter.
        """
        new_pairs = Counter()
        for pair, amount in self.pairs.items():
            inserted = self.rules[pair]
            new_pairs[pair[0] + inserted] += amount
            new_pairs[inserted + pair[1]] += amount
            self.elements[inserted] += amount
        self.pairs = new_pairs


class Today(Puzzle):
    def parser(self):
        self.template = self.input[0]
        self.rules = {}
        for rule in self.input[2:]:
            pair, inserted = rule.split(" -> ")
            self.rules[pair] = inserted

    def part_one(self, steps=10):
        poly = Polymer(self.template, self.rules)
        for _ in range(steps):
            poly.step()
        return max(poly.elements.values()) - min(poly.elements.values())

    def part_two(self):
        return self.part_one(40)


solutions = (3906, 4441317262452)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
