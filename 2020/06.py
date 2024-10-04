"""Day 6: Custom Customs."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.groups = [[]]
        for line in self.input:
            if line:
                self.groups[-1].append(line)
            else:
                self.groups.append([])

    def part_one(self):
        """Put every answers in a set and get its length."""
        return sum(len(set("".join(g))) for g in self.groups)

    def part_two(self):
        """Return the length of the intersection of answers."""
        return sum(len(set.intersection(*map(set, g))) for g in self.groups)


if __name__ == "__main__":
    Today().solve()
