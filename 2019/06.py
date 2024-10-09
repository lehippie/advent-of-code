"""--- Day 6: Universal Orbit Map ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.map = {}
        for orbit in self.input:
            objs = orbit.split(")")
            self.map[objs[1]] = objs[0]

    def part_one(self):
        self.orbits = {}
        for obj in self.map:
            self.orbits[obj] = [self.map[obj]]
            while self.orbits[obj][-1] != "COM":
                self.orbits[obj].append(self.map[self.orbits[obj][-1]])
        return sum(len(path) for path in self.orbits.values())

    def part_two(self):
        return len(set(self.orbits["YOU"]).symmetric_difference(self.orbits["SAN"]))


if __name__ == "__main__":
    Today().solve()
