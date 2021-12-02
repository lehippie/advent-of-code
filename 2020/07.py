"""Day 7: Handy Haversacks."""

import re
from aoc.puzzle import Puzzle


MY_BAG = "shiny gold"


def containers(rules, bag):
    """Return a set of containers for <bag>."""
    return {r for r in rules if bag in rules[r]}


class Puzzle07(Puzzle):
    def parser(self):
        data = {}
        for line in self.input:
            bag, inside = line.split(" bags contain ")
            inside = re.findall(r"(\d+)\s([a-z]+\s[a-z]+)\sbag", inside)
            inside = {k: int(v) for v, k in inside}
            data[bag] = inside
        return data

    def part_one(self):
        bags = containers(self.input, MY_BAG)
        while True:
            previous_bags = bags.copy()
            for b in previous_bags:
                bags.update(containers(self.input, b))
            if bags == previous_bags:
                return len(bags)

    def part_two(self):
        insides = {}
        bags_queue = list(self.input[MY_BAG].items())
        while bags_queue:
            bag, quantity = bags_queue.pop(0)
            insides[bag] = insides.get(bag, 0) + quantity
            bags_queue.extend((b, q * quantity) for b, q in self.input[bag].items())
        return sum(insides.values())


if __name__ == "__main__":
    Puzzle07(solutions=(151, 41559)).solve()
