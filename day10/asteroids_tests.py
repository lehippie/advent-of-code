"""Tests of Asteroids map library."""

from pathlib import Path
from asteroids import AsteroidsMap


def tests():
    a = AsteroidsMap(['.#..#', '.....', '#####', '....#', '...##'])
    assert a.sizeX == 5
    assert a.sizeY == 5
    assert a.positions == [(1,0), (4,0), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3), (3,4), (4,4)]
    assert set(a.detections[(3,4)]) == set([(4,0), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3), (4,4)])
    assert list(a.counts.values()) == [7, 7, 6, 7, 7, 7, 5, 7, 8, 7]
    assert a.best == (3,4)

    testmap = str(Path(__file__).parent / 'testmap1.txt')
    a = AsteroidsMap(testmap)
    assert a.best == (5,8)
    assert a.counts[a.best] == 33

    testmap = str(Path(__file__).parent / 'testmap2.txt')
    a = AsteroidsMap(testmap)
    assert a.best == (1,2)
    assert a.counts[a.best] == 35

    testmap = str(Path(__file__).parent / 'testmap3.txt')
    a = AsteroidsMap(testmap)
    assert a.best == (6,3)
    assert a.counts[a.best] == 41

    testmap = str(Path(__file__).parent / 'testmap4.txt')
    a = AsteroidsMap(testmap)
    assert a.best == (11,13)
    assert a.counts[a.best] == 210


if __name__ == "__main__":
    tests()
