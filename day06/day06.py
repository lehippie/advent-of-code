"""Day 6: Universal Orbit Map."""

from pathlib import Path
from orbits import Orbit

# Input
input_file = Path(__file__).parent / 'local_orbits.txt'
with open(input_file) as f:
    orbits_map = [line[:-1] for line in f]

# Part 1:
orb = Orbit(orbits_map)
print(f"Orbit map checksum is {orb.checksum}")
assert orb.checksum == 294191

# Part 2:
t = orb.transfer('YOU', 'SAN')
print(f"Transfers needed to reach same orbit as Santa: {t}")
assert t == 424
