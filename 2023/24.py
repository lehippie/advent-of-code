"""--- Day 24: Never Tell Me The Odds ---"""

from itertools import combinations
from math import copysign
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.hails = []
        for line in self.input:
            self.hails.append([int(i) for i in line.replace("@", ",").split(",")])

    def part_one(self, area=(200000000000000, 400000000000000)):
        """Each line passing through point (x0,y0,z0) with vector
        (a,b,c) has an equation (x-x0)/a = (y-y0)/b = (z-z0)/c.
        Ignoring z, its cartesian equation is y = y0 + (b/a)*(x-x0).

        If they are not parallel, we solve the equality of their
        equations to get (xi, yi) of the intersection and check that
        it is not in the past and in the test area.
        """
        intersections = 0
        for path1, path2 in combinations(self.hails, 2):
            x01, y01, _, a1, b1, _ = path1
            x02, y02, _, a2, b2, _ = path2
            # Parallel paths?
            det = a1 * b2 - a2 * b1
            if det == 0:
                continue
            xi = (a1 * a2 * (y01 - y02) + a1 * b2 * x02 - a2 * b1 * x01) / det
            # Paths crossing in the past?
            if (copysign(xi, a1) < copysign(x01, a1)) or (
                copysign(xi, a2) < copysign(x02, a2)
            ):
                continue
            # Intersection in test area?
            if area[0] <= xi <= area[1]:
                if area[0] <= y01 + (b1 / a1) * (xi - x01) <= area[1]:
                    intersections += 1
        return intersections

    def part_two(self):
        return super().part_two()


solutions = (27732, None)

if __name__ == "__main__":
    # Today(infile="test.txt", solutions=(None, None)).solve()
    Today(solutions=solutions).solve()
