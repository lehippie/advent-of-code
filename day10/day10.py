"""Day 10: Monitoring Station."""

from pathlib import Path
from asteroids import AsteroidsMap

# Input
input_file = Path(__file__).parent / 'ceres_asteroids_map.txt'
ceres = AsteroidsMap(str(input_file))

# Part 1:
print(f"Best location is {ceres.best} "
      f"with {ceres.counts[ceres.best]} asteroids detected.")
assert ceres.counts[ceres.best] == 340

# Part 2:
