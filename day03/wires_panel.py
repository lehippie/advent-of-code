"""Wires panel library."""


class Wire():
    """Wire class."""

    def __init__(self, raw_path):
        """Decode string path."""
        self.raw_path = raw_path.split(',')
        self.path = [(0,0)]
        steps_gen = ((p[0], int(p[1:])) for p in self.raw_path)
        for d, n in steps_gen:
            for _ in range(n):
                if d == 'U':
                    step = (self.path[-1][0], self.path[-1][1] + 1)
                if d == 'D':
                    step = ((self.path[-1][0], self.path[-1][1] - 1))
                if d == 'L':
                    step = ((self.path[-1][0] - 1, self.path[-1][1]))
                if d == 'R':
                    step = ((self.path[-1][0] + 1, self.path[-1][1]))
                self.path.append(step)

    def crosses(self, other_wire):
        """Return intersections of two Wires without central port."""
        intersections = list(set(self.path) & set(other_wire.path))
        intersections = sorted(intersections, key=lambda x: [x[0], x[1]])
        return [M for M in intersections if M != (0,0)]

    def closest_cross(self, wire2):
        """Distance to closest intersection point."""
        distances = [abs(c[0]) + abs(c[1]) for c in self.crosses(wire2)]
        return min(distances)

    def delay(self, M):
        """Delay to reach point M."""
        return self.path.index(M)

    def shortest_cross(self, wire2):
        """Timing to closest intersection point."""
        timings = [self.delay(c) + wire2.delay(c) for c in self.crosses(wire2)]
        return min(timings)


if __name__ == "__main__":
    from wires_panel_tests import tests
    tests()
