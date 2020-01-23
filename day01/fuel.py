"""Fuel calculations library."""


def fuel_for_mass(mass):
    """Calculate fuel needed for given mass."""
    return max(mass // 3 - 2, 0)

def total_fuel_for_mass(mass):
    """Calculate fuel needed for given mass, taking into account the
    mass of added fuel."""
    fuel = [fuel_for_mass(mass)]
    while fuel[-1] != 0:
        fuel.append(fuel_for_mass(fuel[-1]))
    return sum(fuel)


if __name__ == "__main__":
    from fuel_tests import tests
    tests()
