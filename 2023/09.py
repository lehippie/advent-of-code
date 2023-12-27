"""--- Day 9: Mirage Maintenance ---"""

from aoc.puzzle import Puzzle


def prediction(history):
    pred = history[-1]
    while history[-1] != 0:
        history = [h2 - h1 for h1, h2 in zip(history, history[1:])]
        pred += history[-1]
    return pred


def backward_prediction(history):
    pred = history[0]
    step = 0
    while any(history):
        step += 1
        history = [h2 - h1 for h1, h2 in zip(history, history[1:])]
        pred += -history[0] if step % 2 else history[0]
    return pred


class Today(Puzzle):
    def parser(self):
        self.histories = [list(map(int, l.split())) for l in self.input]

    def part_one(self):
        return sum(prediction(history) for history in self.histories)

    def part_two(self):
        return sum(backward_prediction(history) for history in self.histories)


if __name__ == "__main__":
    Today().solve()
