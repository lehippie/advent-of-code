"""Day 12: Passage Pathing."""

from collections import defaultdict
from aoc.puzzle import Puzzle


class Puzzle12(Puzzle):
    def parser(self):
        self.caves = defaultdict(list)
        for line in self.input:
            ca, cb = line.split("-")
            self.caves[ca].append(cb)
            self.caves[cb].append(ca)

    def part_one(self):
        paths_count = 0
        exploration = [["start"]]
        while exploration:
            path = exploration.pop(0)
            for cave in self.caves[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    exploration.append(path + [cave])
        return paths_count

    def part_two(self):
        paths_count = 0
        exploration = [(["start"], True)]
        while exploration:
            path, twice_small_allowed = exploration.pop(0)
            for cave in self.caves[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    exploration.append((path + [cave], twice_small_allowed))
                elif twice_small_allowed and cave != "start":
                    exploration.append((path + [cave], False))
        return paths_count


if __name__ == "__main__":
    Puzzle12(solutions=(5254, 149385)).solve()
