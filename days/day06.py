"""Day 6 script."""

import env
from lib import orbits

# Input
orbit_map = []
with open('inputs/06_orbit_map.txt') as f:
    for line in f:
        orbit_map.append(line[:-1])

# Part 1: 294191
orb = orbits.Orbit(orbit_map)
print(f"Orbit map checksum is {orb.checksum}")

# Part 2: 424
t = orb.transfer('YOU', 'SAN')
print(f"Transfers needed to reach same orbit as Santa: {t}")
