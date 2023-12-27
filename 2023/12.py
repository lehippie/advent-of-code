"""--- Day 12: Hot Springs ---"""

import re

from functools import lru_cache
from aoc.puzzle import Puzzle


@lru_cache
def pattern(n):
    """Create a regex pattern to detect overlapping groups of <n>
    consecutive ? and # that are neither preceded nor followed by
    other #s.
    """
    return re.compile(rf"(?<!#)(?=[\?#]{{{n}}})(?![\?#]{{{n}}}#)")


@lru_cache
def arrangements(row, groups):
    """Recursive function that place first group and call itself on
    the remaining row and groups. Search is stopped if we skip a # or
    if the rest of ? and # is less than total of springs to place.
    """
    if not groups:
        return 0 if "#" in row else 1
    out = 0
    for match in pattern(groups[0]).finditer(row):
        if "#" in row[: match.start()]:
            break
        remaining = row[match.start() + groups[0] + 1 :].strip(".")
        if remaining.count("#") + remaining.count("?") < sum(groups[1:]):
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
        """Consecutive dots are fused and leading/trailing ones are
        removed to help converge similar rows in the lru_cache.
        """
        rows = [re.sub(r"\.+", ".", s.strip(".")) for s in self.rows]
        return sum(arrangements(row, groups) for row, groups in zip(rows, self.groups))

    def part_two(self):
        counts = 0
        for row, groups in zip(self.rows, self.groups):
            r = re.sub(r"\.+", ".", "?".join(row for _ in range(5)).strip("."))
            g = []
            for _ in range(5):
                g.extend(groups)
            counts += arrangements(r, tuple(g))
        return counts


if __name__ == "__main__":
    Today().solve()
