"""Tests of Intcode computer class."""

import env
from lib import intcode


i = intcode.Intcode([1,0,0,0,99])
i.execute()
assert i.memory == [2,0,0,0,99]

i = intcode.Intcode([2,3,0,3,99])
i.execute()
assert i.memory == [2,3,0,6,99]

i = intcode.Intcode([2,4,4,5,99,0])
i.execute()
assert i.memory == [2,4,4,5,99,9801]

i = intcode.Intcode([1,1,1,4,99,5,6,0,99])
i.execute()
assert i.memory == [30,1,1,4,2,5,6,0,99]

i = intcode.Intcode([1,9,10,3,2,3,11,0,99,30,40,50])
i.execute()
assert i.memory == [3500,9,10,70,2,3,11,0,99,30,40,50]
