"""Day 14: Extended Polymerization."""

from collections import Counter
from aoc.puzzle import Puzzle


class Polymer:
    def __init__(self, template, rules):
        self.elements = Counter(template)
        self.pairs = Counter(a + b for a, b in zip(template[:-1], template[1:]))
        self.rules = rules

    def run_step(self):
        new_pairs = Counter()
        for pair, count in self.pairs.items():
            insert = self.rules[pair]
            self.elements[insert] += count
            new_pairs[pair[0] + insert] += count
            new_pairs[insert + pair[1]] += count
        self.pairs = new_pairs


class Today(Puzzle):
    def parser(self):
        self.template = self.input[0]
        self.rules = {}
        for rule in self.input[2:]:
            pair, insert = rule.split(" -> ")
            self.rules[pair] = insert

    def part_one(self, steps=10):
        poly = Polymer(self.template, self.rules)
        for _ in range(steps):
            poly.run_step()
        return max(poly.elements.values()) - min(poly.elements.values())

    def part_two(self):
        return self.part_one(40)


solutions = (3906, 4441317262452)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
