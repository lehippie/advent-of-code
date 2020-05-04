"""Day 11: Space Police."""

from pathlib import Path

import matplotlib.pyplot as plt

from intcode import Intcode
from painting_robot import PaintingRobot

# Input
input_file = Path(__file__).parent / 'painting_robot_program.txt'
robot_brain = Intcode.from_file(input_file)

# Part 1:
robot = PaintingRobot()
panels = robot.run(robot_brain)
print("Amount of panels painted:", len(panels))
assert len(panels) == 1863

# Part 2:
robot = PaintingRobot(start='white')
robot_brain.reset()
panels = robot.run(robot_brain)

xx = [p[0] for p, c in panels.items() if c]
yy = [p[1] for p, c in panels.items() if c]
plt.rcParams['toolbar'] = 'None'
_, ax = plt.subplots(
    figsize=(4, 0.6),
    facecolor='k')
ax.set_facecolor('k')
ax.plot(xx, yy, 'ws')
plt.show() # BLULZJLZ
