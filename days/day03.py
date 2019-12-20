"""Day 3 script."""

import env
from lib import wires

# Input
with open('inputs/03_wires.txt') as f:
    wire1 = wires.Wire(f.readline())
    wire2 = wires.Wire(f.readline())

# Part 1: 446
distance = wire1.closest_cross(wire2)
print(f"Closest intersection is: {distance}")

# Part 2: 9006
timing = wire1.shortest_cross(wire2)
print(f"Shortest intersection is: {timing}")
