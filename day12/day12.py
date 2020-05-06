"""Day 12: The N-Body Problem."""

import re
from pathlib import Path
from moons_motion import Moon, MotionSimulator


# Input
input_file = Path(__file__).parent / 'moons_positions.txt'
moon_names = ['Io', 'Europa', 'Ganymede', 'Callisto']
with input_file.open() as f:
    moon_positions = [
        [int(p) for p in re.findall(r'-?[0-9]+', line)]
        for line in f
    ]


# Part 1:
sim = MotionSimulator([
    Moon(p, name=n)
    for p, n in zip(moon_positions, moon_names)
])
sim.next_step(1000)
total_energy = sim.energy()
print(f"Moons system energy = {total_energy}")
assert total_energy == 7687


# Part 2:
cycle_steps = sim.find_cycle()
print(f"System cycles in {cycle_steps} steps.")
assert cycle_steps == 334945516288044
