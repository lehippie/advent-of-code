"""Day 7: Amplification Circuit."""

from itertools import permutations
from pathlib import Path
from intcode import Intcode
import thrusters

# Input
input_file = Path(__file__).parent / 'amplifier_controller_software.txt'
amp = Intcode(str(input_file))

# Part 1:
max_signal = 0
for phases in permutations(range(5)):
    thruster_signal = thrusters.thrusters(amp, phases)
    if thruster_signal > max_signal:
        max_signal = thruster_signal
        best_phases = phases
print(f"Maximum output is {max_signal} "
      f"for phase sequence {best_phases}")
assert max_signal == 117312

# Part 2:
amplifiers = [Intcode(str(input_file), name=i) for i in 'ABCDE']
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
assert max_signal ==  1336480
