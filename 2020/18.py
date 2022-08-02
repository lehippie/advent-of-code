"""Day 18: Operation Order."""

import re
from aoc.puzzle import Puzzle


PARENTHESE = re.compile(r"\(\d+(?: [\+\*] \d+)+\)")
ADDITION = re.compile(r"\d+(?: \+ \d+)+")


def left2right(expression: str):
    """Calculation with left-to-right precedence."""
    expression = expression.split(" ")
    result = int(expression[0])
    for op, val in zip(expression[1::2], expression[2::2]):
        if op == "+":
            result += int(val)
        elif op == "*":
            result *= int(val)
    return str(result)


def add_before_mult(expression: str):
    """Calculation with addition before multiplication."""
    while additions := ADDITION.findall(expression):
        for a in additions:
            expression = expression.replace(a, left2right(a))
    return left2right(expression)


def evaluate(expression, method=left2right):
    while parentheses := PARENTHESE.findall(expression):
        for p in parentheses:
            expression = expression.replace(p, method(p[1:-1]))
    return int(method(expression))


class Today(Puzzle):
    def part_one(self):
        return sum(evaluate(exp) for exp in self.input)

    def part_two(self):
        return sum(evaluate(exp, add_before_mult) for exp in self.input)


solutions = (6923486965641, 70722650566361)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
