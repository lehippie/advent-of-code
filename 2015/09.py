"""Day 9: All in a Single Night."""

from collections import defaultdict
from itertools import permutations
from aoc.puzzle import Puzzle


class Locations:
    def __init__(self, graph: dict):
        self.graph = graph
        self.routes = {}
        for route in permutations(self.graph.keys()):
            self.routes[" -> ".join(route)] = sum(
                self.graph[a][b] for a, b in zip(route[:-1], route[1:])
            )


class Today(Puzzle):
    def parser(self):
        self.graph = defaultdict(dict)
        for line in self.input:
            loc1, _, loc2, _, distance = line.split()
            self.graph[loc1][loc2] = int(distance)
            self.graph[loc2][loc1] = int(distance)

    def part_one(self):
        locations = Locations(self.graph)
        return min(locations.routes.values())

    def part_two(self):
        locations = Locations(self.graph)
        return max(locations.routes.values())


solutions = (251, 898)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
