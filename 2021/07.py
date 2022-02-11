"""Day 7: The Treachery of Whales."""

from math import floor, ceil
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.crabs = list(map(int, self.input.split(",")))

    def part_one(self):
        """As fuel consumption is equal to the distance, the optimal
        solution is the median of the positions as there will be as
        many crabs on the left as on the right. Going away from it
        would decrease the fuel needed for one side less than it
        would increase it for all the other crabs.
        """
        crabs = sorted(self.crabs)
        median = crabs[(len(crabs) - 1) // 2]
        return sum(abs(crab - median) for crab in crabs)

    def part_two(self):
        """For a crab, the fuel consumption for n steps is n(n+1)/2.
        We need to find the minimum of those, summed over every crabs.
        With h the crab positions and x the the alignment position,
        the sum to minimize is abs(h-x) * (abs(h-x) + 1) / 2.

        The root of the derivative with respect to x tells us that the
        analytical solution lies between +/- 0.5 of the mean of the
        positions. Its real value depends on their distribution so we
        cannot deduce anything else from the general case.

        In conclusion, we reduced the possible optimal positions to
        the intergers around the mean of the crabs positions.

        P.S.: The derivative of abs(x) is sgn(x) except at x = 0. It
        does not bother us because the crab already at the optimal
        position won't move.
        """
        mean = sum(self.crabs) / len(self.crabs)
        fuels = []
        for m in floor(mean), ceil(mean):
            distances = [abs(crab - m) for crab in self.crabs]
            fuels.append(sum(d * (d + 1) // 2 for d in distances))
        return min(fuels)


solutions = (335271, 95851339)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
