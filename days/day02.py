"""Day 2 script."""

import env
from lib.intcode import Intcode

# Input
gap = Intcode('inputs/02_gravity_assist_program.txt')

# Part 1:
gap.memory[1] = 12
gap.memory[2] = 2
gap.execute()
print(f"Gravity Assist Program output for '1202' input: {gap.memory[0]}")
assert gap.memory[0] == 4484226

# Part 2:
def execute(program, noun, verb):
    """Execute program with given noun and verb."""
    program.reset()
    program.memory[1] = noun
    program.memory[2] = verb
    program.execute()
    return program.memory[0]

def find_input(program, wanted_output, max_input=100):
    """Find input of program that gives wanted output."""
    for noun in range(max_input):
        for verb in range(max_input):
            if execute(program, noun, verb) == wanted_output:
                return 100 * noun + verb

wanted = 19690720
best_input = find_input(gap, wanted)
print(f"Input giving {wanted} output: {best_input}")
assert best_input == 5696


# Extra
def gap_outputs():
    import numpy as np
    import matplotlib.pyplot as plt
    outputs = np.zeros((100, 100))
    nouns = list(range(100))
    verbs = nouns.copy()
    for n in nouns:
        for v in verbs:
            outputs[n,v] = execute(gap, n, v)
    plt.imshow(outputs)
    plt.show()
# gap_outputs()
