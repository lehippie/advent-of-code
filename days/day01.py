"""Day 1 script."""

import env
from lib import fuel

# Input
with open('inputs/01_modules.txt') as f:
    modules_masses = [int(mass) for mass in f]

# Part 1:
fuel_modules = sum(fuel.fuel_for_mass(m) for m in modules_masses)
print(f"Amount of fuel needed for the modules: {fuel_modules}")
assert fuel_modules == 3426455

# Part 2:
total_fuel = sum(fuel.fuel_total(m) for m in modules_masses)
print(f"Amount of fuel needed, counting added fuel: {total_fuel}")
assert total_fuel == 5136807
