"""Day 7 script."""

from itertools import permutations

import env
from lib import intcode, thrusters


# Part 1: 117312
acs = intcode.from_file('inputs/07_amplifier_controller_software.txt')
max_signal = 0
for phases in permutations(range(5)):
    thruster_signal = thrusters.thrusters(acs, phases)
    if thruster_signal > max_signal:
        max_signal = thruster_signal
        best_phases = phases
print(f"Maximum output is {max_signal} "
      f"for phase sequence {best_phases}")

# Part 2: 1336480
amplifiers = [intcode.from_file('inputs/07_amplifier_controller_software.txt',
              name=i) for i in 'ABCDE']
max_signal = 0
for phases in permutations(range(5, 10)):
    for amp in amplifiers:
        amp.reset()
    thruster_signal = thrusters.feedback_thrusters(amplifiers, phases)
    if thruster_signal > max_signal:
        max_signal = thruster_signal
        best_phases = phases
print(f"Maximum output is {max_signal} "
      f"for phase sequence {best_phases} (with feedback loop)")
