"""Orbit map library."""


class Orbit():
    """Orbit Map class."""

    def __init__(self, raw_map):
        self.map = [m for m in raw_map if m]
        self.direct()
        self.indirect()
        self.calculate_checksum()

    def direct(self):
        """Read direct orbits from map."""
        self.orbits = {}
        for orbit in self.map:
            objects = orbit.split(')')
            self.orbits[objects[1]] = [objects[0], []]

    def indirect(self):
        """List indirect orbits of each object."""
        for obj in self.orbits:
            self.orbits[obj][1] = []
            direct = self.orbits[obj][0]
            while direct in self.orbits:
                direct = self.orbits[direct][0]
                self.orbits[obj][1].append(direct)

    def calculate_checksum(self):
        """Calculate checksum of an orbit map."""
        self.checksum = 0
        for p in self.orbits:
            self.checksum += 1 + len(self.orbits[p][1])

    def transfer(self, a, b):
        """Calculate the amount of transfers for a to join b."""
        path_a = [self.orbits[a][0]] + self.orbits[a][1]
        path_b = [self.orbits[b][0]] + self.orbits[b][1]
        root = next(o for o in path_a if o in path_b)
        return path_a.index(root) + path_b.index(root)


if __name__ == "__main__":
    from orbits_tests import tests
    tests()
