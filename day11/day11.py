"""Day 11: Space Police."""

from pathlib import Path
from intcode import Intcode
from painting_robot import PaintingRobot

# Input
input_file = Path(__file__).parent / 'painting_robot_program.txt'
robot_brain = Intcode.from_file(input_file)

# Part 1:
robot = PaintingRobot()
while True:
    color = robot_brain.run(robot.look(), halt_on_output=True)
    direction = robot_brain.run(halt_on_output=True)
    if robot_brain.finished:
        break
    robot.action(color, direction)
print("Amount of panels painted:", len(robot.panels))
assert len(robot.panels) == 1863

# Part 2:
