"""--- Day 6: Wait For It ---"""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        times = list(map(int, re.findall(r"\d+", self.input[0])))
        distances = list(map(int, re.findall(r"\d+", self.input[1])))
        product = 1
        for time, distance in zip(times, distances):
            product *= sum((time - t) * t > distance for t in range(1, time))
        return product

    def part_two(self):
        """The race is won if (time - t) * t is greater than distance,
        where t is the duration of the press. It is a parabol centered
        at time/2. The first winning t is sufficient to calculate how
        many ways there are to win.
        
        To calculate it, we solve `t² - time * t + distance = 0` and
        add one to the result because we want a solution greater than
        the distance.
        """
        time, distance = [int(s.replace(" ", "").split(":")[1]) for s in self.input]
        first = (time - (time**2 - 4 * distance) ** 0.5) // 2 + 1
        return time - 2 * first + 1


solutions = (503424, 32607562)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
