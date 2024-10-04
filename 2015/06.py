"""Day 6: Probably a Fire Hazard."""

from numpy import zeros
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        def parse(line):
            words = line.split(" ")
            if words[0] == "turn":
                words.pop(0)
            xmin, ymin = map(int, words[1].split(","))
            xmax, ymax = map(lambda x: int(x) + 1, words[3].split(","))
            return (words[0], xmin, xmax, ymin, ymax)

        self.instructions = [parse(line) for line in self.input]

    def part_one(self):
        lights = zeros((1000, 1000), dtype=int)
        for instruction, xmin, xmax, ymin, ymax in self.instructions:
            if instruction == "on":
                lights[xmin:xmax, ymin:ymax] = 1
            elif instruction == "off":
                lights[xmin:xmax, ymin:ymax] = 0
            elif instruction == "toggle":
                lights[xmin:xmax, ymin:ymax] += 1
                lights[xmin:xmax, ymin:ymax] %= 2
        return lights.sum()

    def part_two(self):
        lights = zeros((1000, 1000), dtype=int)
        for instruction, xmin, xmax, ymin, ymax in self.instructions:
            if instruction == "on":
                lights[xmin:xmax, ymin:ymax] += 1
            elif instruction == "off":
                lights[xmin:xmax, ymin:ymax] -= 1
                lights[lights < 0] = 0
            elif instruction == "toggle":
                lights[xmin:xmax, ymin:ymax] += 2
        return lights.sum()


if __name__ == "__main__":
    Today().solve()
