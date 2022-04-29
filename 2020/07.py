"""Day 7: Handy Haversacks."""

import re
from aoc.puzzle import Puzzle


MY_BAG = "shiny gold"


def containers(rules, bag):
    """Return a set of containers for <bag>."""
    return {r for r in rules if bag in rules[r]}


class Today(Puzzle):
    def parser(self):
        self.rules = {}
        for line in self.input:
            bag, inside = line.split(" bags contain ")
            inside = re.findall(r"(\d+)\s([a-z]+\s[a-z]+)\sbag", inside)
            inside = {k: int(v) for v, k in inside}
            self.rules[bag] = inside

    def part_one(self):
        bags = containers(self.rules, MY_BAG)
        while True:
            previous_bags = bags.copy()
            for b in previous_bags:
                bags.update(containers(self.rules, b))
            if bags == previous_bags:
                return len(bags)

    def part_two(self):
        insides = {}
        bags_queue = list(self.rules[MY_BAG].items())
        while bags_queue:
            bag, quantity = bags_queue.pop(0)
            insides[bag] = insides.get(bag, 0) + quantity
            bags_queue.extend((b, q * quantity) for b, q in self.rules[bag].items())
        return sum(insides.values())


solutions = (151, 41559)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
