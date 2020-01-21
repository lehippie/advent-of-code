"""Day 5 script."""

import env
from lib.intcode import Intcode

# Input
test = Intcode('inputs/05_test_diagnostic_program.txt')

# Part 1: 2845163
print("Diagnostic for air conditioner unit:")
test.execute(1, 'stdout')

# Part 2: 9436229
test.reset()
print("Diagnostic for thermal radiator controller:")
test.execute(5, 'stdout')
