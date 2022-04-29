"""Day 16: Ticket Translation."""

import re
from copy import deepcopy
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.rules = {}
        lines = iter(self.input)
        while line := next(lines):
            field, ranges = line.rstrip().split(": ")
            ranges = re.findall(r"(\d+)-(\d+)", ranges)
            self.rules[field] = set()
            for r1, r2 in ranges:
                self.rules[field].update(range(int(r1), int(r2) + 1))
        while not next(lines).startswith("your"):
            pass
        self.me = [int(v) for v in next(lines).rstrip().split(",")]
        while not next(lines).startswith("nearby"):
            pass
        self.nearby = []
        for line in lines:
            self.nearby.append([int(v) for v in line.rstrip().split(",")])

    def part_one(self):
        accepted_values = set()
        for s in self.rules.values():
            accepted_values.update(s)
        error_rate = 0
        valids_nearby = []
        for ticket in self.nearby:
            errors = [value for value in ticket if value not in accepted_values]
            if errors:
                error_rate += sum(errors)
            else:
                valids_nearby.append(ticket)
        self.nearby = valids_nearby
        return error_rate

    def part_two(self):
        values_per_position = [set(v) for v in zip(*self.nearby)]
        my_ticket = {}
        rules = deepcopy(self.rules)
        while rules:
            for position, values in enumerate(values_per_position):
                possible_rules = [
                    rule
                    for rule, accepted_values in rules.items()
                    if values.issubset(accepted_values)
                ]
                if len(possible_rules) == 1:
                    my_ticket[possible_rules[0]] = self.me[position]
                    del rules[possible_rules[0]]
        return prod(v for rule, v in my_ticket.items() if rule.startswith("departure"))


solutions = (18227, 2355350878831)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
