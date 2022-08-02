"""Day 2: Password Philosophy."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        def parse_line(line):
            values, letter, password = line.split(" ")
            return password, letter[0], *map(int, values.split("-"))

        self.passwords = [parse_line(l) for l in self.input]

    def part_one(self):
        return sum(v1 <= pwd.count(l) <= v2 for pwd, l, v1, v2 in self.passwords)

    def part_two(self):
        return sum(
            (pwd[v1 - 1] == l) != (pwd[v2 - 1] == l)
            for pwd, l, v1, v2 in self.passwords
        )


solutions = (628, 705)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
