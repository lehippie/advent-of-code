"""Day 25: Combo Breaker."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.keys = set(map(int, self.input))

    def part_one(self):
        """Transform the subject number 7 until the value becomes
        one of the public keys. Then, transform the other public
        key with the loop_size that was needed.
        """
        loop_size = 0
        value = 1
        while value not in self.keys:
            value = (value * 7) % 20201227
            loop_size += 1

        key = next(k for k in self.keys if k != value)
        value = 1
        for _ in range(loop_size):
            value = (value * key) % 20201227
        return value


solutions = (17673381, NotImplemented)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
