"""Day 13: Care Package."""

from pathlib import Path

from arcade import Arcade
from intcode import Intcode


# Input
input_file = Path(__file__).parent / 'game.txt'
with input_file.open() as f:
    game_program = f.readline()
game_program = [int(i) for i in game_program.split(",")]


# Part 1:
arcade = Arcade(Intcode(game_program, "Game"))
arcade.run()
blocks_amount = sum(1 for _, i in arcade.tiles.items() if i == 2)
print(f"There are {blocks_amount} block tiles.")
assert blocks_amount == 452


# Part 2:
game_program[0] = 2
arcade = Arcade(Intcode(game_program, "Game with coin"))
arcade.run()
print(f"Final score: {arcade.score}.")
assert arcade.score == 21415
