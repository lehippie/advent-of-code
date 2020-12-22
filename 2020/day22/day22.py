"""Day 22: Crab Combat."""

from collections import deque
from copy import deepcopy
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

    @property
    def is_finished(self):
        decks_length = [len(deck) for deck in self.decks]
        if any(l == 0 for l in decks_length):
            return decks_length.index(max(decks_length))
        return None

    def play_round(self):
        cards = [deck.popleft() for deck in self.decks]
        winner = cards.index(max(cards))
        self.decks[winner].extend(sorted(cards, reverse=True))

    def play(self):
        while (winner := self.is_finished) is None:
            self.play_round()
        self.winner = winner

    @property
    def winner_score(self):
        assert self.winner is not None, "No winner yet."
        score = 0
        winner_deck = list(self.decks[self.winner])
        winner_deck.reverse()
        for k, card in enumerate(winner_deck):
            score += (k + 1) * card
        return score


def part_one(decks):
    game = Combat(decks)
    game.play()
    return game.winner_score


# --- Part Two ---

class RecursiveCombat(Combat):

    def __init__(self, decks):
        super().__init__(decks)
        self.history = []

    @property
    def deck_hash(self):
        return hash("|".join(
            str(",".join(str(card) for card in deck))
            for deck in self.decks
        ))

    @property
    def is_finished(self):
        if self.deck_hash in self.history:
            return 0
        return super().is_finished # is this working ?

    def play_round(self):
        self.history.append(self.deck_hash)
        cards = [deck.popleft() for deck in self.decks]
        if all(len(deck) >= cards[k] for k, deck in enumerate(self.decks)):
            sub_game = RecursiveCombat([
                deque(list(deck)[0:cards[k]])
                for k, deck in enumerate(self.decks)
            ])
            sub_game.play()
            winner = sub_game.winner
        else:
            winner = cards.index(max(cards))
        self.decks[winner].append(cards[winner])
        self.decks[winner].append(cards[int(not winner)])


def part_two(decks):
    game = RecursiveCombat(decks)
    game.play()
    return game.winner_score


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
    assert result_two
