"""--- Day 21: Keypad Conundrum ---"""

from functools import lru_cache
from itertools import combinations
from aoc.puzzle import Puzzle

DIRECTIONS = {1: "v", -1: "^", 1j: ">", -1j: "<"}
REVERSE = {"^": "v", "v": "^", "<": ">", ">": "<"}
NUMPAD = {
    "A": 3 + 2j,
    "0": 3 + 1j,
    "1": 2,
    "2": 2 + 1j,
    "3": 2 + 2j,
    "4": 1,
    "5": 1 + 1j,
    "6": 1 + 2j,
    "7": 0,
    "8": 1j,
    "9": 2j,
}
DIRPAD = {
    "A": 2j,
    "^": 1j,
    "v": 1 + 1j,
    "<": 1,
    ">": 1 + 2j,
}


def find_possible_paths(pad):
    """For each couple of keys, find all allowed paths from one to
    the other. Paths with alternating directions are not kept as
    it would induce too much back-and-forth moves on a parent
    directional pad.
    """
    paths = {key: {key: ["A"]} for key in pad}
    for start, end in combinations(pad, r=2):
        paths[start][end], paths[end][start] = set(), set()
        delta = pad[end] - pad[start]
        delta_row, delta_col = int(delta.real), int(delta.imag)
        n_row, n_col = abs(delta_row), abs(delta_col)
        updown = [delta_row // n_row for _ in range(n_row)]
        leftright = [delta_col // n_col * 1j for _ in range(n_col)]
        for moves in (updown + leftright, leftright + updown):
            position = pad[start]
            for move in moves:
                position += move
                if position not in pad.values():
                    break
            else:
                path = "".join(DIRECTIONS[m] for m in moves)
                paths[start][end].add(path + "A")
                paths[end][start].add("".join(REVERSE[m] for m in path[::-1]) + "A")
    return paths


class Today(Puzzle):
    def parser(self):
        self.numpaths = find_possible_paths(NUMPAD)
        self.dirpaths = find_possible_paths(DIRPAD)

    @lru_cache
    def get_length(self, path, depth=2):
        length = 0
        if depth == 1:
            return sum(
                min(len(p) for p in self.dirpaths[a][b])
                for a, b in zip("A" + path, path)
            )
        for a, b in zip("A" + path, path):
            length += min(self.get_length(p, depth - 1) for p in self.dirpaths[a][b])
        return length

    def part_one(self, depth=2):
        complexities = 0
        for code in self.input:
            length = 0
            for a, b in zip("A" + code, code):
                length += min(self.get_length(p, depth) for p in self.numpaths[a][b])
            complexities += length * int(code[:-1])
        return complexities

    def part_two(self):
        return self.part_one(25)


if __name__ == "__main__":
    Today().solve()
