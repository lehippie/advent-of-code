"""--- Day 10: Monitoring Station ---"""

from cmath import phase, pi, polar
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        """Asteroids positions are kept as complex numbers with negative
        imaginary parts to keep correct orientations.
        """
        self.map = set()
        for r, row in enumerate(self.input):
            for c, state in enumerate(row):
                if state == "#":
                    self.map.add(c - r * 1j)

    def part_one(self):
        self.detections = {}
        for location in self.map:
            directions = set()
            for asteroid in self.map.difference([location]):
                angle = phase(asteroid - location)
                if angle not in directions:
                    directions.add(angle)
            self.detections[location] = len(directions)
        return max(self.detections.values())

    def part_two(self):
        """From the station, detected asteroids are sorted by their phase.
        As it is counterclockwise, we need a reverse sorting.
        Also, the laser starts its job at an angle of pi/2 so we substract
        2*pi to phases that are over it this.
        """
        self.station = max(self.detections, key=self.detections.get)
        detected = {}
        for asteroid in self.map.difference([self.station]):
            r, phi = polar(asteroid - self.station)
            if phi not in detected or r < detected[phi][1]:
                detected[phi] = [asteroid, r]
        detected = {
            a: phi if phi <= pi / 2 else phi - 2 * pi
            for phi, (a, _) in detected.items()
        }
        bet = sorted(detected, key=detected.get, reverse=True)[199]
        return int(100 * bet.real - bet.imag)


if __name__ == "__main__":
    Today().solve()
