"""Day 14: Space Stoichiometry."""

from pathlib import Path
from nanofactory import Factory

# Puzzle input
input_file = Path(__file__).parent / "reactions.txt"

# Part 1
fac = Factory.from_file(input_file)
ore_required = fac.direct_reaction["ORE"]
print(f"{ore_required} ORE required to produce 1 FUEL.")
assert ore_required == 201324

# Part 2
fuel = fac.produce()
print(f"1 trillion ORE produced {fuel} FUEL.")
assert fuel == 6326857
