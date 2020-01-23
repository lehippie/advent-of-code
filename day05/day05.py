"""Day 5: Sunny with a Chance of Asteroids."""

from pathlib import Path
from intcode import Intcode

# Input
input_file = Path(__file__).parent / 'TEST_diagnostic_program.txt'
diagnostic = Intcode(str(input_file))

# Part 1:
outs = diagnostic.run(1)
print("Diagnostic for air conditioner unit:", outs)
assert outs[-1] == 2845163

# Part 2:
diagnostic.reset()
out = diagnostic.run(5)
print("Diagnostic for thermal radiator controller:", out)
assert out == 9436229
