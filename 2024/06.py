"""--- Day 6: Guard Gallivant ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.area, self.obstacles = set(), set()
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                position = r + c * 1j
                if cell == ".":
                    self.area.add(position)
                if cell == "#":
                    self.obstacles.add(position)
                elif cell == "^":
                    self.start = position
                    self.area.add(position)

    def part_one(self):
        """The guard is followed by keeping track of the visited
        cells in a set.
        """
        guard, direction = self.start, -1
        visited = set()
        while guard in self.area:
            visited.add(guard)
            step = guard + direction
            if step in self.obstacles:
                direction *= -1j
            else:
                guard = step
        return len(visited)

    def part_two(self):
        """While the guard is followed again, for each step forward
        in a position that have not been visited yet, we simulate the
        path of a virtual guard turning to the right.
        Loops are found if the virtual guard eventually gets in its
        own path.
        """
        guard, direction = self.start, -1
        visited, path, obstructions = set(), set(), set()
        while guard in self.area:
            visited.add(guard)
            path.add((guard, direction))
            step = guard + direction
            if step in self.obstacles:
                direction *= -1j
                continue

            # Simulation
            if step in self.area and step not in visited:
                g, d, p = guard, direction * -1j, path.copy()
                while g in self.area:
                    p.add((g, d))
                    s = g + d
                    if s in self.obstacles or s == step:
                        d *= -1j
                    else:
                        if (s, d) in p:
                            obstructions.add(step)
                            break
                        g = s

            guard = step
        return len(obstructions)


if __name__ == "__main__":
    Today().solve()
