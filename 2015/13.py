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


class Today(Puzzle):
    def parser(self):
        self.graph = defaultdict(dict)
        for line in self.input:
            words = line.split()
            if "gain" in line:
                self.graph[words[0]][words[-1][:-1]] = int(words[3])
            else:
                self.graph[words[0]][words[-1][:-1]] = -int(words[3])

    def part_one(self):
        table = DinnerTable(self.graph)
        return max(table.arrangements.values())

    def part_two(self):
        input_with_me = deepcopy(self.graph)
        for attendee in self.graph:
            input_with_me[attendee]["me"] = 0
            input_with_me["me"][attendee] = 0
        table = DinnerTable(input_with_me)
        return max(table.arrangements.values())


solutions = (664, 640)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
