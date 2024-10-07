"""Day 10: Syntax Scoring."""

import re
from aoc.puzzle import Puzzle


LEGAL_PAIRS = r"\(\)|\[\]|{}|<>"
CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
SYNTAX_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def check_syntax(line):
    """Analyze a line and return its status and score.

    First, all legal pairs are removed iteratively. Then, if a closing
    character remains, it means it's not correctly preceded by its
    opening counterpart. The first illegal closer is considered to
    calculate the score.
    Incomplete lines are corrected by following the remaining openers
    from right to left.
    """
    while re.search(LEGAL_PAIRS, line):
        line = re.sub(LEGAL_PAIRS, "", line)
    if set(line).intersection(CLOSERS.values()):
        status = "corrupted"
        score = SYNTAX_POINTS[next(c for c in line if c in CLOSERS.values())]
    else:
        status = "incomplete"
        score = 0
        for character in (CLOSERS[c] for c in line[::-1]):
            score = 5 * score + AUTOCOMPLETE_POINTS[character]
    return status, score


class Today(Puzzle):
    def part_one(self):
        self.lines = [check_syntax(line) for line in self.input]
        return sum(score for status, score in self.lines if status == "corrupted")

    def part_two(self):
        scores = [score for status, score in self.lines if status == "incomplete"]
        return sorted(scores)[(len(scores) - 1) // 2]


if __name__ == "__main__":
    Today().solve()
