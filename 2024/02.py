"""--- Day 2: Red-Nosed Reports ---"""

from aoc.puzzle import Puzzle


def is_safe(report):
    repsorted = sorted(report)
    diffs = [b - a for a, b in zip(repsorted, repsorted[1:])]
    if repsorted in [report, report[::-1]] and all(1 <= d <= 3 for d in diffs):
        return True
    return False


def is_tolerable(report):
    if is_safe(report):
        return True
    for k in range(len(report)):
        if is_safe(report[:k] + report[k + 1 :]):
            return True
    return False


class Today(Puzzle):
    def parser(self):
        self.reports = [list(map(int, line.split())) for line in self.input]

    def part_one(self):
        return sum(is_safe(report) for report in self.reports)

    def part_two(self):
        return sum(is_tolerable(report) for report in self.reports)


if __name__ == "__main__":
    Today().solve()
