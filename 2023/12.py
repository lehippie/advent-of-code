"""--- Day 12: Hot Springs ---"""

import re
from collections import Counter
from functools import lru_cache
from aoc.puzzle import Puzzle


@lru_cache
def pattern(n):
    """Create a regex pattern to detect groups of <n> ? and # that
    are not preceded nor followed by additionnal #s.
    """
    return re.compile(rf"(?<!#)(?=[\?#]{{{n}}})(?![\?#]{{{n}}}#)")


@lru_cache
def arrangements(row, groups):
    if not groups:
        return 0 if "#" in row else 1
    out = 0
    for match in pattern(groups[0]).finditer(row):
        if "#" in row[: match.start()]:
            break
        remaining = row[match.start() + groups[0] + 1 :].strip(".")
        count = Counter(remaining)
        if count["#"] + count["?"] < sum(groups[1:]):
            break
        out += arrangements(remaining, groups[1:])
    return out


class Today(Puzzle):
    def parser(self):
        self.rows = []
        self.groups = []
        for line in self.input:
            row, groups = line.split()
            self.rows.append(row)
            self.groups.append(tuple(int(g) for g in groups.split(",")))

    def part_one(self):
        rows = [re.sub(r"\.+", ".", s.strip(".")) for s in self.rows]
        return sum(arrangements(row, groups) for row, groups in zip(rows, self.groups))

    def part_two(self):
        a = 0
        for row, groups in zip(self.rows, self.groups):
            r = re.sub(r"\.+", ".", "?".join(row for _ in range(5)).strip("."))
            g = []
            [g.extend(groups) for _ in range(5)]
            a += arrangements(r, tuple(g))
        return a


solutions = (7286, 25470469710341)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
