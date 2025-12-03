"""--- Day 3: Lobby ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def part_one(self):
        output = 0
        for bank in self.input:
            ten = max(bank[:-1])
            unit = max(bank[bank.index(ten) + 1 :])
            output += int(ten + unit)
        return output

    def part_two(self):
        output = 0
        for bank in self.input:
            jolts = []
            i = 0
            for j in range(11, 0, -1):
                jolts.append(max(bank[i:-j]))
                i += bank[i:].index(jolts[-1]) + 1
            jolts.append(max(bank[i:]))
            output += int("".join(jolts))
        return output


if __name__ == "__main__":
    Today().solve()
