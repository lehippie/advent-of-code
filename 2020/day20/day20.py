"""Day 20: Jurassic Jigsaw."""

import re
from collections import Counter
from itertools import combinations, product
from math import prod, sqrt
from pathlib import Path


INPUT_FILE = "tiles.txt"

def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = ''.join(f.readlines()).split("\n\n")
    tiles = {}
    for d in data:
        lines = d.rstrip().split("\n")
        tiles[int(re.findall(r"\d+", lines[0])[0])] = lines[1:]
    return tiles


# --- Part One ---

class Tile:
    def __init__(self, tile_id, tile):
        self.id = tile_id
        self.tile = tile
        self.connections = {}

    @property
    def edges(self):
        return {
            "0": self.tile[0],
            "-0": self.tile[0][::-1],
            "1": "".join(line[-1] for line in self.tile),
            "-1": "".join(line[-1] for line in self.tile)[::-1],
            "2": self.tile[-1],
            "-2": self.tile[-1][::-1],
            "3": "".join(line[0] for line in self.tile),
            "-3": "".join(line[0] for line in self.tile)[::-1],
        }

    def check_connection(self, other_tile):
        edges = set(self.edges.values())
        other_edges = set(other_tile.edges.values())
        same = edges.intersection(other_edges)
        if same:
            same = same.pop()
            mine = next(k for k, e in self.edges.items() if e == same)
            hers = next(k for k, e in other_tile.edges.items() if e == same)
            self.connections[abs(int(mine))] = other_tile.id
            other_tile.connections[abs(int(hers))] = self.id

    def rotate(self):
        self.tile = [
            "".join(line[i] for line in self.tile[::-1])
            for i in range(len(self.tile[0]))
        ]
        self.connections = {(e+1)%4: t for e, t in self.connections.items()}

    def flip_lr(self):
        self.tile = [line[::-1] for line in self.tile]
        self.connections = {(e+2)%4 if e%2 else e: t
                            for e, t in self.connections.items()}

    def flip_ud(self):
        self.tile = self.tile[::-1]
        self.connections = {(e+2)%4 if not e%2 else e: t
                            for e, t in self.connections.items()}


class Image:
    def __init__(self, tiles):
        self.tiles = {tid: Tile(tid, t) for tid, t in tiles.items()}
        self.find_connections()
        self.corners = [tile.id for tile in self.tiles.values()
                        if len(tile.connections) == 2]
        self.checksum = prod(self.corners)
        self.form_image()

    def find_connections(self):
        for tileA, tileB in combinations(self.tiles.values(), 2):
            tileA.check_connection(tileB)

    def fill_line(self, starting_tile):
        ids = [starting_tile.id]
        try:
            while True:
                next_tile = self.tiles[starting_tile.connections[1]]
                edge = next(e for e, i in next_tile.connections.items()
                            if i == starting_tile.id)
                for _ in range(3 - edge):
                    next_tile.rotate()
                if next_tile.edges["3"] != starting_tile.edges["1"]:
                    next_tile.flip_ud()
                ids.append(next_tile.id)
                starting_tile = next_tile
        except KeyError:
            return ids

    def fill_column(self, starting_tile):
        ids = [starting_tile.id]
        try:
            while True:
                next_tile = self.tiles[starting_tile.connections[2]]
                edge = next(e for e, i in next_tile.connections.items()
                            if i == starting_tile.id)
                for _ in range((4 - edge) % 4):
                    next_tile.rotate()
                if next_tile.edges["0"] != starting_tile.edges["2"]:
                    next_tile.flip_lr()
                ids.append(next_tile.id)
                starting_tile = next_tile
        except KeyError:
            return ids

    def form_image(self):
        size = int(sqrt(len(self.tiles)))
        self.layout = [[] for _ in range(size)]
        # Place first corner
        corner = self.tiles[self.corners[0]]
        while set(corner.connections) != {1, 2}:
            corner.rotate()
        # Fill first line
        self.layout[0] = self.fill_line(corner)
        # Fill each column
        for t in self.layout[0]:
            column_ids = self.fill_column(self.tiles[t])
            for k, cid in enumerate(column_ids):
                if k != 0:
                    self.layout[k].append(cid)
        # Final image
        self.image = []
        for ids in self.layout:
            tiles = [self.tiles[tid].tile for tid in ids]
            for k, t in enumerate(tiles):
                tiles[k] = t[1:-1]
                tiles[k] = [line[1:-1] for line in tiles[k]]
            self.image.extend(["".join(lines) for lines in zip(*tiles)])


def part_one(tiles):
    return Image(tiles)


# --- Part Two ---

def part_two(image: Image):
    sea = Tile(0, image.image)
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    monsters_found = []
    rotations_tested = 0
    while True:
        size = (len(monster), len(monster[0]))
        hashes = [[r, c] for r, c in product(range(size[0]), range(size[1]))
                        if monster[r][c] == "#"]
        for r, c in product(
            range(0, len(sea.tile) - size[0] + 1),
            range(0, len(sea.tile[0]) - size[1] + 1)
        ):
            coords = [[r+x, c+y] for x, y in hashes]
            if "".join(sea.tile[x][y] for x, y in coords) == "#"*len(hashes):
                monsters_found.append((r, c))
                for x, y in coords:
                    sea.tile[x] = f"{sea.tile[x][:y]}O{sea.tile[x][y+1:]}"
        if monsters_found:
            break
        rotations_tested += 1
        sea.rotate()
        if rotations_tested == 4:
            sea.flip_ud()
    # print("\n".join(sea.tile))
    return Counter("".join(sea.tile))["#"]


# --- Tests & Run ---

def tests():
    # Part One
    test = part_one(load_input("test.txt"))
    assert test.checksum == 20899048083289
    # Part Two
    roughness = part_two(test)
    assert roughness == 273


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    image = part_one(puzzle_input)
    print(f"Part One answer: {image.checksum}")
    assert image.checksum == 54755174472007

    result_two = part_two(image)
    print(f"Part Two answer: {result_two}")
    assert result_two == 1692
