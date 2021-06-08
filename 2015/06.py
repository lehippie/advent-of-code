"""Day 6: Probably a Fire Hazard."""

from aoc.puzzle import Puzzle

import numpy as np


def line_parser(line):
    words = line.split(" ")
    if words[0] == "turn":
        words.pop(0)
    xmin, ymin = map(int, words[1].split(","))
    xmax, ymax = map(lambda x: int(x) + 1, words[3].split(","))
    return (words[0], xmin, xmax, ymin, ymax)


class Lights:
    def __init__(self, shape=(1000, 1000)):
        self.grid = np.zeros(shape, dtype=int)

    @property
    def brightness(self):
        return self.grid.sum()


class TodayPuzzle(Puzzle):
    def part_one(self):
        lights = Lights()
        for instruction, xmin, xmax, ymin, ymax in self.input:
            if instruction == "on":
                lights.grid[xmin:xmax, ymin:ymax] = 1
            elif instruction == "off":
                lights.grid[xmin:xmax, ymin:ymax] = 0
            elif instruction == "toggle":
                lights.grid[xmin:xmax, ymin:ymax] += 1
                lights.grid[xmin:xmax, ymin:ymax] %= 2
        return lights.brightness

    def part_two(self):
        lights = Lights()
        for instruction, xmin, xmax, ymin, ymax in self.input:
            if instruction == "on":
                lights.grid[xmin:xmax, ymin:ymax] += 1
            elif instruction == "off":
                lights.grid[xmin:xmax, ymin:ymax] -= 1
                lights.grid[lights.grid < 0] = 0
            elif instruction == "toggle":
                lights.grid[xmin:xmax, ymin:ymax] += 2
        return lights.brightness


if __name__ == "__main__":
    puzzle = TodayPuzzle(
        line_parser=line_parser,
        tests={
            "part_one": [
                (["turn on 0,0 through 999,999"], 1000000),
                (["turn on 0,0 through 0,0", "toggle 0,0 through 999,0"], 999),
            ],
            "part_two": [
                (["turn on 0,0 through 0,0"], 1),
                (["toggle 0,0 through 999,999"], 2000000),
            ],
        },
        solution_one=377891,
        solution_two=14110788,
    )
    if puzzle.test():
        puzzle.solve()
