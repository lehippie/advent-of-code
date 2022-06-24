"""Day 8: Matchsticks."""

from collections import Counter
from aoc.puzzle import Puzzle


def code_len(string):
    """By encoding the string to bytes and decoding it while
    escaping characters, the in-memory length is obtained.
    """
    return len(string[1:-1].encode().decode("unicode_escape"))


def encoded_len(string):
    """The encoded length is obtained by adding 2 for the
    surrounding double quotes and 1 for each double quotes and
    each backlash (stored as a double backlash in memory).
    """
    count = Counter(string)
    return len(string) + 2 + count['"'] + count["\\"]


class Today(Puzzle):
    def part_one(self):
        return sum(len(s) - code_len(s) for s in self.input)

    def part_two(self):
        return sum(encoded_len(s) - len(s) for s in self.input)


solutions = (1371, 2117)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
