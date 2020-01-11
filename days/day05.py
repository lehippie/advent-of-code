"""Day 5 script."""

import env
from lib import intcode

# Input
test = intcode.from_file('inputs/05_test_diagnostic_program.txt')

# Part 1: 2845163
print(test.execute(1))

# Part 2: 9436229
test.reset()
print(test.execute(5))
