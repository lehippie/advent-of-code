"""Day 22: Crab Combat."""

from collections import deque
from copy import deepcopy
from itertools import islice
from pathlib import Path


# --- Parsing input ---

def parse_input(filename):
    filepath = Path(__file__).parent / filename
    decks = [deque(), deque()]
    with open(filepath) as f:
        line = f.readline()
        while (line := f.readline()) != "\n":
            decks[0].append(int(line.rstrip()))
        assert "Player 2" in f.readline()
        for line in f:
            decks[1].append(int(line.rstrip()))
    return decks


# --- Part One ---

class Combat:
    def __init__(self, decks):
        self.decks = deepcopy(decks)
        self.winner = None

    def has_won(self):
        try:
            return next((k+1) % 2
                        for k, deck in enumerate(self.decks)
                        if len(deck) == 0)
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


def part_one(decks):
    game = Combat(decks)
    game.play()
    return game.score(game.winner)


# --- Part Two ---

class RecursiveCombat(Combat):

    def __init__(self, decks):
        super().__init__(decks)
        self.history = set()

    def deck_hash(self):
        return hash("|".join(
            str(",".join(str(card) for card in deck))
            for deck in self.decks
        ))

    def has_won(self):
        if (dh := self.deck_hash()) in self.history:
            return 0
        self.history.add(dh)
        return super().has_won()

    def play_round(self):
        cards = tuple(deck.popleft() for deck in self.decks)
        if all(len(deck) >= card for deck, card in zip(self.decks, cards)):
            sub_game = RecursiveCombat([
                deque(islice(deck, card))
                for deck, card in zip(self.decks, cards)
            ])
            sub_game.play()
            win = sub_game.winner
        else:
            win = cards.index(max(cards))
        self.decks[win].append(cards[win])
        self.decks[win].append(cards[(win+1) % 2])


def part_two(decks):
    game = RecursiveCombat(decks)
    game.play()
    return game.score(game.winner)


# --- Tests & Run ---

def tests():
    test = parse_input("test.txt")
    assert part_one(test) == 306
    assert part_two(test) == 291


if __name__ == "__main__":
    tests()

    puzzle_input = parse_input("decks.txt")

    result_one = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 32495

    result_two = part_two(puzzle_input)
    print(f"Part Two answer: {result_two}")
    assert result_two == 32665
