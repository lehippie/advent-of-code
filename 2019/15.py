"""--- Day 15: Oxygen System ---"""

from collections import deque
from copy import deepcopy
from aoc.puzzle import Puzzle
from intcode import Intcode

MOVE = {1: 1j, 2: -1j, 3: -1, 4: 1}
TRAVERSABLE = {1, 2}


class Droid:
    def __init__(self, program):
        self.brain = Intcode(program)
        self.position = 0
        self.steps = 0


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        """Explore the sealed part of the ship with BFS."""
        droids = deque([Droid(self.program)])
        self.open = {0}
        self.walls = set()
        while droids:
            droid = droids.popleft()
            for command, move in MOVE.items():
                destination = droid.position + move
                if destination in self.open.union(self.walls):
                    continue
                d = deepcopy(droid)
                reply = d.brain.run(command)
                if reply == 0:
                    self.walls.add(destination)
                elif reply in TRAVERSABLE:
                    self.open.add(destination)
                    d.position += move
                    d.steps += 1
                    droids.append(d)
                    if reply == 2:
                        self.oxygen_system = d.position
                        steps_to_oxygen_system = d.steps
        return steps_to_oxygen_system

    def part_two(self):
        oxygenated = {self.oxygen_system}
        frontier = {self.oxygen_system}
        time = 0
        while oxygenated != self.open:
            spread = set()
            for location in frontier:
                near = self.open.intersection(location + move for move in MOVE.values())
                spread.update(near.difference(oxygenated))
                oxygenated.update(spread)
            frontier = spread
            time += 1
        return time


if __name__ == "__main__":
    Today().solve()
