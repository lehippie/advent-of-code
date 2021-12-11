"""Day 10: Syntax Scoring."""

import re
from collections import Counter
from aoc.puzzle import Puzzle


MINI_CHUNKS = r"\(\)|\[\]|{}|<>"
CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
SYNTAX_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


class Line:
    def __init__(self, line):
        self.line = line
        self.status = None
        self.err = None
        self.analyze()

    def analyze(self):
        while re.search(MINI_CHUNKS, self.line):
            self.line = re.sub(MINI_CHUNKS, "", self.line)
        if set(self.line).intersection(CLOSERS.values()):
            self.status = "corrupted"
            self.err = next(char for char in self.line if char in CLOSERS.values())
        else:
            self.status = "incomplete"
            self.err = "".join(CLOSERS[char] for char in self.line[::-1])


def completion_score(completion):
    score = 0
    for char in completion:
        score = 5 * score + COMPLETION_SCORES[char]
    return score


class Puzzle10(Puzzle):
    def part_one(self):
        lines = [Line(line) for line in self.input]
        corruptions = Counter(line.err for line in lines if line.status == "corrupted")
        return sum(SYNTAX_SCORES[char] * corruptions[char] for char in corruptions)

    def part_two(self):
        lines = [Line(line) for line in self.input]
        scores = [
            completion_score(line.err) for line in lines if line.status == "incomplete"
        ]
        return sorted(scores)[(len(scores) - 1) // 2]


if __name__ == "__main__":
    Puzzle10(solutions=(319233, 1118976874)).solve()
