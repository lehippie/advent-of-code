"""Moons Motion library."""

from itertools import combinations
from numpy import lcm

class Moon():
    """Moon class."""

    def __init__(self, pos=[0, 0, 0], vel=[0, 0, 0], name=None):
        if len(pos) != 3 or len(vel) != 3:
            raise IOError("Position and velocity lengths must be exactly 3.")
        self.pos = list(pos)
        self.vel = list(vel)
        self.name = name

    def move(self):
        for k in range(3):
            self.pos[k] += self.vel[k]

    def energy(self):
        self.pot = sum(abs(p) for p in self.pos)
        self.kin = sum(abs(v) for v in self.vel)
        return self.pot * self.kin


class MotionSimulator():
    """Simulator of moons motions."""

    def __init__(self, moons=[Moon()]):
        self.moons = moons
        self.steps = 0

    def __str__(self):
        p = [2] * 6
        for k in range(3):
            p[k] = max(
                p[k],
                max([len(str(m.pos[k])) for m in self.moons])
            )
            p[k+3] = max(
                p[k+3],
                max([len(str(m.vel[k])) for m in self.moons])
            )
        out = f"After {self.steps} steps:\n"
        m = [
            (f"pos=<x={m.pos[0]:>{p[0]}}, "
                  f"y={m.pos[1]:>{p[1]}}, "
                  f"z={m.pos[2]:>{p[2]}}>, "
             f"vel=<x={m.vel[0]:>{p[3]}}, "
                  f"y={m.vel[1]:>{p[4]}}, "
                  f"z={m.vel[2]:>{p[5]}}>")
            for m in self.moons
        ]
        out = out + '\n'.join(m)
        return out

    def names(self):
        return [m.name for m in self.moons]

    def apply_gravity(self):
        for m1, m2 in combinations(self.moons, 2):
            for k in range(3):
                if m1.pos[k] < m2.pos[k]:
                    m1.vel[k] += 1
                    m2.vel[k] += -1
                elif m1.pos[k] > m2.pos[k]:
                    m1.vel[k] += -1
                    m2.vel[k] += 1

    def apply_velocity(self):
        for m in self.moons:
            m.move()

    def energy(self):
        return sum(m.energy() for m in self.moons)

    def next_step(self, n=1):
        for _ in range(n):
            self.apply_gravity()
            self.apply_velocity()
        self.steps += n

    def state(self, ax):
        return ''.join(
            ''.join(map(str, [m.pos[ax], m.vel[ax]]))
            for m in self.moons
        )

    def find_cycle(self):
        cycles = [None, None, None]
        self.steps = 0
        memory = [self.state(0), self.state(1), self.state(2)]
        while not all(cycles):
            self.next_step()
            for k in range(3):
                state = self.state(k)
                if not cycles[k] and state == memory[k]:
                    cycles[k] = self.steps
        return lcm.reduce(cycles)


if __name__ == '__main__':
    from moons_motion_tests import tests
    tests()
