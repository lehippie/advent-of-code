"""Day 7: Handy Haversacks."""

import re
from pathlib import Path
from typing import final


INPUT_FILE = "luggage_rules.txt"
MY_BAG = "shiny gold"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    data = {}
    with filepath.open() as f:
        for line in f:
            bag, inside = line.split(" bags contain ")
            inside = re.findall(r"(\d+)\s([a-z]+\s[a-z]+)\sbag", inside)
            inside = {k: int(v) for v, k in inside}
            data[bag] = inside
    return data


# --- Part One ---

def containers(rules, bag):
    """Return a set of containers for <bag>."""
    return {r for r in rules if bag in rules[r]}


def outermost_bags(rules, bag=MY_BAG):
    """Return bags in <rules> that can contain <bag>."""
    bags = containers(rules, bag)
    while True:
        previous_bags = bags.copy()
        for b in previous_bags:
            bags.update(containers(rules, b))
        if bags == previous_bags:
            return bags


def part_one(rules):
    """Part One solution."""
    containers_count = len(outermost_bags(rules))
    print(f"{containers_count} bags can contain at least one {MY_BAG} bag.")
    assert containers_count == 151


# --- Part Two ---

def inside_bags(rules, bag=MY_BAG):
    """Return required bags inside <bag>."""
    insides = {}
    bags_queue = list(rules[bag].items())
    while bags_queue:
        bag, quantity = bags_queue.pop(0)
        insides[bag] = insides.get(bag, 0) + quantity
        bags_queue.extend((b, q * quantity) for b, q in rules[bag].items())
    return insides


def part_two(rules):
    """Part Two solution."""
    insides_count = sum(inside_bags(rules).values())
    print(f"{insides_count} bags are required inside a {MY_BAG} bag.")
    assert insides_count == 41559


# --- Tests ---

def tests():
    # Part One
    test_rules = load_input("test_input_01.txt")
    assert len(outermost_bags(test_rules)) == 4
    # Part Two
    assert sum(inside_bags(test_rules).values()) == 32
    test_rules = load_input("test_input_02.txt")
    assert sum(inside_bags(test_rules).values()) == 126


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
