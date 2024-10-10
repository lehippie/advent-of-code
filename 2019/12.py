"""--- Day 12: The N-Body Problem ---"""

import re
from itertools import combinations
from math import lcm
from aoc.puzzle import Puzzle


class MotionSimulator:
    def __init__(self, moons):
        self.moons = [m.copy() for m in moons]
        self.step = 0

    def run_step(self):
        for m1, m2 in combinations(self.moons, 2):
            for p in range(3):
                if m1[p] < m2[p]:
                    m1[p + 3] += 1
                    m2[p + 3] += -1
                elif m1[p] > m2[p]:
                    m1[p + 3] += -1
                    m2[p + 3] += 1
        for moon in self.moons:
            for p in range(3):
                moon[p] += moon[p + 3]
        self.step += 1


class Today(Puzzle):
    def parser(self):
        self.moons = [
            [int(p) for p in re.findall(r"-?[0-9]+", position)] + [0, 0, 0]
            for position in self.input
        ]

    def part_one(self):
        sim = MotionSimulator(self.moons)
        while sim.step != 1000:
            sim.run_step()
        return sum(
            sum(map(abs, moon[:3])) * sum(map(abs, moon[3:])) for moon in sim.moons
        )

    def part_two(self):
        """To speed up the search we can calculate the lcm of the cycles
        of independant systems. Here, the independance exists between the
        different axes.
        Also, as the step function is bijective (one state is accessible
        by only a unique previous state), the starting position is part of
        the cycle so we don't have to keep track of the full history.
        """
        sim = MotionSimulator(self.moons)
        initial_states = [sum((m[p::3] for m in self.moons), []) for p in range(3)]
        cycles = [None for _ in range(3)]
        while any(c is None for c in cycles):
            sim.run_step()
            states = (sum((m[p::3] for m in sim.moons), []) for p in range(3))
            for c, (state, init) in enumerate(zip(states, initial_states)):
                if cycles[c] is None and state == init:
                    cycles[c] = sim.step
        return lcm(*cycles)


if __name__ == "__main__":
    Today().solve()
