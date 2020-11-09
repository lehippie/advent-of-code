"""Tests of Arcade library."""

from arcade import Arcade


def tests():
    a = Arcade()
    a.draw_tile(1, 2, 3)
    a.draw_tile(6, 5, 4)
    assert a.tiles == {(1, 2): 3, (6, 5): 4}


if __name__ == '__main__':
    tests()
