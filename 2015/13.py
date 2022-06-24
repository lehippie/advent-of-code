"""Day 13: Knights of the Dinner Table."""

from collections import defaultdict
from copy import deepcopy
from itertools import permutations
from aoc.puzzle import Puzzle


def table_arrangements(attendees):
    """Tables are cyclic so possible arrangements are
    permutations of attendees when one of them is fixed.
    """
    for p in permutations(attendees[1:]):
        yield [attendees[0]] + list(p)


def max_happiness(happiness: dict):
    nb_attendees = len(happiness)
    best_table = 0
    for table in table_arrangements(list(happiness)):
        table_happiness = 0
        for i, attendee in enumerate(table):
            right = table[(i + 1) % nb_attendees]
            left = table[i - 1]
            table_happiness += happiness[attendee][right]
            table_happiness += happiness[attendee][left]
        if table_happiness > best_table:
            best_table = table_happiness
    return best_table


class Today(Puzzle):
    def parser(self):
        self.attendees = defaultdict(dict)
        for line in self.input:
            words = line.split()
            if words[2] == "gain":
                self.attendees[words[0]][words[-1][:-1]] = int(words[3])
            if words[2] == "lose":
                self.attendees[words[0]][words[-1][:-1]] = -int(words[3])

    def part_one(self):
        return max_happiness(self.attendees)

    def part_two(self):
        me_included = deepcopy(self.attendees)
        for attendee in self.attendees:
            me_included[attendee]["me"] = 0
            me_included["me"][attendee] = 0
        return max_happiness(me_included)


solutions = (664, 640)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
