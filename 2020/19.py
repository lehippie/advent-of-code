"""Day 19: Monster Messages."""

import re
from aoc.puzzle import Puzzle


def rule_pattern(n, rules):
    """Iteratively replace numbers in rule <n> by their content
    until there are only "a", "b" and matching characters.
    """
    pattern = rules[n]
    while any(char not in "ab |()+" for char in pattern):
        for i in set(re.findall(r"\d+", pattern)):
            pattern = re.sub(rf"\b{i}\b", rules[i], pattern)
    return "^" + pattern.replace(" ", "") + "$"


class Today(Puzzle):
    def parser(self):
        idx = self.input.index("")
        self.rules = {}
        for line in self.input[:idx]:
            n, rule = line.split(": ")
            self.rules[n] = f"({rule})" if "|" in rule else rule.replace('"', "")
        self.messages = self.input[idx + 1 :]

    def part_one(self):
        rule = re.compile(rule_pattern("0", self.rules))
        return sum(1 for m in self.messages if rule.match(m))

    def part_two(self):
        """Rule 8 is replaced by rule 42 with regex modifier "+".
        Rule 11 transforms into any number of rule 42 followed by
        the same number of rule 31. Thus we add new possibilities
        for rule 11 in the form of 42{n} 31{n}.
        The length of the longest message is the upper limit for n,
        divided by 2 because there are pattern 42 and 31.
        """
        new_rules = self.rules.copy()
        new_rules["8"] = "(42+)"
        M = max(len(m) for m in self.messages)
        new_rules["11"] = f"({'|'.join('42 '*i + '31 '*i for i in range(1, M//2))})"
        rule = re.compile(rule_pattern("0", new_rules))
        return sum(1 for m in self.messages if rule.match(m))


solutions = (239, 405)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
