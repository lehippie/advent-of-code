"""Day 3: Crossed Wires."""

from pathlib import Path
from wires_panel import Wire

# Input
input_file = Path(__file__).parent / 'venus_wires_panel.txt'
with open(input_file) as f:
    wire1 = Wire(f.readline())
    wire2 = Wire(f.readline())

# Part 1:
distance = wire1.closest_cross(wire2)
print(f"Closest intersection is: {distance}")
assert distance == 446

# Part 2:
timing = wire1.shortest_cross(wire2)
print(f"Shortest intersection is: {timing}")
assert timing == 9006
