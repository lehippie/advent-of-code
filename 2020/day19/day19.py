"""Day 19: Monster Messages."""

import re
from pathlib import Path


INPUT_FILE = "messages.txt"

def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        rules = {}
        while (line := f.readline()) != "\n":
            rule_id, rule = line.strip().split(": ")
            rules[int(rule_id)] = rule
        rules = {rid: f"({r})" if "|" in r else r.replace('"', "")
                 for rid, r in rules.items()}
        messages = [line.strip() for line in f]
    return rules, messages


# --- Part One ---

def reduce_rule(rules, rule_id):
    rule = rules[rule_id]
    while not all(c in "ab (|)" for c in rule):
        for i in set(re.findall(r"\d+", rule)):
            rule = re.sub(r"\b" + i + r"\b", rules[int(i)], rule)
    return "^" + rule.replace(" ", "") + "$"


def part_one(rules, messages):
    rule = re.compile(reduce_rule(rules, 0))
    good_messages = [m for m in messages if rule.match(m)]
    return good_messages


# --- Part Two ---

def part_two(rules, messages):
    maxlen = max(len(m) for m in messages)
    rules[8] = f"({'|'.join('42 '*i for i in range(1, maxlen))})"
    rules[11] = f"({'|'.join('42 '*i + '31 '*i for i in range(1, maxlen//2))})"
    return part_one(rules, messages)


# --- Tests & Run ---

def tests():
    # Part One
    test = load_input("test.txt")
    assert len(part_one(*test)) == 2
    # Part Two
    test = load_input("test2.txt")
    assert len(part_one(*test)) == 3
    assert len(part_two(*test)) == 12


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    result_one = len(part_one(*puzzle_input))
    print(f"Part One answer: {result_one}")
    assert result_one == 239

    result_two = len(part_two(*puzzle_input))
    print(f"Part Two answer: {result_two}")
    assert result_two == 405
