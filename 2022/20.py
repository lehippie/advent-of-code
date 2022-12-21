"""Day 20: Grove Positioning System."""

from aoc.puzzle import Puzzle


def mix(steps, links):
    for k, s in enumerate(steps):
        if s == 0:
            continue
        links[links.index(k)] = links[k]
        destination = k
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
        """Positions of numbers are stored as the indexes of a list
        where the value is the position of the following number.
        Steps are computed beforehand, converting negative ones into
        their positive equivalents.
        """
        L = len(self.file) - 1
        steps = [abs(n) % L if n > 0 else L - (abs(n) % L) for n in self.file]
        links = [k + 1 for k in range(L)] + [0]
        links = mix(steps, links)
        return decrypt(self.file, links)

    def part_two(self):
        new_file = [811589153 * n for n in self.file]
        L = len(new_file) - 1
        steps = [abs(n) % L if n > 0 else L - (abs(n) % L) for n in new_file]
        links = [k + 1 for k in range(L)] + [0]
        for _ in range(10):
            links = mix(steps, links)
        return decrypt(new_file, links)


solutions = (5498, 3390007892081)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
