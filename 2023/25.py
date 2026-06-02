"""--- Day 25: Snowverload ---"""

from collections import defaultdict
from pathlib import Path
from aoc.puzzle import Puzzle

# Thanks graphviz!
EDGES = [set(["jxd", "bbz"]), set(["glz", "mxd"]), set(["clb", "brd"])]


class Today(Puzzle):
    def parser(self):
        self.graph = defaultdict(list)
        for line in self.input:
            a, bs = line.split(": ")
            for b in bs.split():
                # Uncomment the 2 following lines to create graphviz data
                # with open(Path(__file__).parent / "graph.txt", "a") as f:
                #     f.write(f"    {a} -- {b};\n")
                self.graph[a].append(b)
                self.graph[b].append(a)

    def part_one(self):
        frontier = [next(key for key in self.graph)]
        reached = set(frontier)
        while frontier:
            component = frontier.pop()
            for connected in self.graph[component]:
                if set([component, connected]) in EDGES:
                    continue  # TODO: code an algorithm that detect these
                if connected not in reached:
                    reached.add(connected)
                    frontier.append(connected)
        return len(reached) * (len(self.graph) - len(reached))


if __name__ == "__main__":
    Today().solve()
