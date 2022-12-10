"""Day 10: Cathode-Ray Tube."""

from hashlib import md5
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        self.x = [1]
        for instr in self.input:
            self.x.append(self.x[-1])
            if "addx" in instr:
                self.x.append(self.x[-1] + int(instr[5:]))
        return sum(c * self.x[c - 1] for c in range(20, len(self.x), 40))

    def part_two(self):
        screen = ""
        for c in range(240):
            screen += "#" if self.x[c] - 1 <= c % 40 <= self.x[c] + 1 else " "
        screen = "\n".join(screen[40 * k : 40 * (k + 1)] for k in range(6))
        # print(screen)
        return md5(screen.encode()).hexdigest()


solutions = (13520, "10f996f2a7086790b6b2e7b9dc7e2e60")

if __name__ == "__main__":
    Today(solutions=solutions).solve()
