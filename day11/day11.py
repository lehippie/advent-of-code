"""Day 11: Space Police."""

from pathlib import Path
from intcode import Intcode

# Input
input_file = Path(__file__).parent / 'painting_robot_program.txt'
robot = Intcode.from_file(input_file)

# Part 1:
