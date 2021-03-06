"""Tests of Intcode computer."""

from intcode import Intcode


def tests():
    ###########################
    ####    Day02 tests    ####
    ###########################

    i = Intcode([1,9,10,3,2,3,11,0,99,30,40,50])
    i.execute_next()
    assert i.memory == [1,9,10,70,2,3,11,0,99,30,40,50]
    i.execute_next()
    assert i.memory == [3500,9,10,70,2,3,11,0,99,30,40,50]

    i = Intcode([1,0,0,0,99])
    i.run()
    assert i.memory == [2,0,0,0,99]

    i = Intcode([2,3,0,3,99])
    i.run()
    assert i.memory == [2,3,0,6,99]

    i = Intcode([2,4,4,5,99,0])
    i.run()
    assert i.memory == [2,4,4,5,99,9801]

    i = Intcode([1,1,1,4,99,5,6,0,99])
    i.run()
    assert i.memory == [30,1,1,4,2,5,6,0,99]
    assert i.pointer == 8
    i.reset()
    assert i.memory == [1,1,1,4,99,5,6,0,99]

    ###########################
    ####    Day05 tests    ####
    ###########################

    i = Intcode([1002,4,3,4,33])
    i.run()
    assert i.memory == [1002,4,3,4,99]

    i = Intcode([1101,100,-1,4,0])
    i.run()
    assert i.memory == [1101,100,-1,4,99]

    i = Intcode([3,9,8,9,10,9,4,9,99,-1,8])
    assert i.run(8) == 1
    i.reset()
    assert i.run(66) == 0
    i.reset()
    assert i.run(-8) == 0

    i = Intcode([3,9,7,9,10,9,4,9,99,-1,8])
    assert i.run(7) == 1
    i.reset()
    assert i.run(8) == 0
    i.reset()
    assert i.run(42) == 0

    i = Intcode([3,3,1108,-1,8,3,4,3,99])
    assert i.run(8) == 1
    i.reset()
    assert i.run(66) == 0
    i.reset()
    assert i.run(-8) == 0

    i = Intcode([3,3,1107,-1,8,3,4,3,99])
    assert i.run(7) == 1
    i.reset()
    assert i.run(8) == 0
    i.reset()
    assert i.run(42) == 0

    i = Intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
    assert i.run(0) == 0
    i.reset()
    assert i.run(500) == 1
    i.reset()
    assert i.run(-1) == 1

    i = Intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1])
    assert i.run(0) == 0
    i.reset()
    assert i.run(500) == 1
    i.reset()
    assert i.run(-1) == 1

    i = Intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    assert i.run(-123) == 999
    i.reset()
    assert i.run(8) == 1000
    i.reset()
    assert i.run(666) == 1001


if __name__ == "__main__":
    tests()
