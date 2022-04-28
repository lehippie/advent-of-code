"""Day 11: Corporate Policy."""

import re
from string import ascii_lowercase
from aoc.puzzle import Puzzle


DOUBLES = re.compile(r"(.)\1")
STRAIGHTS = [ascii_lowercase[k : k + 3] for k in range(len(ascii_lowercase) - 2)]


def next_letter(letter):
    if letter in "abcdefgijlmopqrstuvwxy":
        return chr(ord(letter) + 1)
    if letter in "hkn":
        return chr(ord(letter) + 2)
    if letter == "z":
        return "a"
    raise IOError(f"Invalid lower case letter '{letter}'")


def increment(password):
    pwd = list(password)
    pwd[-1] = next_letter(pwd[-1])
    if pwd[-1] == "a":
        pwd = list(increment("".join(pwd[:-1]))) + [pwd[-1]]
    return "".join(pwd)


def is_valid(password):
    if not any(straight in password for straight in STRAIGHTS):
        return False
    if any(letter in password for letter in "ilo"):
        return False
    if len(set(DOUBLES.findall(password))) < 2:
        return False
    return True


class Today(Puzzle):
    def part_one(self):
        self.pwd = increment(self.input)
        while not is_valid(self.pwd):
            self.pwd = increment(self.pwd)
        return self.pwd

    def part_two(self):
        password = increment(self.pwd)
        while not is_valid(password):
            password = increment(password)
        return password


solutions = ("hepxxyzz", "heqaabcc")

if __name__ == "__main__":
    Today(solutions=solutions).solve()
