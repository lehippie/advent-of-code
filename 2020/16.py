"""Day 16: Ticket Translation."""

import re
from itertools import chain
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.rules = {}
        for line in self.input[: self.input.index("")]:
            field, ranges = line.rstrip().split(": ")
            ranges = re.findall(r"(\d+)-(\d+)", ranges)
            self.rules[field] = set(
                chain(*(range(int(r1), int(r2) + 1) for r1, r2 in ranges))
            )

        idx = self.input.index("your ticket:")
        self.my_ticket = list(map(int, self.input[idx + 1].split(",")))

        idx = self.input.index("nearby tickets:")
        self.nearby = [list(map(int, l.split(","))) for l in self.input[idx + 1 :]]

    def part_one(self):
        """While getting the error rate, we filter invalid tickets."""
        all_values = set.union(*self.rules.values())
        error_rate = 0
        self.valids = []
        for ticket in self.nearby:
            errors = [value for value in ticket if value not in all_values]
            if errors:
                error_rate += sum(errors)
            else:
                self.valids.append(ticket)
        return error_rate

    def part_two(self):
        """Sets of values per positions are compared to the rules to
        find fields that have only one possibility. We iterate over
        positions by removing found fields to reconstruct our ticket.
        """
        ticket = {}
        values_per_position = [set(v) for v in zip(*self.valids)]
        fields = set(self.rules)
        while fields:
            for position, values in enumerate(values_per_position):
                possible_fields = [f for f in fields if values.issubset(self.rules[f])]
                if len(possible_fields) == 1:
                    ticket[possible_fields[0]] = self.my_ticket[position]
                    fields.remove(possible_fields[0])
        return prod(v for f, v in ticket.items() if f.startswith("departure"))


solutions = (18227, 2355350878831)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
