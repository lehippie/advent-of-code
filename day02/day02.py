"""Day 2: 1202 Program Alarm."""

from pathlib import Path
from intcode import Intcode

# Input
input_file = Path(__file__).parent / 'gravity_assist_program.txt'
gap = Intcode(str(input_file))

# Part 1:
gap.memory[1] = 12
gap.memory[2] = 2
gap.run()
print(f"Gravity Assist Program output for '1202' input: {gap.memory[0]}")
assert gap.memory[0] == 4484226

# Part 2:
def run(program, noun, verb):
    """Execute program with given noun and verb."""
    program.reset()
    program.memory[1] = noun
    program.memory[2] = verb
    program.run()
    return program.memory[0]

def find_input(program, wanted_output, max_input=100):
    """Find input of program that gives wanted output."""
    for noun in range(max_input):
        for verb in range(max_input):
            if run(program, noun, verb) == wanted_output:
                return 100 * noun + verb

wanted = 19690720
best_input = find_input(gap, wanted)
print(f"Input giving {wanted} output: {best_input}")
assert best_input == 5696
