"""Day 23: Unstable Diffusion."""

from collections import defaultdict
from itertools import product
from math import prod
from aoc.puzzle import Puzzle


NORTH = [-1j, -1 - 1j, 1 - 1j]
SOUTH = [1j, -1 + 1j, 1 + 1j]
WEST = [-1, -1 - 1j, -1 + 1j]
EAST = [1, 1 - 1j, 1 + 1j]


class ElvesProcess:
    def __init__(self, elves: set):
        self.elves = elves.copy()
        self.checks = [NORTH, SOUTH, WEST, EAST]
        self.stable = False

    def adjacents(self, elf):
        elf = int(elf.real), int(elf.imag)
        for adj in product(*((p - 1, p, p + 1) for p in elf)):
            if adj != elf:
                yield adj[0] + adj[1] * 1j

    def do_steps(self, n):
        for _ in range(n):
            elves = set()
            movers = defaultdict(list)
            for elf in self.elves:
                if not self.elves.intersection(self.adjacents(elf)):
                    elves.add(elf)
                    continue
                for direction in self.checks:
                    if not self.elves.intersection((elf + d for d in direction)):
                        movers[elf + direction[0]].append(elf)
                        break
                else:
                    elves.add(elf)
            for destination, proposers in movers.items():
                if len(proposers) > 1:
                    elves.update(proposers)
                else:
                    elves.add(destination)
            if elves == self.elves:
                self.stable = True
                return
            self.elves = elves
            self.checks = self.checks[1:] + self.checks[:1]

    def empty_count(self):
        elves = [(int(elf.real), int(elf.imag)) for elf in self.elves]
        spans = [(min(e), max(e) + 1) for e in zip(*elves)]
        return prod(s[1] - s[0] for s in spans) - len(elves)

    def solve(self):
        steps = 0
        while not self.stable:
            self.do_steps(1)
            steps += 1
        return steps


class Today(Puzzle):
    def parser(self):
        self.elves = set()
        for r, row in enumerate(self.input):
            for c, col in enumerate(row):
                if col == "#":
                    self.elves.add(c + r * 1j)

    def part_one(self):
        process = ElvesProcess(self.elves)
        process.do_steps(10)
        return process.empty_count()

    def part_two(self):
        process = ElvesProcess(self.elves)
        return process.solve()


solutions = (4049, 1021)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
