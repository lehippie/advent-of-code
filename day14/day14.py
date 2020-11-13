"""Day 14: Space Stoichiometry."""

from pathlib import Path
from nanofactory import Factory

# Puzzle input
input_file = Path(__file__).parent / "reactions.txt"

# Part 1
fac = Factory.from_file(input_file)
ore_required = fac.simplify()
print(f"Minimum {ore_required} ORE is required to produce exactly 1 FUEL.")
assert ore_required == 201324

# Part 2
