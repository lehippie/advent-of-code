"""Advent of Code - Day One."""


def fuel_needed(mass):
    return max(mass // 3 - 2, 0)


def fuel_total(mass):
    fuel = [fuel_needed(mass)]
    while fuel[-1] != 0:
        fuel.append(fuel_needed(fuel[-1]))
    return sum(fuel)


if __name__ == '__main__':
    fuel1 = 0
    fuel2 = 0
    with open('input.txt') as f:
        for mass in f:
            fuel1 += fuel_needed(int(mass))
            fuel2 += fuel_total(int(mass))
    print(f"Amount of fuel needed for the modules: {fuel1}")
    print(f"Amount of fuel needed, counting added fuel: {fuel2}")
