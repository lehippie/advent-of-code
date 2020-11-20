"""Day 10: Monitoring Station."""

from pathlib import Path
from asteroids import AsteroidsMap

# Input
input_file = Path(__file__).parent / 'ceres_asteroids_map.txt'
ceres = AsteroidsMap(str(input_file))

# Part 1:
print(f"Best location is {ceres.station} "
      f"with {ceres.station_count} asteroids detected.")
assert ceres.station_count == 340

# Part 2:
n = 200
bet = ceres.vaporized(n)
bet_format = 100 * bet[0] + bet[1]
print(f"The {n}th asteroid to be vaporized is at {bet}")
assert bet_format == 2628
