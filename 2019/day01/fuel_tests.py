"""Tests of fuel calculations library."""

import fuel


def tests():
    assert fuel.fuel_for_mass(12) == 2
    assert fuel.fuel_for_mass(14) == 2
    assert fuel.fuel_for_mass(1969) == 654
    assert fuel.fuel_for_mass(100756) == 33583

    assert fuel.total_fuel_for_mass(14) == 2
    assert fuel.total_fuel_for_mass(1969) == 966
    assert fuel.total_fuel_for_mass(100756) == 50346


if __name__ == "__main__":
    tests()
