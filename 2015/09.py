"""Day 9: All in a Single Night."""

from collections import defaultdict
from itertools import permutations
from aoc.puzzle import Puzzle


def calculate_distances(graph):
    routes = {}
    for locations in permutations(graph):
        routes[" -> ".join(locations)] = sum(
            graph[a][b] for a, b in zip(locations, locations[1:])
        )
    return routes


class Today(Puzzle):
    def parser(self):
        self.graph = defaultdict(dict)
        for line in self.input:
            loc1, _, loc2, _, distance = line.split()
            self.graph[loc1][loc2] = int(distance)
            self.graph[loc2][loc1] = int(distance)

    def part_one(self):
        self.routes = calculate_distances(self.graph)
        return min(self.routes.values())

    def part_two(self):
        return max(self.routes.values())


if __name__ == "__main__":
    Today().solve()
