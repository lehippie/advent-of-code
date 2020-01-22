"""Day 9 script."""

import env
from lib.intcode import Intcode

# Input
boost = Intcode('inputs/09_boost_program.txt')

# Part 1:
out = boost.run(1)
print("BOOST test keycode:", out)
assert out == 3839402290

# Part 2:
boost.reset()
distress_coordinates = boost.run(2)
print("Coordinates of the distress signal:", distress_coordinates)
assert distress_coordinates == 35734
