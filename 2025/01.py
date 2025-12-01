"""--- Day 1: Secret Entrance ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        password = 0
        dial = 50
        for instruction in self.input:
            direction = 1 if instruction[0] == "R" else -1
            clicks = int(instruction[1:])
            dial = (dial + direction * clicks) % 100
            if dial == 0:
                password += 1
        return password

    def part_two(self):
        password = 0
        dial = 50
        for instruction in self.input:
            direction = 1 if instruction[0] == "R" else -1
            clicks = int(instruction[1:])
            password += clicks // 100
            clicks = clicks % 100
            if dial == 0:
                dial = (dial + direction * clicks) % 100
            else:
                dial += direction * clicks
                if not 0 < dial < 100:
                    password += 1
                    dial %= 100
        return password


if __name__ == "__main__":
    Today().solve()
