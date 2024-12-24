"""--- Day 14: Restroom Redoubt ---"""

import re
from math import prod
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.robots = [tuple(map(int, re.findall(r"-?\d+", l))) for l in self.input]

    def part_one(self):
        quadrants = [0, 0, 0, 0]
        xlim, ylim = 101 // 2, 103 // 2
        for px, py, vx, vy in self.robots:
            x = (px + 100 * vx) % 101
            y = (py + 100 * vy) % 103
            if x < xlim and y < ylim:
                quadrants[0] += 1
            elif x < xlim and y > ylim:
                quadrants[1] += 1
            elif x > xlim and y < ylim:
                quadrants[2] += 1
            elif x > xlim and y > ylim:
                quadrants[3] += 1
        return prod(quadrants)

    def part_two(self):
        """Looking at the first iterations, we can see repeating patterns:
        Horizontal = 30 and 133 seconds => cycle = 103
        Vertical = 89 and 190 seconds => cycle = 101
        The Christmas tree appears when those patterns are lining up.
        """
        robots = {*self.robots}
        positions = {x + y * 1j for x, y, _, _, in robots}
        t = 0
        while True:
            t += 1
            next_robots, next_positions = set(), set()
            for px, py, vx, vy in robots:
                x = (px + vx) % 101
                y = (py + vy) % 103
                next_robots.add((x, y, vx, vy))
                next_positions.add(x + y * 1j)
            robots = next_robots
            positions = next_positions
            if not (t - 30) % 103 and not (t - 89) % 101:
                return t
                print(
                    "\n".join(
                        "".join(
                            "@" if x + y * 1j in positions else " " for x in range(101)
                        )
                        for y in range(103)
                    )
                    + f"\n------ t = {t} ------\n"
                )


if __name__ == "__main__":
    Today().solve()
