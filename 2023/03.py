"""--- Day 3: Gear Ratios ---"""

import re
from collections import defaultdict
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        parts_sum = 0
        for l, line in enumerate(self.input):
            for part in re.finditer(r"\d+", line):
                start, end = part.span()
                arounds = set()
                # Add the character before, ...
                if start != 0:
                    arounds.add(line[start - 1])
                    start -= 1
                # ... the character after, ...
                if end != len(line):
                    arounds.add(line[end])
                    end += 1
                # ... the line above, ...
                if l != 0:
                    arounds.update(self.input[l - 1][start:end])
                # ... the line below, ...
                if l != len(self.input) - 1:
                    arounds.update(self.input[l + 1][start:end])
                # ... and check if there is a symbol.
                if arounds.difference("."):
                    parts_sum += int(part[0])
        return parts_sum

    def part_two(self):
        """For gears, parts that are adjacent to a * are saved in a
        dict where the key is the coordinates of the gear. This dict
        is then filtered to keep the ones with only 2 adjacent parts.
        """
        gears = defaultdict(list)
        for l, line in enumerate(self.input):
            for part in re.finditer(r"\d+", line):
                start, end = part.span()
                # Check the character before, ...
                if start != 0:
                    if line[start - 1] == "*":
                        gears[(l, start - 1)].append(int(part[0]))
                    start -= 1
                # ... the character after, ...
                if end != len(line):
                    if line[end] == "*":
                        gears[(l, end)].append(int(part[0]))
                    end += 1
                # ... the line above, ...
                if l != 0:
                    for gear in re.finditer(r"\*", self.input[l - 1][start:end]):
                        gears[(l - 1, start + gear.start())].append(int(part[0]))
                # ... and the line below.
                if l != len(self.input) - 1:
                    for gear in re.finditer(r"\*", self.input[l + 1][start:end]):
                        gears[(l + 1, start + gear.start())].append(int(part[0]))

        return sum(parts[0] * parts[1] for parts in gears.values() if len(parts) == 2)


if __name__ == "__main__":
    Today().solve()
