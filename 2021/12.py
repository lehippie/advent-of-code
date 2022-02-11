"""Day 12: Passage Pathing."""

from collections import defaultdict, deque
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.cave_system = defaultdict(list)
        for line in self.input:
            cave1, cave2 = line.split("-")
            self.cave_system[cave1].append(cave2)
            self.cave_system[cave2].append(cave1)

    def part_one(self):
        """Explore cave system with BFS and count paths to the end."""
        paths_count = 0
        exploration = deque([["start"]])
        while exploration:
            path = exploration.popleft()
            for cave in self.cave_system[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    exploration.append(path + [cave])
        return paths_count

    def part_two(self):
        """Adding a flag to paths to allow visiting a small cave twice."""
        paths_count = 0
        exploration = deque([(["start"], True)])
        while exploration:
            path, can_revisit_small = exploration.popleft()
            for cave in self.cave_system[path[-1]]:
                if cave == "end":
                    paths_count += 1
                elif cave not in path or cave.isupper():
                    exploration.append((path + [cave], can_revisit_small))
                elif can_revisit_small and cave != "start":
                    exploration.append((path + [cave], False))
        return paths_count


solutions = (5254, 149385)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
