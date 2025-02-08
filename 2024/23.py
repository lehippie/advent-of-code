"""--- Day 23: LAN Party ---"""

from collections import defaultdict
from itertools import combinations, product
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.connect = defaultdict(set)
        for link in self.input:
            a, b = link.split("-")
            self.connect[a].add(b)
            self.connect[b].add(a)

    def part_one(self):
        count = 0
        self.triplets = set()
        for a, b, c in combinations(self.connect, r=3):
            if a in self.connect[b] and a in self.connect[c] and b in self.connect[c]:
                self.triplets.add(frozenset((a, b, c)))
                if "t" in {a[0], b[0], c[0]}:
                    count += 1
        return count

    def part_two(self):
        """From triplets calculated in part one, try adding new
        computers to grow them until there is only one left.
        """
        lans = self.triplets
        while len(lans) > 1:
            bigger_lans = set()
            for lan, computer in product(lans, self.connect):
                if self.connect[computer].intersection(lan) == lan:
                    bigger_lans.add(frozenset(lan.union((computer,))))
            lans = bigger_lans
        return ",".join(sorted(lans.pop()))


if __name__ == "__main__":
    Today().solve()
