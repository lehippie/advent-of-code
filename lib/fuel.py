"""Fuel calculation functions."""


def fuel_for_mass(mass):
    """Calculate fuel needed for given mass."""
    return max(mass // 3 - 2, 0)


def fuel_total(mass):
    """Calculate total fuel needed for given mass."""
    fuel = [fuel_for_mass(mass)]
    while fuel[-1] != 0:
        fuel.append(fuel_for_mass(fuel[-1]))
    return sum(fuel)


if __name__ == "__main__":
    import env
    from tests import tests_fuel
    tests_fuel.tests()
