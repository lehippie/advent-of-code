"""--- Day 5: Cafeteria ---"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.freshs = []
        self.ingredients = []
        for line in self.input:
            if "-" in line:
                self.freshs.append(list(map(int, line.split("-"))))
            elif line:
                self.ingredients.append(int(line))

    def part_one(self):
        def is_fresh(ingredient):
            for fresh in self.freshs:
                if fresh[0] <= ingredient <= fresh[1]:
                    return True
            return False

        return sum(is_fresh(ingredient) for ingredient in self.ingredients)

    def part_two(self):
        fresh_ids = 0
        freshs = sorted(self.freshs, key=lambda f: f[0])
        while len(freshs) > 1:
            amin, amax = freshs[0]
            bmin, bmax = freshs[1]
            if amax < bmin:
                fresh_ids += amax - amin + 1
                del freshs[0]
            elif bmax < amax:
                del freshs[1]
            else:
                freshs[0][1] = bmax
                del freshs[1]
        fresh_ids += freshs[0][1] - freshs[0][0] + 1
        return fresh_ids


if __name__ == "__main__":
    Today().solve()
