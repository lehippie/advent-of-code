"""--- Day 5: Print Queue ---"""

from collections import defaultdict
from itertools import combinations
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.after = defaultdict(set)
        self.updates = []
        for line in self.input:
            if "|" in line:
                before, after = line.split("|")
                self.after[int(before)].add(int(after))
            elif "," in line:
                self.updates.append(list(map(int, line.split(","))))

    def part_one(self):
        """An update is correct if for each couple of pages, there
        is a corresponding rule."""
        self.incorrect = []
        result = 0
        for update in self.updates:
            if all(b in self.after[a] for a, b in combinations(update, r=2)):
                result += update[len(update) // 2]
            else:
                self.incorrect.append(update)
        return result

    def part_two(self):
        """The intersection of the update's pages with possible pages
        coming after is decreasing along the update, so we can use the
        size of this intersection as the key for `sorted`.
        No need to activate the `reverse` flag because we only take
        the middle page into account.
        """
        result = 0
        for update in self.incorrect:
            sort_rule = lambda page: len(self.after[page].intersection(update))
            corrected = sorted(update, key=sort_rule)
            result += corrected[len(corrected) // 2]
        return result


if __name__ == "__main__":
    Today().solve()
