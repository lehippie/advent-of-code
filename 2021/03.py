"""Day 3: Binary Diagnostic."""

from collections import Counter
from aoc.puzzle import Puzzle


def gas_filtering(numbers, method):
    """Filter numbers according to given <method>. If the amounts of
    0s and 1s are equal, adding a '1' in the count ensure that 'max'
    will keep 1s and 'min' will keep 0s.
    """
    k = 0
    while len(numbers) > 1:
        count = Counter(n[k] for n in numbers)
        if count["0"] == count["1"]:
            count.update("1")
        numbers = [n for n in numbers if n[k] == method(count, key=count.get)]
        k += 1
    return numbers[0]


class Today(Puzzle):
    def part_one(self):
        """Keeping numbers as strings, we count the amounts of 1s and
        0s for each bit position. Gamma and epsilon strings are
        recreated by keeping most and least commons digits before
        converting them to integer for multiplication.
        """
        counts = [Counter() for _ in range(len(self.input[0]))]
        for number in self.input:
            [counts[k].update(n) for k, n in enumerate(number)]
        gamma = "".join(max(count, key=count.get) for count in counts)
        epsilon = "".join(min(count, key=count.get) for count in counts)
        return int(gamma, base=2) * int(epsilon, base=2)

    def part_two(self):
        """Oxygen and CO2 ratings are found by filtering input numbers
        with max or min methods, respectively.
        """
        oxy = gas_filtering(self.input, method=max)
        co2 = gas_filtering(self.input, method=min)
        return int(oxy, base=2) * int(co2, base=2)


solutions = (1082324, 1353024)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
