"""Day 6 script."""

import env
from lib import orbits

# Input
with open('inputs/06_orbit_map.txt') as f:
    orbit_map = [line[:-1] for line in f]

# Part 1:
orb = orbits.Orbit(orbit_map)
print(f"Orbit map checksum is {orb.checksum}")
assert orb.checksum == 294191

# Part 2:
t = orb.transfer('YOU', 'SAN')
print(f"Transfers needed to reach same orbit as Santa: {t}")
assert t == 424
