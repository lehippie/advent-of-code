"""--- Day 5: If You Give A Seed A Fertilizer ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.almanac = []
        for line in self.input:
            if "seeds:" in line:
                self.seeds = list(map(int, line.split(" ")[1:]))
                continue
            elif "map" in line:
                self.almanac.append([])
                continue
            elif line:
                self.almanac[-1].append(tuple(map(int, line.split(" "))))

    def part_one(self):
        locations = []
        for val in self.seeds:
            for maps in self.almanac:
                try:
                    mapping = next(m for m in maps if m[1] <= val < m[1] + m[2])
                    val += mapping[0] - mapping[1]
                except StopIteration:
                    pass
            locations.append(val)
        return min(locations)

    def part_two(self):
        return super().part_two()


solutions = (309796150, None)

if __name__ == "__main__":
    # Today(infile="test.txt", solutions=(35, None)).solve()
    Today(solutions=solutions).solve()
