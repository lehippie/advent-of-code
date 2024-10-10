"""--- Day 11: Space Police ---"""

from hashlib import md5
from aoc.puzzle import Puzzle
from intcode import Intcode

TURN = {
    0: {"U": "L", "L": "D", "D": "R", "R": "U"},
    1: {"U": "R", "R": "D", "D": "L", "L": "U"},
}
MOVE = {"U": 1j, "R": 1, "D": -1j, "L": -1}


class Robot:
    def __init__(self, program):
        self.brain = Intcode(program)
        self.panels = {}
        self.position = 0
        self.face = "U"

    def run_step(self):
        color = self.panels.get(self.position, 0)
        self.panels[self.position] = self.brain.run(color)
        direction = self.brain.run()
        if direction is not None:
            self.face = TURN[direction][self.face]
            self.position += MOVE[self.face]


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        bot = Robot(self.program)
        while bot.brain.is_running:
            bot.run_step()
        return len(bot.panels)

    def part_two(self):
        bot = Robot(self.program)
        bot.panels[0] = 1
        while bot.brain.is_running:
            bot.run_step()

        xm = int(min(p.real for p in bot.panels))
        xM = int(max(p.real for p in bot.panels))
        ym = int(min(p.imag for p in bot.panels))
        yM = int(max(p.imag for p in bot.panels))
        origin = xm + yM * 1j
        image = "\n".join(
            "".join(
                "#" if bot.panels.get(x + y * 1j - origin, 0) else " "
                for x in range(xm, xM + 1)
            )
            for y in range(yM, ym - 1, -1)
        )
        # print(image)
        return md5(image.encode()).hexdigest()


if __name__ == "__main__":
    Today().solve()
