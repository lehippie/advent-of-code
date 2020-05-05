"""Tests of Moons Motion library."""

from moons_motion import Moon, MotionSimulator


def tests():
    tests_moon()
    tests_motion()


def tests_moon():
    moon = Moon()
    assert moon.pos == [0, 0, 0]
    assert moon.vel == [0, 0, 0]
    moon = Moon((10, 20, 30), list(range(3)))
    assert moon.pos == [10, 20, 30]
    assert moon.vel == [0, 1, 2]
    moon.move()
    assert moon.pos == [10, 21, 32]
    moon.vel[2] = -15
    moon.move()
    assert moon.pos == [10, 22, 17]


def tests_motion():
    sim = MotionSimulator([
        Moon([-1, 0, 2]),
        Moon([2, -10, -7]),
        Moon([4, -8, 8]),
        Moon([3, 5, -1])
    ])
    assert str(sim) == (
        "After 0 steps:\n"
        "pos=<x=-1, y=  0, z= 2>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 2, y=-10, z=-7>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 4, y= -8, z= 8>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 3, y=  5, z=-1>, vel=<x= 0, y= 0, z= 0>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 1 steps:\n"
        "pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>\n"
        "pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>\n"
        "pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>\n"
        "pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 2 steps:\n"
        "pos=<x= 5, y=-3, z=-1>, vel=<x= 3, y=-2, z=-2>\n"
        "pos=<x= 1, y=-2, z= 2>, vel=<x=-2, y= 5, z= 6>\n"
        "pos=<x= 1, y=-4, z=-1>, vel=<x= 0, y= 3, z=-6>\n"
        "pos=<x= 1, y=-4, z= 2>, vel=<x=-1, y=-6, z= 2>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 3 steps:\n"
        "pos=<x= 5, y=-6, z=-1>, vel=<x= 0, y=-3, z= 0>\n"
        "pos=<x= 0, y= 0, z= 6>, vel=<x=-1, y= 2, z= 4>\n"
        "pos=<x= 2, y= 1, z=-5>, vel=<x= 1, y= 5, z=-4>\n"
        "pos=<x= 1, y=-8, z= 2>, vel=<x= 0, y=-4, z= 0>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 4 steps:\n"
        "pos=<x= 2, y=-8, z= 0>, vel=<x=-3, y=-2, z= 1>\n"
        "pos=<x= 2, y= 1, z= 7>, vel=<x= 2, y= 1, z= 1>\n"
        "pos=<x= 2, y= 3, z=-6>, vel=<x= 0, y= 2, z=-1>\n"
        "pos=<x= 2, y=-9, z= 1>, vel=<x= 1, y=-1, z=-1>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 5 steps:\n"
        "pos=<x=-1, y=-9, z= 2>, vel=<x=-3, y=-1, z= 2>\n"
        "pos=<x= 4, y= 1, z= 5>, vel=<x= 2, y= 0, z=-2>\n"
        "pos=<x= 2, y= 2, z=-4>, vel=<x= 0, y=-1, z= 2>\n"
        "pos=<x= 3, y=-7, z=-1>, vel=<x= 1, y= 2, z=-2>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 6 steps:\n"
        "pos=<x=-1, y=-7, z= 3>, vel=<x= 0, y= 2, z= 1>\n"
        "pos=<x= 3, y= 0, z= 0>, vel=<x=-1, y=-1, z=-5>\n"
        "pos=<x= 3, y=-2, z= 1>, vel=<x= 1, y=-4, z= 5>\n"
        "pos=<x= 3, y=-4, z=-2>, vel=<x= 0, y= 3, z=-1>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 7 steps:\n"
        "pos=<x= 2, y=-2, z= 1>, vel=<x= 3, y= 5, z=-2>\n"
        "pos=<x= 1, y=-4, z=-4>, vel=<x=-2, y=-4, z=-4>\n"
        "pos=<x= 3, y=-7, z= 5>, vel=<x= 0, y=-5, z= 4>\n"
        "pos=<x= 2, y= 0, z= 0>, vel=<x=-1, y= 4, z= 2>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 8 steps:\n"
        "pos=<x= 5, y= 2, z=-2>, vel=<x= 3, y= 4, z=-3>\n"
        "pos=<x= 2, y=-7, z=-5>, vel=<x= 1, y=-3, z=-1>\n"
        "pos=<x= 0, y=-9, z= 6>, vel=<x=-3, y=-2, z= 1>\n"
        "pos=<x= 1, y= 1, z= 3>, vel=<x=-1, y= 1, z= 3>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 9 steps:\n"
        "pos=<x= 5, y= 3, z=-4>, vel=<x= 0, y= 1, z=-2>\n"
        "pos=<x= 2, y=-9, z=-3>, vel=<x= 0, y=-2, z= 2>\n"
        "pos=<x= 0, y=-8, z= 4>, vel=<x= 0, y= 1, z=-2>\n"
        "pos=<x= 1, y= 1, z= 5>, vel=<x= 0, y= 0, z= 2>"
    )
    sim.next_step()
    assert str(sim) == (
        "After 10 steps:\n"
        "pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>\n"
        "pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>\n"
        "pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>\n"
        "pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>"
    )
    assert sim.energy() == 179

    sim = MotionSimulator([
        Moon([-8, -10, 0]),
        Moon([5, 5, 10]),
        Moon([2, -7, 3]),
        Moon([9, -8, -3])
    ])
    assert str(sim) == (
        "After 0 steps:\n"
        "pos=<x=-8, y=-10, z= 0>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 5, y=  5, z=10>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 2, y= -7, z= 3>, vel=<x= 0, y= 0, z= 0>\n"
        "pos=<x= 9, y= -8, z=-3>, vel=<x= 0, y= 0, z= 0>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 10 steps:\n"
        "pos=<x=-9, y=-10, z= 1>, vel=<x=-2, y=-2, z=-1>\n"
        "pos=<x= 4, y= 10, z= 9>, vel=<x=-3, y= 7, z=-2>\n"
        "pos=<x= 8, y=-10, z=-3>, vel=<x= 5, y=-1, z=-2>\n"
        "pos=<x= 5, y=-10, z= 3>, vel=<x= 0, y=-4, z= 5>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 20 steps:\n"
        "pos=<x=-10, y=  3, z=-4>, vel=<x=-5, y= 2, z= 0>\n"
        "pos=<x=  5, y=-25, z= 6>, vel=<x= 1, y= 1, z=-4>\n"
        "pos=<x= 13, y=  1, z= 1>, vel=<x= 5, y=-2, z= 2>\n"
        "pos=<x=  0, y=  1, z= 7>, vel=<x=-1, y=-1, z= 2>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 30 steps:\n"
        "pos=<x=15, y= -6, z=-9>, vel=<x=-5, y=  4, z= 0>\n"
        "pos=<x=-4, y=-11, z= 3>, vel=<x=-3, y=-10, z= 0>\n"
        "pos=<x= 0, y= -1, z=11>, vel=<x= 7, y=  4, z= 3>\n"
        "pos=<x=-3, y= -2, z= 5>, vel=<x= 1, y=  2, z=-3>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 40 steps:\n"
        "pos=<x=14, y=-12, z=-4>, vel=<x=11, y= 3, z= 0>\n"
        "pos=<x=-1, y= 18, z= 8>, vel=<x=-5, y= 2, z= 3>\n"
        "pos=<x=-5, y=-14, z= 8>, vel=<x= 1, y=-2, z= 0>\n"
        "pos=<x= 0, y=-12, z=-2>, vel=<x=-7, y=-3, z=-3>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 50 steps:\n"
        "pos=<x=-23, y=  4, z= 1>, vel=<x=-7, y=-1, z= 2>\n"
        "pos=<x= 20, y=-31, z=13>, vel=<x= 5, y= 3, z= 4>\n"
        "pos=<x= -4, y=  6, z= 1>, vel=<x=-1, y= 1, z=-3>\n"
        "pos=<x= 15, y=  1, z=-5>, vel=<x= 3, y=-3, z=-3>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 60 steps:\n"
        "pos=<x= 36, y=-10, z= 6>, vel=<x= 5, y= 0, z= 3>\n"
        "pos=<x=-18, y= 10, z= 9>, vel=<x=-3, y=-7, z= 5>\n"
        "pos=<x=  8, y=-12, z=-3>, vel=<x=-2, y= 1, z=-7>\n"
        "pos=<x=-18, y= -8, z=-2>, vel=<x= 0, y= 6, z=-1>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 70 steps:\n"
        "pos=<x=-33, y=-6, z= 5>, vel=<x=-5, y=-4, z= 7>\n"
        "pos=<x= 13, y=-9, z= 2>, vel=<x=-2, y=11, z= 3>\n"
        "pos=<x= 11, y=-8, z= 2>, vel=<x= 8, y=-6, z=-7>\n"
        "pos=<x= 17, y= 3, z= 1>, vel=<x=-1, y=-1, z=-3>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 80 steps:\n"
        "pos=<x= 30, y=-8, z= 3>, vel=<x= 3, y=  3, z= 0>\n"
        "pos=<x= -2, y=-4, z= 0>, vel=<x= 4, y=-13, z= 2>\n"
        "pos=<x=-18, y=-7, z=15>, vel=<x=-8, y=  2, z=-2>\n"
        "pos=<x= -2, y=-1, z=-8>, vel=<x= 1, y=  8, z= 0>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 90 steps:\n"
        "pos=<x=-25, y=-1, z= 4>, vel=<x= 1, y=-3, z= 4>\n"
        "pos=<x=  2, y=-9, z= 0>, vel=<x=-3, y=13, z=-1>\n"
        "pos=<x= 32, y=-8, z=14>, vel=<x= 5, y=-4, z= 6>\n"
        "pos=<x= -1, y=-2, z=-8>, vel=<x=-3, y=-6, z=-9>"
    )
    sim.next_step(10)
    assert str(sim) == (
        "After 100 steps:\n"
        "pos=<x=  8, y=-12, z=-9>, vel=<x=-7, y=  3, z= 0>\n"
        "pos=<x= 13, y= 16, z=-3>, vel=<x= 3, y=-11, z=-5>\n"
        "pos=<x=-29, y=-11, z=-1>, vel=<x=-3, y=  7, z= 4>\n"
        "pos=<x= 16, y=-13, z=23>, vel=<x= 7, y=  1, z= 1>"
    )
    assert sim.energy() == 1940


if __name__ == '__main__':
    tests()