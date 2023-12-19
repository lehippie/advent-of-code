"""--- Day 18: Lavaduct Lagoon ---"""

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
        """Green's theorem for polygons (aka shoelace formula). It
        calculates the area of any polygon by the sum of the oriented
        areas of each triangle made by the origin and each couple of
        vertices.

        Adjustments must be made because this calculate the area while
        passing through points and not a grid: edges miss 1/2, inner
        corners 1/4 and outer corners 3/4. They are almost the same
        amount of inner and outer corners so counting 1/2 for each
        balances them. The exception is for 4 of outer corners (like
        in a simple square), for which we need to add 1.
        """
        digit2direction = {"0": "R", "1": "D", "2": "L", "3": "U"}
        length, area, p0 = 0, 0, 0
        for _, _, color in self.plan:
            direction = digit2direction[color[-1]]
            n = int(f"0x{color[:5]}", base=16)
            length += n
            p1 = p0 + n * MOVE[direction]
            area += p0.real * p1.imag - p0.imag * p1.real
            p0 = p1
        return int(area / 2 + length / 2 + 1)


solutions = (26857, 129373230496292)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
