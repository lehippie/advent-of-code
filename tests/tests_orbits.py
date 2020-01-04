"""Tests of orbits."""

import env
from lib import orbits


def tests():
    o = orbits.Orbit(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H',
                      'D)I', 'E)J', 'J)K', 'K)L'])
    assert o.checksum == 42

    o = orbits.Orbit(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H',
                      'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'])
    assert o.transfer('YOU', 'SAN') == 4


if __name__ == "__main__":
    tests()
