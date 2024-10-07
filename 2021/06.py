"""Day 6: Lanternfish."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self, days=80):
        """Positions are irrelevant. Only the amount of each timer
        matters. We use a list where the index is the timer and
        the value is the count of fishes.
        """
        timers = [self.input.count(str(k)) for k in range(9)]
        for _ in range(days):
            timers = timers[1:] + timers[:1]
            timers[6] += timers[-1]
        return sum(timers)

    def part_two(self):
        return self.part_one(256)


if __name__ == "__main__":
    Today().solve()
