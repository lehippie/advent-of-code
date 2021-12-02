"""Day 6: Custom Customs."""

from aoc.puzzle import Puzzle


class Puzzle06(Puzzle):
    def parser(self):
        groups = [[]]
        for line in self.input:
            if line:
                groups[-1].append(line)
            else:
                groups.append([])
        return groups

    def part_one(self):
        return sum(len(set("".join(g))) for g in self.input)

    def part_two(self):
        return sum(len(set.intersection(*map(set, g))) for g in self.input)


if __name__ == "__main__":
    Puzzle06(solutions=(6763, 3512)).solve()
