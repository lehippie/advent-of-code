"""--- Day 13: Point of Incidence ---"""

from aoc.puzzle import Puzzle


def mirrored_line(pattern):
    for i in range(1, len(pattern)):
        if all(l1 == l2 for l1, l2 in zip(pattern[i:], pattern[i - 1 :: -1])):
            return i


def smudged_mirror_line(pattern):
    for i in range(1, len(pattern)):
        repaired = False
        difference = False
        for l1, l2 in zip(pattern[i:], pattern[i - 1 :: -1]):
            if l1 == l2:
                continue
            if not repaired and sum(m1 != m2 for m1, m2 in zip(l1, l2)) == 1:
                repaired = True
                continue
            difference = True
            break
        if repaired and not difference:
            return i


class Today(Puzzle):
    def parser(self):
        self.patterns = "\n".join(self.input).split("\n\n")
        self.patterns = [p.split("\n") for p in self.patterns]

    def part_one(self, detector=mirrored_line):
        total = 0
        for p in self.patterns:
            if l := detector(p):
                total += 100 * l
            else:
                r = ["".join(x[i] for x in p) for i in range(len(p[0]))]
                total += detector(r)
        return total

    def part_two(self):
        return self.part_one(detector=smudged_mirror_line)


solutions = (34202, 34230)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
