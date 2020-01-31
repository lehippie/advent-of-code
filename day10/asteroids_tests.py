"""Tests of Asteroids map library."""

from pathlib import Path
from asteroids import AsteroidsMap


def tests():
    a = AsteroidsMap(['.#..#', '.....', '#####', '....#', '...##'])
    assert a.positions == [(1,0), (4,0), (0,2), (1,2), (2,2), (3,2), (4,2), (4,3), (3,4), (4,4)]
    assert a.count_detections() == [7, 7, 6, 7, 7, 7, 5, 7, 8, 7]
    assert a.station == (3,4)
    assert a.station_count == 8

    testmap = str(Path(__file__).parent / 'testmap1.txt')
    a = AsteroidsMap(testmap)
    assert a.station == (5,8)
    assert a.station_count == 33

    testmap = str(Path(__file__).parent / 'testmap2.txt')
    a = AsteroidsMap(testmap)
    assert a.station == (1,2)
    assert a.station_count == 35

    testmap = str(Path(__file__).parent / 'testmap3.txt')
    a = AsteroidsMap(testmap)
    assert a.station == (6,3)
    assert a.station_count == 41

    testmap = str(Path(__file__).parent / 'testmap4.txt')
    a = AsteroidsMap(testmap)
    assert a.station == (11,13)
    assert a.station_count == 210


if __name__ == "__main__":
    tests()
