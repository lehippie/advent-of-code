"""Day 13: Knights of the Dinner Table."""

from collections import defaultdict
from copy import deepcopy
from itertools import permutations
from aoc.puzzle import Puzzle


class DinnerTable:
    def __init__(self, graph: dict):
        self.graph = graph
        self.attendees = list(self.graph.keys())
        self.n_attendees = len(self.attendees)
        self.arrangements = {
            p: 0 for p in permutations(self.attendees) if p[0] == self.attendees[0]
        }
        for arrangement in self.arrangements:
            for i, attendee in enumerate(arrangement):
                right = arrangement[(i + 1) % self.n_attendees]
                left = arrangement[i - 1]
                self.arrangements[arrangement] += self.graph[attendee][right]
                self.arrangements[arrangement] += self.graph[attendee][left]


class Puzzle13(Puzzle):
    def parser(self):
        graph = defaultdict(dict)
        for line in self.input:
            words = line.split()
            if "gain" in line:
                graph[words[0]][words[-1][:-1]] = int(words[3])
            else:
                graph[words[0]][words[-1][:-1]] = -int(words[3])
        return graph

    def part_one(self):
        table = DinnerTable(self.input)
        return max(table.arrangements.values())

    def part_two(self):
        input_with_me = deepcopy(self.input)
        for attendee in self.input:
            input_with_me[attendee]["me"] = 0
            input_with_me["me"][attendee] = 0
        table = DinnerTable(input_with_me)
        return max(table.arrangements.values())


if __name__ == "__main__":
    Puzzle13(solutions=(664, 640)).solve()
