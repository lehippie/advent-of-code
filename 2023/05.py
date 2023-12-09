"""--- Day 5: If You Give A Seed A Fertilizer ---"""

from aoc.puzzle import Puzzle


def apply(maps, ranges):
    ranges.sort(key=lambda r: r[0])
    next_ranges = []
    for rstart, rstop in ranges:
        for mstart, mstop, offset in maps:
            if rstop < mstart:
                break
            if rstart > mstop:
                continue
            if rstart < mstart:
                next_ranges.append((rstart, mstart - 1))
                rstart = mstart
            if rstop <= mstop:
                next_ranges.append((rstart + offset, rstop + offset))
                rstart = None
                break
            else:
                next_ranges.append((rstart + offset, mstop + offset))
                rstart = mstop + 1
        if rstart is not None:
            next_ranges.append((rstart, rstop))
    return next_ranges


class Today(Puzzle):
    def parser(self):
        self.seeds = list(map(int, self.input[0].split(" ")[1:]))
        self.almanac = []
        for line in self.input[2:]:
            if "map" in line:
                self.almanac.append([])
            elif line:
                dest, source, length = map(int, line.split(" "))
                self.almanac[-1].append((source, source + length - 1, dest - source))
        for maps in self.almanac:
            maps.sort(key=lambda m: m[0])

    def part_one(self):
        locations = []
        for number in self.seeds:
            for maps in self.almanac:
                try:
                    number += next(
                        offset
                        for start, stop, offset in maps
                        if start <= number <= stop
                    )
                except StopIteration:
                    pass
            locations.append(number)
        return min(locations)

    def part_two(self):
        ranges = [
            (start, start + end - 1)
            for start, end in zip(self.seeds[::2], self.seeds[1::2])
        ]
        for maps in self.almanac:
            ranges = apply(maps, ranges)
        return min(r[0] for r in ranges)


solutions = (309796150, 50716416)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
