"""Day 2 script."""

import env
from lib import intcode

# Input
gap_file = 'inputs/02_gravity_assist_program.txt'

# Part 1
gap = intcode.from_file(gap_file)
gap.memory[1] = 12
gap.memory[2] = 2
gap.execute()
print(f"Gravity Assist Program output for '1202' input: {gap.memory[0]}")

# Part 2
def execute_gap(noun, verb):
    """Execute Gravity Assist Program with given noun and verb."""
    gap = intcode.from_file(gap_file)
    gap.memory[1] = noun
    gap.memory[2] = verb
    gap.execute()
    return gap.memory[0]

def find_gap_input(wanted_output):
    """Find input that gives wanted output."""
    for noun in range(100):
        for verb in range(100):
            if execute_gap(noun, verb) == wanted_output:
                return 100 * noun + verb

wanted = 19690720
print(f"Input giving {wanted} output: {find_gap_input(wanted)}")
