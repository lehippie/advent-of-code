"""Day 22: Crab Combat."""

from collections import deque
from itertools import islice
from aoc.puzzle import Puzzle


class Combat:
    def __init__(self, decks):
        self.decks = [deque(deck) for deck in decks]
        self.winner = None

    def play(self):
        while self.winner is None:
            self.play_round()

    def play_round(self):
        cards = [deck.popleft() for deck in self.decks]
        win = cards.index(max(cards))
        self.decks[win].extend((cards[win], cards[(win + 1) % 2]))
        if not all(self.decks):
            self.winner = next(k for k, d in enumerate(self.decks) if d)

    def score(self):
        deck = self.decks[self.winner]
        return sum(k * card for k, card in zip(range(len(deck), 0, -1), deck))


class RecursiveCombat(Combat):
    def __init__(self, decks):
        super().__init__(decks)
        self.history = set()

    def play_round(self):
        state = tuple(map(tuple, self.decks))
        if state in self.history:
            self.winner = 0
        else:
            self.history.add(state)
            cards = [deck.popleft() for deck in self.decks]
            if all(len(deck) >= card for deck, card in zip(self.decks, cards)):
                sub_game = RecursiveCombat(
                    [list(islice(d, card)) for d, card in zip(self.decks, cards)]
                )
                sub_game.play()
                win = sub_game.winner
            else:
                win = cards.index(max(cards))
            self.decks[win].extend((cards[win], cards[(win + 1) % 2]))
            if not all(self.decks):
                self.winner = next(k for k, d in enumerate(self.decks) if d)


class Today(Puzzle):
    def parser(self):
        idx = self.input.index("")
        self.decks = [
            list(map(int, self.input[1:idx])),
            list(map(int, self.input[idx + 2 :])),
        ]

    def part_one(self, game=Combat):
        g = game(self.decks)
        g.play()
        return g.score()

    def part_two(self):
        return self.part_one(RecursiveCombat)


if __name__ == "__main__":
    Today().solve()
