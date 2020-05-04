"""Tests of Emergency Hull Painting Robot library."""

import painting_robot as pr


def tests():
    r = pr.PaintingRobot()
    assert r.look() == 0
    r.paint('white')
    assert r.look() == 1
    r.rotate(1)
    assert r.face == 'e'
    r.move()
    assert r.look() == 0
    r.action(1, 'left')
    assert r.panels[(1,0)] == 1
    assert r.face == 'n'
    assert (r.posx, r.posy) == (1, 1)
    assert r.look() == 0
    r.rotate('left')
    r.move()
    r.rotate(0)
    r.move()
    assert r.look() == 1
    assert r.face == 's'


if __name__ == '__main__':
    tests()