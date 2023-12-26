"""--- Day 25: Snowverload ---"""

from collections import defaultdict
from aoc.puzzle import Puzzle


# Thanks graphviz!
EDGES = [set(["jxd", "bbz"]), set(["glz", "mxd"]), set(["clb", "brd"])]


class Today(Puzzle):
    def parser(self):
        self.graph = defaultdict(list)
        for line in self.input:
            a, bs = line.split(": ")
            for b in bs.split():
                if set([a, b]) in EDGES:
                    continue  # TODO: replace with proper algorithm that detect these
                self.graph[a].append(b)
                self.graph[b].append(a)

    def part_one(self):
        frontier = [next(key for key in self.graph)]
        reached = set(frontier)
        while frontier:
            component = frontier.pop()
            for connected in self.graph[component]:
                if connected not in reached:
                    reached.add(connected)
                    frontier.append(connected)
        return len(reached) * (len(self.graph) - len(reached))


solutions = 518391

if __name__ == "__main__":
    Today(solutions=solutions).solve()
