"""Day 21: Dirac Dice."""

from collections import Counter, defaultdict
from itertools import cycle, product
from aoc.puzzle import Puzzle


class DiracDice:
    def __init__(self, starting_positions):
        self.positions = list(starting_positions)
        self.n_players = len(self.positions)
        self.scores = [0] * self.n_players
        self.turn = 0
        self.dice = cycle(range(1, 101))

    def has_ended(self):
        return max(self.scores) >= 1000

    def next_turn(self):
        roll = sum(next(self.dice) for _ in range(3))
        player = self.turn % self.n_players
        self.positions[player] = (self.positions[player] + roll) % 10 or 10
        self.scores[player] += self.positions[player]
        self.turn += 1


class Puzzle21(Puzzle):
    def parser(self):
        return tuple(int(line.split()[-1]) for line in self.input)

    def part_one(self):
        game = DiracDice(self.input)
        while not game.has_ended():
            game.next_turn()
        return min(game.scores) * 3 * game.turn

    def part_two(self):
        n_players = len(self.input)
        quantum_rolls = Counter(sum(rolls) for rolls in product(range(1, 4), repeat=3))
        wins = [0] * n_players
        games = {self.input + (0,) * n_players + (0,): 1}
        while games:
            _games = defaultdict(int)
            for state, n_games in games.items():
                player = state[-1]
                for roll, n_roll in quantum_rolls.items():
                    positions = list(state[0:n_players])
                    scores = list(state[n_players:-1])
                    positions[player] = (positions[player] + roll) % 10 or 10
                    scores[player] += positions[player]
                    if scores[player] >= 21:
                        wins[player] += n_games * n_roll
                    else:
                        _state = tuple(positions + scores + [(player + 1) % n_players])
                        _games[_state] += n_games * n_roll
            games = _games
        return max(wins)


if __name__ == "__main__":
    Puzzle21(solutions=(503478, 716241959649754)).solve()