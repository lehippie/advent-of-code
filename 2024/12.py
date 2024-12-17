"""--- Day 12: Garden Groups ---"""

from aoc.puzzle import Puzzle

DIRECTIONS = (1, -1, 1j, -1j)
CORNERS_DIRECTIONS = ((1, 1j), (1j, -1), (-1, -1j), (-1j, 1))


def get_region(seed, plants):
    """DFS applied to the plants map."""
    plant = plants[seed]
    region = {seed}
    frontier = [seed]
    while frontier:
        position = frontier.pop()
        for d in DIRECTIONS:
            adj = position + d
            if adj in plants and adj not in region and plants[adj] == plant:
                region.add(adj)
                frontier.append(adj)
    return region


class Today(Puzzle):
    def parser(self):
        self.plants = {
            r + c * 1j: cell
            for r, row in enumerate(self.input)
            for c, cell in enumerate(row)
        }

    def part_one(self):
        """Find regions with DFS to calculate perimeters and areas."""
        price = 0
        self.regions = []
        remaining = set(self.plants)
        while remaining:
            seed = remaining.pop()
            region = get_region(seed, self.plants)
            self.regions.append(region)
            perimeter = sum(
                sum(p + d not in region for d in DIRECTIONS) for p in region
            )
            price += len(region) * perimeter
            remaining = remaining.difference(region)
        return price

    def part_two(self):
        """The amount of sides is equal to the amount of corners."""
        price = 0
        for region in self.regions:
            corners = 0
            for p in region:
                for d1, d2 in CORNERS_DIRECTIONS:
                    if p + d1 not in region and p + d2 not in region:
                        corners += 1
                    if (
                        p + d1 in region
                        and p + d2 in region
                        and p + d1 + d2 not in region
                    ):
                        corners += 1
            price += len(region) * corners
        return price


if __name__ == "__main__":
    Today().solve()
