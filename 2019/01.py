"""Day 1: The Tyranny of the Rocket Equation."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.modules = list(map(int, self.input))

    def part_one(self):
        return sum(mass // 3 - 2 for mass in self.modules)

    def part_two(self):
        total_fuel = 0
        for mass in self.modules:
            fuel = mass // 3 - 2
            while fuel > 0:
                total_fuel += fuel
                fuel = fuel // 3 - 2
        return total_fuel


if __name__ == "__main__":
    Today().solve()
