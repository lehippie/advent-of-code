"""Day 5 script."""

import env
from lib.intcode import Intcode

# Input
diagnostic = Intcode('inputs/05_test_diagnostic_program.txt')

# Part 1:
print("Diagnostic for air conditioner unit:")
diagnostic.execute(1, stdout=True)
assert diagnostic.last_output == 2845163

# Part 2:
diagnostic.reset()
out = diagnostic.execute(5)
print("Diagnostic for thermal radiator controller:", out)
assert out == 9436229
