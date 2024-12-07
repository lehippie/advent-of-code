"""--- Day 6: Guard Gallivant ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.area = set()
        self.obstacles = set()
        for r, row in enumerate(self.input):
            for c, cell in enumerate(row):
                position = r + c * 1j
                if cell == ".":
                    self.area.add(position)
                if cell == "#":
                    self.obstacles.add(position)
                elif cell == "^":
                    self.area.add(position)
                    self.start = position

    def part_one(self):
        guard = self.start
        direction = -1
        visited = set()
        while guard in self.area:
            visited.add(guard)
            step = guard + direction
            if step in self.obstacles:
                direction *= -1j
                continue
            guard += direction
        return len(visited)

    def part_two(self):
        guard = self.start
        direction = -1
        visited = set()
        path = set()
        obstructions = set()
        while guard in self.area:
            visited.add(guard)
            path.add((guard, direction))
            step = guard + direction
            if step in self.obstacles:
                direction *= -1j
                continue
            if step in self.area and step not in visited:
                test_guard = guard
                test_direction = direction * -1j
                test_path = path.copy()
                while test_guard in self.area:
                    test_path.add((test_guard, test_direction))
                    test_step = test_guard + test_direction
                    if test_step in self.obstacles or test_step == step:
                        test_direction *= -1j
                        continue
                    test_guard += test_direction
                    if (test_guard, test_direction) in test_path:
                        obstructions.add(step)
                        break
            guard += direction
        return len(obstructions)


if __name__ == "__main__":
    Today().solve()
