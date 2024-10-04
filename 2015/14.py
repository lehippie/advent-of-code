"""Day 14: Reindeer Olympics."""

import re
from aoc.puzzle import Puzzle


class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.period = fly_time + rest_time

    def fly(self, time_limit):
        """The reindeer will fly during an integer amount of
        its period plus the remaining seconds of the incomplete
        period (with a limit of its <fly_time>).
        """
        duration = (time_limit // self.period) * self.fly_time
        duration += min(time_limit % self.period, self.fly_time)
        return duration * self.speed


class Today(Puzzle):
    def parser(self):
        def parse(line):
            name = line.split()[0]
            stats = list(map(int, re.findall(r"\d+", line)))
            return Reindeer(name, *stats)

        self.reindeers = [parse(line) for line in self.input]

    def part_one(self, race_duration=2503):
        """Calculate the distance traveled by each reindeer and
        return the maximum.
        """
        return max(reindeer.fly(race_duration) for reindeer in self.reindeers)

    def part_two(self, race_duration=2503):
        """Positions have to be determined at each second to
        distribute the points.
        """
        points = [0] * len(self.reindeers)
        for t in range(1, race_duration + 1):
            distances = [reindeer.fly(t) for reindeer in self.reindeers]
            lead = max(distances)
            for k, distance in enumerate(distances):
                if distance == lead:
                    points[k] += 1
        return max(points)


if __name__ == "__main__":
    Today().solve()
