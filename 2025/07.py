"""--- Day 7: Laboratories ---"""

import re
from collections import defaultdict
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.beam = self.input[0].index("S")
        self.splitters = []
        for row in self.input[1:]:
            if "^" in row:
                self.splitters.append({m.start() for m in re.finditer(r"\^", row)})

    def part_one(self):
        splits = 0
        beams = set([self.beam])
        for splitters in self.splitters:
            next_beams = set()
            for beam in beams:
                if beam in splitters:
                    splits += 1
                    next_beams.add(beam - 1)
                    next_beams.add(beam + 1)
                else:
                    next_beams.add(beam)
            beams = next_beams
        return splits

    def part_two(self):
        beams = {self.beam: 1}
        for splitters in self.splitters:
            next_beams = defaultdict(int)
            for beam, n in beams.items():
                if beam in splitters:
                    next_beams[beam - 1] += n
                    next_beams[beam + 1] += n
                else:
                    next_beams[beam] += n
            beams = next_beams
        return sum(beams.values())


if __name__ == "__main__":
    Today().solve()
