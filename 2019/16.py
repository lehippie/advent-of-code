"""--- Day 16: Flawed Frequency Transmission ---"""

from aoc.puzzle import Puzzle


def gen(k, limit, plus=True):
    """From position k, generate the signal portions to add or substract."""
    if plus:
        start, stop = k, 2 * k + 1
    else:
        start, stop = 3 * k + 2, 4 * k + 3
    step = 4 * k + 4
    while start < limit:
        yield (start, min(stop, limit))
        start += step
        stop += step


class Today(Puzzle):
    def parser(self):
        self.signal = list(map(int, self.input))

    def part_one(self):
        """Repeating digits from the 0,1,0,-1 pattern while skipping the first 0
        is the same as repeating 1,0,-1,0 starting at the position to calculate.
        Thus, a new value is independent from the values before it.
        Portions of signals to add or substract are determined from a cumulative
        sum to limit duplicate calculations.
        """
        signal = self.signal.copy()
        N = len(signal)
        for _ in range(100):
            csum = [0]
            for v in signal:
                csum.append(csum[-1] + v)

            for k in range(N):
                signal[k] = (
                    abs(
                        sum(csum[b] - csum[a] for a, b in gen(k, N))
                        - sum(csum[b] - csum[a] for a, b in gen(k, N, False))
                    )
                    % 10
                )
        return int("".join(map(str, signal[:8])))

    def part_two(self):
        """For indices higher than half the signal's length applying fft is the
        same as summing each value after the index.
        The input is 650 digits long, so the real signal is 6500000 digits long.
        The offset places the useful message in the second half of the signal,
        meaning that a new value is simply defined by the sum of itself and the
        following digits as there won't be any zeros or minus-ones.
        """
        offset = int(self.input[:7])
        signal = (self.signal * 10000)[offset:]
        for _ in range(100):
            csum = [signal[-1]]
            for v in reversed(signal[:-1]):
                csum.append(csum[-1] + v)
            signal = [v % 10 for v in reversed(csum)]
        return int("".join(map(str, signal[:8])))


if __name__ == "__main__":
    Today().solve()
