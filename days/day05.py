"""Day 5 script."""

import env
from lib import intcode

# Input
test = intcode.from_file('inputs/05_test_diagnostic_program.txt')

# Part 1: 2845163
test.execute() # Input = 1

# Part 2: 9436229
test.reset()
test.execute() # Input = 5
