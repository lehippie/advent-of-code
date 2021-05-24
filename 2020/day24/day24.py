"""Day 24: Lobby Layout."""

import re
from pathlib import Path


# --- Parsing input ---

def parse_input(filename):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        data = [re.findall(r"[ns]?[ew]", line) for line in f]
    return data


# --- Part One ---

def part_one(tiles):
    blacks = set()
    for tile in tiles:
        x, y = 0, 0
        for step in tile:
            if step == "e":
                x += 1
            elif step == "se":
                x += 1
                y -= 1
            elif step == "sw":
                y -= 1
            elif step == "w":
                x -= 1
            elif step == "nw":
                x -= 1
                y += 1
            elif step == "ne":
                y += 1
        if (x, y) in blacks:
            blacks.remove((x, y))
        else:
            blacks.add((x, y))
    return blacks


# --- Part Two ---

def neighbors(x, y):
    return {(x+1, y), (x+1, y-1), (x, y-1), (x-1, y), (x-1, y+1), (x, y+1)}


def part_two(blacks):
    for _ in range(100):
        next_blacks = set()
        whites_to_check = set()
        for black in blacks:
            around = neighbors(*black)
            if len(around.intersection(blacks)) in {1, 2}:
                next_blacks.add(black)
            whites_to_check.update(around.difference(blacks))
        for white in whites_to_check:
            if len(neighbors(*white).intersection(blacks)) == 2:
                next_blacks.add(white)
        blacks = next_blacks
    return len(blacks)


# --- Tests & Run ---

def tests():
    test = parse_input("test.txt")
    test = part_one(test)
    assert len(test) == 10
    assert part_two(test) == 2208


if __name__ == "__main__":
    tests()

    puzzle_input = parse_input("tiles.txt")

    result_one = part_one(puzzle_input)
    print("Part One answer:", len(result_one))
    assert len(result_one) == 436

    result_two = part_two(result_one)
    print("Part Two answer:", result_two)
    assert result_two == 4133
