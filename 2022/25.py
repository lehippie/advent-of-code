"""Day 25: Full of Hot Air."""

from aoc.puzzle import Puzzle


S2D = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
D2S = {v: k for k, v in S2D.items()}


def snafu2dec(snafu):
    decimal = 0
    for s, k in zip(snafu[::-1], range(len(snafu))):
        decimal += S2D[s] * 5**k
    return decimal


def dec2snafu(decimal):
    kmax = next(k for k in range(100) if 5**k > decimal)
    values = []
    for k in range(kmax, -1, -1):
        values.append(decimal // 5**k)
        decimal = decimal % 5**k
    while True:
        try:
            index = next(i for i, v in enumerate(values[::-1]) if v not in D2S)
            index = len(values) - 1 - index
            values[index] -= 5
            values[index - 1] += 1
        except StopIteration:
            return "".join(D2S[v] for v in values).lstrip("0")


class Today(Puzzle):
    def part_one(self):
        return dec2snafu(sum(snafu2dec(s) for s in self.input))


if __name__ == "__main__":
    Today().solve()
