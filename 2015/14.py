"""Day 14: Reindeer Olympics."""

import re

from aoc.puzzle import Puzzle


def parser(puzzle_line):
    name = puzzle_line.split()[0]
    stats = list(map(int, re.findall(r"\d+", puzzle_line)))
    return Reindeer(name, *stats)


class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.period = fly_time + rest_time

    def fly(self, duration):
        distance = (duration // self.period) * self.speed * self.fly_time
        distance += self.speed * min(duration % self.period, self.fly_time)
        return distance


class TodayPuzzle(Puzzle):
    def part_one(self, race_duration=2503):
        return max(reindeer.fly(race_duration) for reindeer in self.input)

    def part_two(self, race_duration=2503):
        points = [0 for _ in self.input]
        for t in range(1, race_duration + 1):
            distances = [reindeer.fly(t) for reindeer in self.input]
            for k, distance in enumerate(distances):
                if distance == max(distances):
                    points[k] += 1
        return max(points)


if __name__ == "__main__":
    TodayPuzzle(parser=parser, parse_lines=True, solutions=(2660, 1256)).solve()
