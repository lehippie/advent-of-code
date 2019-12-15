"""Tests of fuel calculation functions."""

import env
from lib import fuel


assert fuel.fuel_for_mass(12) == 2
assert fuel.fuel_for_mass(14) == 2
assert fuel.fuel_for_mass(1969) == 654
assert fuel.fuel_for_mass(100756) == 33583

assert fuel.fuel_total(14) == 2
assert fuel.fuel_total(1969) == 966
assert fuel.fuel_total(100756) == 50346
