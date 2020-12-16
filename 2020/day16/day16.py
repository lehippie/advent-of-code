"""Puzzle."""

import re
from copy import deepcopy
from math import prod
from pathlib import Path


INPUT_FILE = "tickets.txt"

def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    data = {"rules": {}, "nearby": []}
    with filepath.open() as f:
        while (line := f.readline()) != "\n":
            field, ranges = line.rstrip().split(": ")
            ranges = re.findall(r"(\d+)-(\d+)", ranges)
            data["rules"][field] = set()
            for r1, r2 in ranges:
                data["rules"][field].update(range(int(r1), int(r2) + 1))
        while not f.readline().startswith("your"):
            pass
        data["my"] = [int(v) for v in f.readline().rstrip().split(",")]
        while not f.readline().startswith("nearby"):
            pass
        for line in f:
            data["nearby"].append([int(v) for v in line.rstrip().split(",")])
    return data


# --- Part One ---

def part_one(tickets):
    # Regroup every accepted values
    accepted_values = set()
    for s in tickets["rules"].values():
        accepted_values.update(s)
    # Caculate error rate and keep only valid ones
    error_rate = 0
    valid_tickets = []
    for ticket in tickets["nearby"]:
        errors = [value for value in ticket if value not in accepted_values]
        if errors:
            error_rate += sum(errors)
        else:
            valid_tickets.append(ticket)
    tickets["nearby"] = valid_tickets
    return error_rate, tickets


# --- Part Two ---

def part_two(tickets):
    values_per_position = [set(v) for v in zip(*tickets["nearby"])]
    my_ticket = {}
    while tickets["rules"]:
        for position, values in enumerate(values_per_position):
            possible_rules = [
                rule
                for rule, accepted_values in tickets["rules"].items()
                if values.issubset(accepted_values)
            ]
            if len(possible_rules) == 1:
                my_ticket[possible_rules[0]] = tickets["my"][position]
                del tickets["rules"][possible_rules[0]]
    return my_ticket


# --- Tests & Run ---

def tests():
    # Part One
    test = load_input("test_01.txt")
    assert part_one(test)[0] == 71
    # Part Two
    test = load_input("test_02.txt")
    assert part_two(test) == {"class": 12, "row": 11, "seat": 13}


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    result_one, tickets = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 18227

    my_ticket = part_two(tickets)
    result_two = prod(
        value
        for rule, value in my_ticket.items()
        if rule.startswith("departure")
    )
    print(f"Part Two answer: {result_two}")
    assert result_two == 2355350878831
