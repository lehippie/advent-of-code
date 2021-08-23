"""Day 9: All in a Single Night."""

from collections import defaultdict
from itertools import permutations

from aoc.puzzle import Puzzle


def parser(puzzle_input):
    graph = defaultdict(dict)
    for line in puzzle_input:
        loc1, _, loc2, _, distance = line.split()
        graph[loc1][loc2] = int(distance)
        graph[loc2][loc1] = int(distance)
    return graph


class Locations:
    def __init__(self, graph: dict):
        self.graph = graph
        self.routes = {}
        for route in permutations(self.graph.keys()):
            self.routes[" -> ".join(route)] = sum(
                self.graph[a][b] for a, b in zip(route[:-1], route[1:])
            )


class TodayPuzzle(Puzzle):
    def part_one(self):
        self.locations = Locations(self.input)
        return min(self.locations.routes.values())

    def part_two(self):
        return max(self.locations.routes.values())


if __name__ == "__main__":
    TodayPuzzle(parser=parser, solutions=(251, 898)).solve()
