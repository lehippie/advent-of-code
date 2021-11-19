"""Day 3: Perfectly Spherical Houses in a Vacuum."""

from aoc.puzzle import Puzzle


class Santa:
    def __init__(self):
        self.x, self.y = 0, 0

    @property
    def position(self):
        return self.x, self.y

    def move(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        elif direction == ">":
            self.x += 1
        elif direction == "<":
            self.x -= 1
        return self.position


class Puzzle03(Puzzle):
    def part_one(self):
        santa = Santa()
        houses = {santa.position}
        for direction in self.input:
            houses.add(santa.move(direction))
        return len(houses)

    def part_two(self):
        santa = Santa()
        robot = Santa()
        houses = {santa.position}
        for i, direction in enumerate(self.input):
            if i % 2:
                houses.add(santa.move(direction))
            else:
                houses.add(robot.move(direction))
        return len(houses)


if __name__ == "__main__":
    Puzzle03(solutions=(2572, 2631)).solve()
