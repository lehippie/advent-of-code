"""--- Day 18: Lavaduct Lagoon ---"""

from math import ceil
from aoc.puzzle import Puzzle

MOVE = {"U": -1j, "D": 1j, "L": -1, "R": 1}


class Today(Puzzle):
    def parser(self):
        self.plan = []
        for line in self.input:
            direction, n, color = line.split()
            self.plan.append((direction, int(n), color[2:-1]))

    def part_one(self):
        """After forming the trench, we use a flood-fill method in
        a square surrounding the trench to find the exterior. The
        result is the surface of the square minus the exterior.
        """
        # Form the trench
        position = 0
        trench = set([position])
        for direction, n, _ in self.plan:
            trench.update(position + i * MOVE[direction] for i in range(1, n + 1))
            position = position + n * MOVE[direction]

        # Find surrounding square
        rm = min(p.real for p in trench) - 1
        rM = max(p.real for p in trench) + 2
        im = min(p.imag for p in trench) - 1
        iM = max(p.imag for p in trench) + 2

        # Flood-fill the exterior
        frontier = [rm + im * 1j]
        exterior = set(frontier)
        while frontier:
            position = frontier.pop()
            for direction in MOVE.values():
                p = position + direction
                if (
                    p not in exterior
                    and p not in trench
                    and rm <= p.real < rM
                    and im <= p.imag < iM
                ):
                    frontier.append(p)
                    exterior.add(p)
        return int((rM - rm) * (iM - im) - len(exterior))

    def part_two(self):
        """Green's theorem for polygons (aka shoelace formula).
        Adjustments must be taken into account because this theorem
        works on points, not on a path made of m²: the perimeter
        needs an added 1/2 per m², outer corners are balanced by inner
        ones except for 4 of them. Thus the area is initialized to 1.
        """
        digit2direction = {"0": "R", "1": "D", "2": "L", "3": "U"}
        trench = [0]
        area = 1
        length = 0
        for _, _, color in self.plan:
            direction = digit2direction[color[-1]]
            n = int(f"0x{color[:5]}", base=16)
            trench.append(trench[-1] + n * MOVE[direction])
            p1, p2 = trench[-2], trench[-1]
            area += (p1.real * p2.imag - p1.imag * p2.real) / 2
            length += n
        area = area + length // 2
        return int(area)


solutions = (26857, 129373230496292)

if __name__ == "__main__":
    Today(infile="test.txt", solutions=(62, 952408144115)).solve()
    Today(solutions=solutions).solve()
