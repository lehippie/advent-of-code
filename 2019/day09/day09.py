"""Day 9: Sensor Boost."""

from pathlib import Path
from intcode import Intcode

# Input
input_file = Path(__file__).parent / 'BOOST_program.txt'
boost = Intcode(str(input_file))

# Part 1:
out = boost.run(1)
print("BOOST test keycode:", out)
assert out == 3839402290

# Part 2:
boost.reset()
distress_coordinates = boost.run(2)
print("Coordinates of the distress signal:", distress_coordinates)
assert distress_coordinates == 35734
