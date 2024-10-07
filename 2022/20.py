"""Day 20: Grove Positioning System."""

from aoc.puzzle import Puzzle


def mix(numbers, times=1):
    """Positions of numbers are stored as the indexes of a list where
    the value is the position of the following number.
    Steps are computed beforehand, converting negative ones into
    their positive equivalents.
    """
    L = len(numbers) - 1
    steps = [abs(n) % L if n > 0 else L - (abs(n) % L) for n in numbers]
    links = [k + 1 for k in range(L)] + [0]
    for _ in range(times):
        for k, s in enumerate(steps):
            previous = links.index(k)
            links[previous] = links[k]
            destination = previous
            for _ in range(s):
                destination = links[destination]
            links[k] = links[destination]
            links[destination] = k
    return links


def decrypt(numbers, links):
    indexes = [numbers.index(0)]
    for _ in range(len(numbers) - 1):
        indexes.append(links[indexes[-1]])
    return sum(numbers[indexes[i % len(numbers)]] for i in (1000, 2000, 3000))


class Today(Puzzle):
    def parser(self):
        self.file = list(map(int, self.input))

    def part_one(self):
        return decrypt(self.file, mix(self.file))

    def part_two(self):
        new_file = [811589153 * n for n in self.file]
        return decrypt(new_file, mix(new_file, 10))


if __name__ == "__main__":
    Today().solve()
