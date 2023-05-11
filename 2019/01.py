"""Day 1: The Tyranny of the Rocket Equation."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.modules = list(map(int, self.input))

    def part_one(self):
        return sum(m // 3 - 2 for m in self.modules)

    def part_two(self):
        total_fuel = 0
        for m in self.modules:
            fuel = [m // 3 - 2]
            while fuel[-1] != 0:
                fuel.append(max(fuel[-1] // 3 - 2, 0))
            total_fuel += sum(fuel)
        return total_fuel


solutions = (3426455, 5136807)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
