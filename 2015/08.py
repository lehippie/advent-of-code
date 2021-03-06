"""Day 8: Matchsticks."""

from collections import Counter

from aoc.puzzle import Puzzle


def char_len(string):
    return len(string[1:-1].encode().decode("unicode_escape"))


def encoded_len(string):
    chars_count = Counter(string)
    return len(string) + chars_count['"'] + chars_count["\\"] + 2


class TodayPuzzle(Puzzle):
    def part_one(self):
        return sum(len(s) - char_len(s) for s in self.input)

    def part_two(self):
        return sum(encoded_len(s) - len(s) for s in self.input)


if __name__ == "__main__":
    TodayPuzzle(solutions=(1371, 2117)).solve()
