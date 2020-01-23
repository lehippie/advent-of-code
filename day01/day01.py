"""Day 1: The Tyranny of the Rocket Equation."""

from pathlib import Path
import fuel

# Input
input_file = Path(__file__).parent / 'mass_of_each_module.txt'
with open(input_file) as f:
    modules_masses = [int(mass) for mass in f]

# Part 1:
fuel_needed = sum(fuel.fuel_for_mass(m) for m in modules_masses)
print(f"Amount of fuel needed for the modules: {fuel_needed}")
assert fuel_needed == 3426455

# Part 2:
total_fuel_needed = sum(fuel.total_fuel_for_mass(m) for m in modules_masses)
print(f"Amount of fuel needed, counting mass of added fuel: {total_fuel_needed}")
assert total_fuel_needed == 5136807
