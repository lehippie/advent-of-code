"""--- Day 8: Haunted Wasteland ---"""

from itertools import cycle
from math import lcm
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.instructions = [int(d == "R") for d in self.input[0]]
        self.nodes = {}
        for line in self.input[2:]:
            node, links = line.split(" = ")
            self.nodes[node] = (links[1:4], links[-4:-1])

    def part_one(self):
        position = "AAA"
        step = 0
        for i in cycle(self.instructions):
            step += 1
            position = self.nodes[position][i]
            if position == "ZZZ":
                return step

    def part_two(self):
        ghosts = [n for n in self.nodes if n[-1] == "A"]
        reached = [0] * len(ghosts)
        step = 0
        for i in cycle(self.instructions):
            step += 1
            for g in range(len(ghosts)):
                if not reached[g]:
                    ghosts[g] = self.nodes[ghosts[g]][i]
                    if ghosts[g][-1] == "Z":
                        reached[g] = step
            if all(reached):
                return lcm(*reached)


if __name__ == "__main__":
    Today().solve()
