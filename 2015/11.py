"""Day 11: Corporate Policy."""

import re
from string import ascii_lowercase
from aoc.puzzle import Puzzle


STRAIGHTS = [ascii_lowercase[k : k + 3] for k in range(len(ascii_lowercase) - 2)]
FORBIDDEN = "iol"
DOUBLES = re.compile(r"([a-z])\1")


def next_letter(letter):
    """Return next letter in alphabetical order.

    Wraps to "a" if "z" if given. To accelerate validity
    check, letters i, o and l are skipped.
    """
    if letter == "z":
        return "a"
    if letter in FORBIDDEN:
        return chr(ord(letter) + 2)
    return chr(ord(letter) + 1)


def increment(password):
    pwd = password[:-1] + next_letter(password[-1])
    if pwd[-1] == "a":
        pwd = increment(pwd[:-1]) + pwd[-1]
    return pwd


def is_valid(password):
    """Check password validity.

    Forbidden letters are still checked here in case there
    are some in starting password.
    """
    if not any(straight in password for straight in STRAIGHTS):
        return False
    if any(letter in password for letter in FORBIDDEN):
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
        pwd = increment(self.pwd)
        while not is_valid(pwd):
            pwd = increment(pwd)
        return pwd


if __name__ == "__main__":
    Today().solve()
