"""--- Day 4: Scratchcards ---"""

import re
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.cards = []
        for line in self.input:
            _, card = line.split(":")
            self.cards.append(
                [re.findall(r"\d+", numbers) for numbers in card.split("|")]
            )

    def part_one(self):
        points = 0
        for card in self.cards:
            if win := len(set(card[0]).intersection(card[1])):
                points += 2 ** (win - 1)
        return points

    def part_two(self):
        scratchcards = [1] * len(self.cards)
        for (card_number, card), amount in zip(enumerate(self.cards), scratchcards):
            win = len(set(card[0]).intersection(card[1]))
            for below in range(win):
                scratchcards[card_number + below + 1] += amount
        return sum(scratchcards)


if __name__ == "__main__":
    Today().solve()
