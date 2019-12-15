"""Advent of Code 2019 - Day One."""


INPUT_FILE = __file__.rsplit('/', 1)[0] + '/input.txt'


def fuel_for_mass(mass):
    return max(mass // 3 - 2, 0)


def fuel_needed(mass):
    fuel = [fuel_for_mass(mass)]
    while fuel[-1] != 0:
        fuel.append(fuel_for_mass(fuel[-1]))
    return sum(fuel)


def calculation(modules=INPUT_FILE):
    fuel_modules = 0
    fuel_total = 0
    with open(modules) as f:
        for mass in f:
            fuel_modules += fuel_for_mass(int(mass))
            fuel_total += fuel_needed(int(mass))
    return fuel_modules, fuel_total


if __name__ == '__main__':
    fuel_modules, fuel_total = calculation()
    print(f"Amount of fuel needed for the modules: {fuel_modules}")
    print(f"Amount of fuel needed, counting added fuel: {fuel_total}")
