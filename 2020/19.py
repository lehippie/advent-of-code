"""Day 19: Monster Messages."""

import re
from aoc.puzzle import Puzzle


def reduce_rule(rules, rule_id):
    rule = rules[rule_id]
    while not all(c in "ab (|)+" for c in rule):
        for i in set(re.findall(r"\d+", rule)):
            rule = re.sub(r"\b" + i + r"\b", rules[int(i)], rule)
    return "^" + rule.replace(" ", "") + "$"


class Puzzle19(Puzzle):
    def parser(self):
        self.rules = {}
        self.messages = []
        for k, line in enumerate(self.input):
            if not line:
                break
            rule_id, rule = line.split(": ")
            self.rules[int(rule_id)] = (
                f"({rule})" if "|" in rule else rule.replace('"', "")
            )
        self.messages = self.input[k + 1 :]

    def part_one(self):
        rule = re.compile(reduce_rule(self.rules, 0))
        return sum(1 for m in self.messages if rule.match(m))

    def part_two(self):
        maxlen = max(len(m) for m in self.messages)
        self.rules[8] = "(42+)"
        self.rules[11] = f"({'|'.join('42 '*i + '31 '*i for i in range(1, maxlen//2))})"
        return self.part_one()


if __name__ == "__main__":
    Puzzle19(solutions=(239, 405)).solve()
