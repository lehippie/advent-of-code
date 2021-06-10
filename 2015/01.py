"""Day 1: Not Quite Lisp."""

from collections import Counter

from aoc.puzzle import Puzzle


class TodayPuzzle(Puzzle):
    def part_one(self):
        parentheses = Counter(self.input)
        return parentheses["("] - parentheses[")"]

    def part_two(self):
        floor = 0
        for i, p in enumerate(self.input):
            floor = (floor + 1) if p == "(" else (floor - 1)
            if floor == -1:
                break
        return i + 1


if __name__ == "__main__":
    TodayPuzzle(solutions=(74, 1795)).solve()
