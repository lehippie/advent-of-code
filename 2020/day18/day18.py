"""Puzzle."""

import re
from pathlib import Path


INPUT_FILE = "expressions.txt"
PARENTHESE = re.compile(r"\(\d+(?:\s[\+\*]\s\d+)+\)")
ADDITION = re.compile(r"\d+(?:\s\+\s\d+)+")


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.rstrip() for line in f]
    return data


# --- Part One ---

def left2right(expression: str):
    """Left-to-right calculation of <expression> without prentheses."""
    expression = expression.split(" ")
    result = int(expression.pop(0))
    while expression:
        operation = expression.pop(0)
        value = int(expression.pop(0))
        if operation == "+":
            result += value
        elif operation == "*":
            result *= value
    return str(result)


def evaluate(expression):
    while parentheses := PARENTHESE.findall(expression):
        for p in parentheses:
            expression = expression.replace(p, left2right(p[1:-1]))
    return int(left2right(expression))


def part_one(expressions):
    return sum(evaluate(exp) for exp in expressions)


# --- Part Two ---

def precedence(expression: str):
    """Calculation an expression without prentheses with precedence."""
    while additions := ADDITION.findall(expression):
        for a in additions:
            expression = expression.replace(a, left2right(a))
    return left2right(expression)


def advanced_evaluate(expression):
    while parentheses := PARENTHESE.findall(expression):
        for p in parentheses:
            expression = expression.replace(p, precedence(p[1:-1]))
    return int(precedence(expression))


def part_two(expressions):
    return sum(advanced_evaluate(exp) for exp in expressions)


# --- Tests & Run ---

def tests():
    # Part One
    tests = load_input("test.txt")
    results = [evaluate(t) for t in tests]
    assert results == [71, 51, 26, 437, 12240, 13632]
    # Part Two
    results = [advanced_evaluate(t) for t in tests]
    assert results == [231, 51, 46, 1445, 669060, 23340]


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    result_one = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 6923486965641

    result_two = part_two(puzzle_input)
    print(f"Part Two answer: {result_two}")
    assert result_two == 70722650566361
