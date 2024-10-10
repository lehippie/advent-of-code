"""--- Day 13: Care Package ---"""

from aoc.puzzle import Puzzle
from intcode import Intcode


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        arcade = Intcode(self.program)
        blocks = set()
        while arcade.is_running:
            x = arcade.run()
            y = arcade.run()
            tile_id = arcade.run()
            if tile_id == 2:
                blocks.add(x - y * 1j)
        return len(blocks)

    def part_two(self):
        arcade = Intcode(self.program)
        arcade.memory[0] = 2
        while arcade.is_running:
            x = arcade.run()
            y = arcade.run()
            tile_id = arcade.run()
            if x == -1 and y == 0:
                score = tile_id
            elif tile_id == 3:
                paddle = x
            elif tile_id == 4:
                ball = x
            elif arcade.waiting_for_input:
                if paddle > ball:
                    joystick = -1
                elif paddle < ball:
                    joystick = 1
                else:
                    joystick = 0
                arcade.inputs.append(joystick)
        return score


if __name__ == "__main__":
    Today().solve()
