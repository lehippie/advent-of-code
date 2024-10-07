"""Day 5: Supply Stacks."""

import re
from copy import deepcopy
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.stacks = [[] for _ in range(9)]
        self.moves = []
        for line in self.input:
            if "[" in line:
                for i, s in enumerate(range(1, len(line), 4)):
                    if line[s] != " ":
                        self.stacks[i].append(line[s])
            elif "move" in line:
                self.moves.append(list(map(int, re.findall(r"\d+", line))))
        self.stacks = [s[::-1] for s in self.stacks]

    def part_one(self):
        stacks = deepcopy(self.stacks)
        for q, f, t in self.moves:
            for _ in range(q):
                stacks[t - 1].append(stacks[f - 1].pop())
        return "".join(s[-1] for s in stacks)

    def part_two(self):
        stacks = deepcopy(self.stacks)
        for q, f, t in self.moves:
            stacks[t - 1].extend(stacks[f - 1][-q:])
            stacks[f - 1] = stacks[f - 1][:-q]
        return "".join(s[-1] for s in stacks)


if __name__ == "__main__":
    Today().solve()
