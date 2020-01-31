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
    assert a.vaporized(1) == (11,12)
    assert a.vaporized(2) == (12,1)
    assert a.vaporized(3) == (12,2)
    assert a.vaporized(10) == (12,8)
    assert a.vaporized(20) == (16,0)
    assert a.vaporized(50) == (16,9)
    assert a.vaporized(100) == (10,16)
    assert a.vaporized(199) == (9,6)
    assert a.vaporized(200) == (8,2)
    assert a.vaporized(201) == (10,9)
    assert a.vaporized(299) == (11,1)


if __name__ == "__main__":
    tests()
