"""Day 2: Password Philosophy."""

from collections import Counter
from aoc.puzzle import Puzzle


def is_valid(password_line, policy="sled"):
    values, letter, password = password_line.split(" ")
    v1, v2 = [int(v) for v in values.split("-")]
    letter = letter[0]
    if policy == "sled":
        return v1 <= Counter(password)[letter] <= v2
    if policy == "toboggan":
        return (password[v1 - 1] == letter) != (password[v2 - 1] == letter)


class Today(Puzzle):
    def part_one(self):
        return sum(is_valid(pwd) for pwd in self.input)

    def part_two(self):
        return sum(is_valid(pwd, "toboggan") for pwd in self.input)


solutions = (628, 705)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
