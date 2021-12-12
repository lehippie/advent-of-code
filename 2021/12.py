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
        paths = []
        exploration = [["start"]]
        while exploration:
            path = exploration.pop(0)
            if path[-1] == "end":
                paths.append(path)
                continue
            for connection in self.caves[path[-1]]:
                if connection not in path or connection.isupper():
                    exploration.append(path + [connection])
        return len(paths)

    def part_two(self):
        paths = []
        exploration = [(["start"], True)]
        while exploration:
            path, small_allowed_twice = exploration.pop(0)
            if path[-1] == "end":
                paths.append(path)
                continue
            for connection in self.caves[path[-1]]:
                if connection not in path or connection.isupper():
                    exploration.append((path + [connection], small_allowed_twice))
                elif small_allowed_twice and connection != "start":
                    exploration.append((path + [connection], False))
        return len(paths)


if __name__ == "__main__":
    Puzzle12(solutions=(5254, 149385)).solve()
