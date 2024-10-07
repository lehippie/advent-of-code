"""Day 21: Dirac Dice."""

from collections import Counter, defaultdict
from itertools import cycle, product
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.start = tuple(int(line.split()[-1]) for line in self.input)

    def part_one(self):
        positions = list(self.start)
        scores = [0, 0]
        dice = cycle(range(1, 101))
        rolls = 0
        player = 0
        while all(score < 1000 for score in scores):
            result = sum(next(dice) for _ in range(3))
            rolls += 3
            positions[player] = (positions[player] + result) % 10 or 10
            scores[player] += positions[player]
            player = (player + 1) % 2
        return min(scores) * rolls

    def part_two(self):
        """Each triple rolls splits in the same amount of universes,
        with a resulting sum of rolls that are identical. Thus, these
        outcomes are precalculated before starting the game.

        A game state reduces to player's positions, scores and the
        next player to roll. Games in progress are stored in a dict
        where values are the amount of universes in this state.
        """
        quantum_rolls = Counter(sum(rolls) for rolls in product(range(1, 4), repeat=3))
        wins = [0, 0]
        games = {self.start + (0, 0, 0): 1}
        while games:
            new_games = defaultdict(int)
            for state, n_games in games.items():
                player = state[-1]
                for roll, n_roll in quantum_rolls.items():
                    positions = list(state[0:2])
                    scores = list(state[2:-1])
                    positions[player] = (positions[player] + roll) % 10 or 10
                    scores[player] += positions[player]
                    if scores[player] >= 21:
                        wins[player] += n_games * n_roll
                    else:
                        new_state = tuple(positions + scores + [(player + 1) % 2])
                        new_games[new_state] += n_games * n_roll
            games = new_games
        return max(wins)


if __name__ == "__main__":
    Today().solve()
