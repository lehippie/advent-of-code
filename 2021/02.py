"""Day 2: Dive!"""

from aoc.puzzle import Puzzle


class Submarine:
    def __init__(self):
        self.position = 0
        self.depth = 0

    def go(self, command, unit):
        if command == "forward":
            self.position += unit
        elif command == "down":
            self.depth += unit
        elif command == "up":
            self.depth -= unit


class AimingSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def go(self, command, unit):
        if command == "forward":
            self.position += unit
            self.depth += self.aim * unit
        elif command == "down":
            self.aim += unit
        elif command == "up":
            self.aim -= unit


class Today(Puzzle):
    def parser(self):
        self.commands = [(c, int(v)) for c, v in map(str.split, self.input)]

    def part_one(self, submarine=Submarine):
        sub = submarine()
        for command, unit in self.commands:
            sub.go(command, unit)
        return sub.position * sub.depth

    def part_two(self):
        return self.part_one(AimingSubmarine)


if __name__ == "__main__":
    Today().solve()
