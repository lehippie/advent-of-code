"""Day 13: Knights of the Dinner Table."""

from collections import defaultdict
from itertools import permutations

from aoc.puzzle import Puzzle


def parser(puzzle_input):
    graph = defaultdict(dict)
    for line in puzzle_input:
        words = line.strip().split()
        if "gain" in line:
            graph[words[0]][words[-1][:-1]] = int(words[3])
        else:
            graph[words[0]][words[-1][:-1]] = -int(words[3])
    return graph


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


class TodayPuzzle(Puzzle):
    def part_one(self):
        table = DinnerTable(self.input)
        return max(table.arrangements.values())

    def part_two(self):
        self.input_with_me = self.input.copy()
        for attendee in self.input:
            self.input_with_me[attendee]["me"] = 0
            self.input_with_me["me"][attendee] = 0
        table = DinnerTable(self.input_with_me)
        return max(table.arrangements.values())


if __name__ == "__main__":
    TodayPuzzle(parser=parser, solutions=(664, 640)).solve()
