"""Day 3 script."""

import env
from lib import wires_panel as wp

# Input
with open('inputs/03_wires.txt') as f:
    wire1_path = f.readline()
    wire2_path = f.readline()

# Part 1
distance = wp.distance(wire1_path, wire2_path)
print(f"Manhattan distance is: {distance}")

# Part 2