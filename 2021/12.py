"""Day 12: Passage Pathing."""

from collections import defaultdict, deque
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
        exploration = deque([deque(["start"])])
        while exploration:
            path = exploration.pop()
            for cave in self.caves[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    new_path = path.copy()
                    new_path.append(cave)
                    exploration.append(new_path)
        return paths_count

    def part_two(self):
        paths_count = 0
        exploration = deque([(deque(["start"]), True)])
        while exploration:
            path, twice_small_allowed = exploration.pop()
            for cave in self.caves[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    new_path = path.copy()
                    new_path.append(cave)
                    exploration.append((new_path, twice_small_allowed))
                elif twice_small_allowed and cave != "start":
                    new_path = path.copy()
                    new_path.append(cave)
                    exploration.append((new_path, False))
        return paths_count


if __name__ == "__main__":
    Puzzle12(solutions=(5254, 149385)).solve()
