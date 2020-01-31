"""Asteroids map library."""

import math


class AsteroidsMap():
    """Asteroids map class."""

    def __init__(self, raw_map, empty_symb='.', ast_symb='#'):
        self.raw_map = self.decode_map(raw_map)
        self.positions = self.list_asteroids(ast_symb)
        self.detection_counts = self.count_detections()
        self.station, self.station_count = self.max_detection_position()
        self.vaporization_order = self._vaporder()

    def __str__(self):
        return '\n'.join(self.raw_map)

    def decode_map(self, raw_map):
        """Import map in form of list or file."""
        if isinstance(raw_map, str):
            with open(raw_map) as f:
                raw_map = [line.replace('\n', '') for line in f]
        return [m for m in raw_map if m]

    def list_asteroids(self, ast_symb):
        """Return positions of asteroids in map."""
        all_asteroids = []
        for y, row in enumerate(self.raw_map):
            posx = [i for i, x in enumerate(row) if x == ast_symb]
            all_asteroids.extend([(x, y) for x in posx])
        return all_asteroids

    def count_detected_from(self, ast):
        """Return count of detected asteroids from <ast>."""
        x0, y0 = ast
        axes = set()
        for x, y in self.positions:
            if x != x0 or y != y0:
                a = math.atan2(y - y0, x - x0)
                axes.add(a)
        return len(axes)

    def count_detections(self):
        """Return count of detected asteroids from each one in the map."""
        return [self.count_detected_from(a) for a in self.positions]

    def max_detection_position(self):
        """Return position with maximum asteroids detection count."""
        maxcount = max(self.detection_counts)
        where = self.positions[self.detection_counts.index(maxcount)]
        return where, maxcount

    def detected_from(self, ast, group=None):
        """Return positions, angles and distances of asteroids
        detected from <ast>.

        Angles calculated from minus y-axis and in [0 ; 2*pi[.
        <group> can be set to be a list of specific asteroids among
        the map.
        """
        if group is None:
            group = self.positions
        x0, y0 = ast
        detections = {}
        for x, y in group:
            if x != x0 or y != y0:
                a = math.atan2(-(x - x0), y - y0) + math.pi
                if a == 2 * math.pi:
                    a = 0
                d = math.sqrt((x - x0)**2 + (y - y0)**2)
                if a in detections and d > detections[a][1]:
                    continue
                detections[a] = ((x, y), d)
        detections = [(X[0], a, X[1]) for a, X in detections.items()]
        return detections

    def _vaporder(self):
        """Return vaporization order."""
        remaining = self.positions.copy()
        remaining.remove(self.station)
        vapor = []
        while remaining:
            detections = self.detected_from(self.station, group=remaining)
            detections.sort(key=lambda d: d[1])
            for d in detections:
                vapor.append(d[0])
                remaining.remove(d[0])
        return vapor

    def vaporized(self, n):
        """Return the position of the <n>th vaporized asteroid."""
        return self.vaporization_order[n-1]


if __name__ == "__main__":
    from asteroids_tests import tests
    tests()
