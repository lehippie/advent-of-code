"""Day 15: Oxygen System."""

from pathlib import Path

from oxygen_system import RepairDroid, oxygen_propagation
from intcode import Intcode


# --- Puzzle input ---
input_file = Path(__file__).parent / "repair_droid_program.txt"
program = Intcode.from_file(input_file)


# --- Part 1 ---
droid = RepairDroid(program)
droid.explore()
droid.find_path()
droid.show_area()
steps = len(droid.path) - 1
print(f"Minimum {steps} steps are required to move to the Oxygen System.")
assert steps == 404


# --- Part 2 ---
oxygenation_time = oxygen_propagation(droid.area)
print(f"It will take {oxygenation_time} minutes to fill oxygen everywhere.")
assert oxygenation_time == 406
