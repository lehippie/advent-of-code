"""Day 20: Jurassic Jigsaw."""

from collections import Counter
from itertools import combinations, product
from math import prod
from aoc.puzzle import Puzzle


MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


class Tile:
    def __init__(self, tile_id, lines):
        self.id = tile_id
        self.lines = lines
        self.size = len(self.lines)
        self.links = {}

    @property
    def borders(self):
        """Return borders of the tile. Directions are indexed
        clockwise: up=0, right=1, down=2, left=3.
        """
        return {
            0: self.lines[0],
            1: "".join(line[-1] for line in self.lines),
            2: self.lines[-1],
            3: "".join(line[0] for line in self.lines),
        }

    def flip(self):
        """Flip upside-down."""
        self.lines = self.lines[::-1]
        self.links = {d if d % 2 else (d + 2) % 4: t for d, t in self.links.items()}

    def rotate(self):
        """Rotate 90° clockwise."""
        self.lines = ["".join(l[i] for l in self.lines[::-1]) for i in range(self.size)]
        self.links = {(d + 1) % 4: t for d, t in self.links.items()}

    def align(self, other, direction):
        """Align an other tile along a direction."""
        border = self.borders[direction]
        other_direction = (direction + 2) % 4
        test_count = 0
        while other.borders[other_direction] != border:
            test_count += 1
            if test_count != 4:
                other.rotate()
            else:
                other.flip()


class Image:
    def __init__(self, tiles):
        self.tiles = tiles
        self.find_links()
        self.arrange_tiles()
        self.checksum = prod(self.grid[r][c].id for r, c in product((0, -1), repeat=2))

    def find_links(self):
        """For each couple of tiles, search for a common border and
        save the links for each match.
        """
        for t1, t2 in combinations(self.tiles, 2):
            borders1 = set(t1.borders.values())
            borders2 = set(t2.borders.values())
            borders2.update({border[::-1] for border in borders2})
            link = borders1.intersection(borders2)
            if link:
                link = link.pop()
                dir1 = next(d for d, b in t1.borders.items() if b == link)
                t1.links[dir1] = t2
                dir2 = next(d for d, b in t2.borders.items() if b in {link, link[::-1]})
                t2.links[dir2] = t1

    def arrange_tiles(self):
        """The correct arrangement is obtained in three steps.
        1: Rotate a corner to have its links right and down.
        2: Fill the first column by matching tiles up to down.
        3: For each line-starting tile, fill the line left to right.
        """
        current_tile = next(tile for tile in self.tiles if len(tile.links) == 2)
        self.grid = [[current_tile]]
        while set(current_tile.links) != {1, 2}:
            current_tile.rotate()

        while 2 in current_tile.links:
            next_tile = current_tile.links[2]
            self.grid.append([next_tile])
            current_tile.align(next_tile, 2)
            current_tile = next_tile

        for line in self.grid:
            current_tile = line[0]
            while 1 in current_tile.links:
                next_tile = current_tile.links[1]
                line.append(next_tile)
                current_tile.align(next_tile, 1)
                current_tile = next_tile

    def get_image(self):
        """Construct the real image by joining tiles without borders."""
        image = []
        for tiles_line in self.grid:
            for k in range(1, tiles_line[0].size - 1):
                image.append("".join(tile.lines[k][1:-1] for tile in tiles_line))
        return image


def find_monsters(sea, monster=MONSTER):
    """Treat the sea image as a Tile and rotate/flip it until
    monsters are found. Detection is based on the hashes
    coordinates in the image.
    """
    sea = Tile(0, sea)
    monster_size = (len(monster), len(monster[0]))
    monster_hashes = set(
        (r, c)
        for r, c in product(range(monster_size[0]), range(monster_size[1]))
        if monster[r][c] == "#"
    )
    monsters_found = False
    test_count = 0
    while True:
        for row, col in product(
            range(0, len(sea.lines) - monster_size[0] + 1),
            range(0, len(sea.lines[0]) - monster_size[1] + 1),
        ):
            coords = set((row + x, col + y) for x, y in monster_hashes)
            if all(sea.lines[r][c] == "#" for r, c in coords):
                monsters_found = True
                for r, c in coords:
                    sea.lines[r] = f"{sea.lines[r][:c]}O{sea.lines[r][c+1:]}"
        if monsters_found:
            break
        test_count += 1
        if test_count != 4:
            sea.rotate()
        else:
            sea.flip()
    return sea.lines


class Today(Puzzle):
    def parser(self):
        self.tiles = "\n".join(self.input).strip().split("\n\n")
        for k, tile in enumerate(self.tiles):
            lines = tile.split("\n")
            self.tiles[k] = Tile(int(lines[0][5:-1]), lines[1:])

    def part_one(self):
        self.image = Image(self.tiles)
        self.image.find_links()
        return self.image.checksum

    def part_two(self):
        sea = find_monsters(self.image.get_image())
        # print("\n".join(sea).replace(".", " ").replace("#", "."))
        return Counter("".join(sea))["#"]


solutions = (54755174472007, 1692)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
