"""Day 1 script."""

import env
from lib import fuel

# Input
modules_masses = []
with open('inputs/01_modules.txt') as f:
    for mass in f:
        modules_masses.append(int(mass))

# Part 1
fuel_modules = [fuel.fuel_for_mass(m) for m in modules_masses]
print(f"Amount of fuel needed for the modules: {sum(fuel_modules)}")

# Part 2
total_fuel = [fuel.fuel_total(m) for m in modules_masses]
print(f"Amount of fuel needed, counting added fuel: {sum(total_fuel)}")
