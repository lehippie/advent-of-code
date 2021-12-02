"""Day 22: Crab Combat."""

from collections import deque
from copy import deepcopy
from itertools import islice
from aoc.puzzle import Puzzle


class Combat:
    def __init__(self, decks):
        self.decks = deepcopy(decks)
        self.winner = None

    def has_won(self):
        try:
            return next(
                (k + 1) % 2 for k, deck in enumerate(self.decks) if len(deck) == 0
            )
        except StopIteration:
            return None

    def play_round(self):
        cards = tuple(deck.popleft() for deck in self.decks)
        win = cards.index(max(cards))
        self.decks[win].extend(sorted(cards, reverse=True))

    def play(self):
        while (player := self.has_won()) is None:
            self.play_round()
        self.winner = player

    def score(self, player):
        score = 0
        deck = self.decks[player]
        for k, card in zip(range(len(deck), 0, -1), deck):
            score += k * card
        return score


class RecursiveCombat(Combat):
    def __init__(self, decks):
        super().__init__(decks)
        self.history = set()

    def deck_hash(self):
        return (self.score(0), self.score(1))

    def has_won(self):
        if (dh := self.deck_hash()) in self.history:
            return 0
        self.history.add(dh)
        return super().has_won()

    def play_round(self):
        cards = tuple(deck.popleft() for deck in self.decks)
        if all(len(deck) >= card for deck, card in zip(self.decks, cards)):
            sub_game = RecursiveCombat(
                [deque(islice(deck, card)) for deck, card in zip(self.decks, cards)]
            )
            sub_game.play()
            win = sub_game.winner
        else:
            win = cards.index(max(cards))
        self.decks[win].append(cards[win])
        self.decks[win].append(cards[(win + 1) % 2])


class Puzzle22(Puzzle):
    def parser(self):
        decks = [deque(), deque()]
        lines = iter(self.input)
        line = next(lines)
        while line := next(lines):
            decks[0].append(int(line))
        assert "Player 2" in next(lines)
        for line in lines:
            decks[1].append(int(line))
        return decks

    def part_one(self):
        game = Combat(self.input)
        game.play()
        return game.score(game.winner)

    def part_two(self):
        game = RecursiveCombat(self.input)
        game.play()
        return game.score(game.winner)


if __name__ == "__main__":
    Puzzle22(solutions=(32495, 32665)).solve()
