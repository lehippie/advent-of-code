"""Day 18: Snailfish."""

import re
from collections import Counter
from itertools import permutations
from aoc.puzzle import Puzzle


PAIR = re.compile(r"\[\d+,\d+\]")
NUMBER_OVER_TEN = re.compile(r"\d\d+")
FIRST_NUMBER = re.compile(r"\d+")
LAST_NUMBER = re.compile(r"(\d+)[^\d]*$")


def explode(pair: re.Match):
    before = pair.string[: pair.start()]
    after = pair.string[pair.end() :]
    x, y = [int(d) for d in re.findall("\d+", pair[0])]
    if (n := LAST_NUMBER.search(before)) is not None:
        before = before[: n.start(1)] + f"{int(n[1]) + x}" + before[n.end(1) :]
    if (n := FIRST_NUMBER.search(after)) is not None:
        after = after[: n.start()] + f"{int(n[0]) + y}" + after[n.end() :]
    return before + "0" + after


def split(number: re.Match):
    before = number.string[: number.start()]
    after = number.string[number.end() :]
    n = int(number[0])
    return before + f"[{n // 2},{n - n // 2}]" + after


def reduce(number):
    """To check for explosions, the amounts of "[" and "]" characters
    present before pair are computed.

    If a number explodes, we must restart the process and resolve any
    new explosion before checking for splits.
    """
    while True:
        has_exploded = False
        for pair in PAIR.finditer(number):
            chars_before = Counter(number[: pair.start()])
            if chars_before["["] - chars_before["]"] > 3:
                number = explode(pair)
                has_exploded = True
                break
        if has_exploded:
            continue
        elif (num := NUMBER_OVER_TEN.search(number)) is not None:
            number = split(num)
        else:
            return number


class SnailfishNumber(str):
    def __add__(self, other):
        return SnailfishNumber(reduce(f"[{self},{other}]"))

    def magnitude(self):
        return eval(self.replace("[", "(3*").replace("]", "*2)").replace(",", "+"))


class Today(Puzzle):
    def part_one(self):
        number = SnailfishNumber(self.input[0])
        for n in self.input[1:]:
            number += n
        return number.magnitude()

    def part_two(self):
        numbers = list(map(SnailfishNumber, self.input))
        return max((x + y).magnitude() for x, y in permutations(numbers, 2))


solutions = (3486, 4747)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
