"""Day 19: Beacon Scanner."""

import numpy as np
from itertools import combinations
from aoc.puzzle import Puzzle


def generate_rotations_matrices():
    r = {
        "x": np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
        "y": np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),
        "z": np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
    }

    def rotations(mat, ax):
        """Generate the 4 rotations around ax."""
        for _ in range(4):
            yield mat
            mat = r[ax] @ mat

    eye = np.eye(3, dtype=int)
    out = list(rotations(eye, "x"))
    out.extend(rotations(r["y"] @ r["y"] @ eye, "x"))
    out.extend(rotations(r["z"] @ eye, "y"))
    out.extend(rotations(r["z"] @ r["z"] @ r["z"] @ eye, "y"))
    out.extend(rotations(r["y"] @ eye, "z"))
    out.extend(rotations(r["y"] @ r["y"] @ r["y"] @ eye, "z"))
    return out


def overlaps(trench, beacons, min_overlap=12):
    """Search for overlaps between beacons to add to the trench.
    Return the common offset if there is an overlap, None otherwise.
    """
    distances = trench[:, np.newaxis, :] - beacons
    uniques, count = np.unique(distances.reshape((-1, 3)), axis=0, return_counts=True)
    if max(count) >= min_overlap:
        return uniques[count.argmax()]


class Today(Puzzle):
    def parser(self):
        self.scanners = "\n".join(self.input).strip().split("\n\n")
        for k, scanner in enumerate(self.scanners):
            self.scanners[k] = np.array(
                [list(map(int, b.split(","))) for b in scanner.split("\n")[1:]]
            )

    def part_one(self):
        """We start with one scanner as the trench and the others in
        a queue. The latter are added one-by-one when enough common
        beacons are found. Otherwise, it goes back into the queue.
        """
        rotations = generate_rotations_matrices()
        self.trench = {"scanners": {(0, 0, 0)}, "beacons": self.scanners[0]}
        scanners_left = self.scanners[1:]
        while scanners_left:
            beacons = scanners_left.pop(0)
            found_overlap = False
            for rotation in rotations:
                oriented_beacons = beacons @ rotation
                offset = overlaps(self.trench["beacons"], oriented_beacons)
                if offset is not None:
                    found_overlap = True
                    oriented_beacons += offset
                    self.trench["scanners"].add(tuple(offset))
                    self.trench["beacons"] = np.unique(
                        np.vstack([self.trench["beacons"], oriented_beacons]),
                        axis=0,
                    )
                    break
            if not found_overlap:
                scanners_left.append(beacons)
        return len(self.trench["beacons"])

    def part_two(self):
        def manhattan(A, B):
            return sum(abs(a - b) for a, b in zip(A, B))

        return max(manhattan(a, b) for a, b in combinations(self.trench["scanners"], 2))


if __name__ == "__main__":
    Today().solve()
