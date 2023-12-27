"""--- Day 5: If You Give A Seed A Fertilizer ---"""

from aoc.puzzle import Puzzle


def apply(maps, ranges):
    """Maps are sorted so we compare each range to them one by
    one until we treat each value. During the process range's start
    is updated to keep track if there are values remaining inside.
    """
    ranges.sort(key=lambda r: r[0])
    next_ranges = []
    for rstart, rstop in ranges:
        for mstart, mstop, offset in maps:
            if rstop < mstart:  # range is before all maps
                break
            if rstart > mstop:  # range is after current map
                continue
            # Manage values before the map...
            if rstart < mstart:
                next_ranges.append((rstart, mstart - 1))
                rstart = mstart
            # ...and values inside the map
            if rstop <= mstop:
                next_ranges.append((rstart + offset, rstop + offset))
                rstart = None
                break
            else:
                next_ranges.append((rstart + offset, mstop + offset))
                rstart = mstop + 1
        # Add remaining values after checking all maps
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
        for n in self.seeds:
            for maps in self.almanac:
                try:
                    n += next(add for start, stop, add in maps if start <= n <= stop)
                except StopIteration:
                    pass
            locations.append(n)
        return min(locations)

    def part_two(self):
        ranges = [
            (start, start + end - 1)
            for start, end in zip(self.seeds[::2], self.seeds[1::2])
        ]
        for maps in self.almanac:
            ranges = apply(maps, ranges)
        return min(r[0] for r in ranges)


if __name__ == "__main__":
    Today().solve()
