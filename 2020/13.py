"""Day 13: Shuttle Search."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.start = int(self.input[0])
        self.buses = [
            (int(b), k) for k, b in enumerate(self.input[1].split(",")) if b != "x"
        ]

    def part_one(self):
        ts = {}
        for bus, _ in self.buses:
            ts[bus] = next(
                t for t in range(self.start, self.start + bus) if t % bus == 0
            )
        first_bus = min(ts, key=ts.get)
        return first_bus * (ts[first_bus] - self.start)

    def part_two(self):
        """We start with the timestamp where one bus arrive at the
        correct subsequent minute with a cycle time equal to its id.
        We then sync another bus by checking each cycle until its
        arrival minute is also correct. The cycle is then updated by
        multiplying it by the new bus id.
        One by one, we converge to the first timestamp where all
        buses arrive in correct order.
        """
        buses = sorted(self.buses, key=lambda x: x[0], reverse=True)
        t = buses[0][0] - buses[0][1]
        cycle = buses[0][0]
        for bus, delay in buses[1:]:
            while not (t + delay) % bus == 0:
                t += cycle
            cycle *= bus
        return t


solutions = (3789, 667437230788118)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
