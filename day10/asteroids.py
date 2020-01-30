"""Asteroids map library."""

import math
from collections import Counter

import numpy as np
import pandas as pd


class AsteroidsMap():
    """Asteroids map class."""

    def __init__(self, raw_map, empty_symb='.', aster_symb='#'):
        self.raw_map = self.decode_map(raw_map)
        self.sizeX = len(raw_map[0])
        self.sizeY = len(raw_map)
        self.positions = self.list_asteroids(aster_symb)
        self.detections = self.list_detections()
        self.counts = {p: len(d) for p, d in self.detections.items()}
        self.best = max(self.counts, key=lambda x: self.counts[x])

    def __str__(self):
        return '\n'.join(self.raw_map)

    def decode_map(self, raw_map):
        """Import map in form of list or file."""
        if isinstance(raw_map, str):
            with open(raw_map) as f:
                raw_map = [line.replace('\n', '') for line in f]
        return [m for m in raw_map if m]

    def list_asteroids(self, aster_symb):
        """Return positions of asteroids in map."""
        all_asteroids = []
        for y, row in enumerate(self.raw_map):
            posx = [i for i, x in enumerate(row) if x == aster_symb]
            all_asteroids.extend([(x, y) for x in posx])
        return all_asteroids

    def list_detections(self):
        """Return detected asteroids from each of them."""
        detections = {}
        for p in self.positions:
            others = self.positions.copy()
            others.remove(p)
            others = pd.DataFrame({
                'coord' : others,
                'rel' : [(x - p[0], y - p[1]) for x, y in others]})
            others['angle'] = [math.atan2(y, x) for x, y in others.rel]
            others['dist'] = [math.sqrt(x**2 + y**2) for x, y in others.rel]
            detections[p] = [others[others.angle == a]
                                   .sort_values(by='dist')
                                   .coord.iloc[0]
                             for a in set(others.angle)]
        return detections


if __name__ == "__main__":
    from asteroids_tests import tests
    tests()
