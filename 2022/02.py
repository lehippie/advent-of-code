"""Day 2: Rock Paper Scissors."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.rounds = [r.split() for r in self.input]

    def part_one(self):
        trans = str.maketrans("XYZ", "ABC")
        score = 0
        for other, me in self.rounds:
            me = me.translate(trans)
            score += ord(me) - 64
            score += 3 * ((ord(me) - ord(other) + 1) % 3)
        return score

    def part_two(self):
        score = 0
        for other, outcome in self.rounds:
            o = ord(other) - 64
            if outcome == "X":
                score += o - 1 if other in "BC" else 3
            elif outcome == "Y":
                score += o + 3
            else:
                score += o + 7 if other in "AB" else 7
        return score


solutions = (13565, 12424)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
