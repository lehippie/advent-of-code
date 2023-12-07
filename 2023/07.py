"""--- Day 7: Camel Cards ---"""

from collections import Counter
from aoc.puzzle import Puzzle


LABELS = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
LABELS.update({str(n): n for n in range(2, 10)})


def hand_type(count):
    c = count.most_common(2)
    if c[0][1] == 5:
        return 7
    elif c[0][1] == 4:
        return 6
    elif c[0][1] == 3:
        if c[1][1] == 2:
            return 5
        return 4
    elif c[0][1] == 2:
        if c[1][1] == 2:
            return 3
        return 2
    elif c[0][1] == 1:
        return 1


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = hand_type(Counter(hand))

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for label, otherlabel in zip(self.hand, other.hand):
            if label != otherlabel:
                return LABELS[label] < LABELS[otherlabel]


class JokerHand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        count = Counter(hand)
        if "J" in hand and len(count) > 1:
            j = count.pop("J")
            count[max(count, key=count.get)] += j
        self.type = hand_type(count)

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for label, otherlabel in zip(self.hand, other.hand):
            if label != otherlabel:
                label = 0 if label == "J" else LABELS[label]
                otherlabel = 0 if otherlabel == "J" else LABELS[otherlabel]
                return label < otherlabel


class Today(Puzzle):
    def part_one(self, hand_type=Hand):
        hands = sorted(hand_type(*line.split()) for line in self.input)
        return sum((i + 1) * h.bid for i, h in enumerate(hands))

    def part_two(self):
        return self.part_one(hand_type=JokerHand)


solutions = (247961593, 248750699)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
