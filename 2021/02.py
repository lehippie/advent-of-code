"""Day 2: Dive!"""

from aoc.puzzle import Puzzle


class Submarine:
    def __init__(self, course):
        self.course = course
        self.position = 0
        self.depth = 0
        self.aim = 0

    def go(self):
        for c, v in self.course:
            if c == "forward":
                self.position += v
            elif c == "down":
                self.depth += v
            elif c == "up":
                self.depth -= v

    def go_with_aim(self):
        for c, v in self.course:
            if c == "forward":
                self.position += v
                self.depth += self.aim * v
            elif c == "down":
                self.aim += v
            elif c == "up":
                self.aim -= v


class Puzzle02(Puzzle):
    def parser(self):
        return [(c, int(v)) for c, v in map(str.split, self.input)]

    def part_one(self):
        sub = Submarine(self.input)
        sub.go()
        return sub.position * sub.depth

    def part_two(self):
        sub = Submarine(self.input)
        sub.go_with_aim()
        return sub.position * sub.depth


if __name__ == "__main__":
    Puzzle02(solutions=(2272262, 2134882034)).solve()
