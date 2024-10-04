"""Day 7: Handy Haversacks."""

import re
from aoc.puzzle import Puzzle


MY_BAG = "shiny gold"


class Today(Puzzle):
    def parser(self):
        self.rules = {}
        for line in self.input:
            bag, inside = line.split(" bags contain ")
            inside = re.findall(r"(\d+)\s([a-z]+\s[a-z]+)\sbag", inside)
            self.rules[bag] = {k: int(v) for v, k in inside}

    def part_one(self):
        def containers(rules, bag):
            """Return a set of possible containers for a bag."""
            return {b for b, content in rules.items() if bag in content}

        bags = containers(self.rules, MY_BAG)
        while True:
            previous_bags = bags.copy()
            for bag in previous_bags:
                bags.update(containers(self.rules, bag))
            if bags == previous_bags:
                return len(bags)

    def part_two(self):
        insides = {}
        bags_queue = list(self.rules[MY_BAG].items())
        while bags_queue:
            bag, n = bags_queue.pop()
            insides[bag] = insides.get(bag, 0) + n
            bags_queue.extend((b, n * k) for b, k in self.rules[bag].items())
        return sum(insides.values())


if __name__ == "__main__":
    Today().solve()
