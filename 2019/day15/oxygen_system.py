"""Oxygen system library."""

import matplotlib.pyplot as plt


DIRECTIONS = {
    "north": 1,
    "south": 2,
    "west": 3,
    "east": 4,
}
DROID_GO_RIGHT = {
    "north": "east",
    "east": "south",
    "south": "west",
    "west": "north",
}
DROID_GO_LEFT = {v: k for k, v in DROID_GO_RIGHT.items()}


class RepairDroid:
    """Repair droid class."""

    def __init__(self, program=None):
        self.program = program
        self.position = (0, 0)
        self.direction = "north"
        self.area = {self.position: 1}
        self.path = []

    def get_destination(self):
        if self.direction == "north":
            return self.position[0], self.position[1] + 1
        if self.direction == "south":
            return self.position[0], self.position[1] - 1
        if self.direction == "west":
            return self.position[0] - 1, self.position[1]
        if self.direction == "east":
            return self.position[0] + 1, self.position[1]

    def turn_right(self):
        self.direction = DROID_GO_RIGHT[self.direction]

    def turn_left(self):
        self.direction = DROID_GO_LEFT[self.direction]

    def move(self):
        destination = self.get_destination()
        status = self.program.run(DIRECTIONS[self.direction])
        self.area[destination] = status
        if status == 0:
            self.turn_left()
        else:
            self.position = destination
            self.turn_right()

    @property
    def oxygen_system(self):
        try:
            pos = next(k for k, v in self.area.items() if v == 2)
        except StopIteration:
            pos = None
        return pos

    @property
    def xlim(self):
        return [min(p[0] for p in self.area), max(p[0] for p in self.area)]

    @property
    def ylim(self):
        return [min(p[1] for p in self.area), max(p[1] for p in self.area)]

    def explore(self):
        """Explore the area with wall-following algorithm."""
        # Start by leaving initial position
        while self.position == (0, 0):
            self.move()
        # End when back to initial position
        while self.position != (0, 0):
            self.move()
        # Fill unexplored values with walls
        self.area = {
            (x, y): self.area.get((x, y), 0)
            for x in range(self.xlim[0], self.xlim[1] + 1)
            for y in range(self.ylim[0], self.ylim[1] + 1)
        }
        if ox_sys := self.oxygen_system:
            print(f"Finished exploring. Oxygen system found at {ox_sys} :]")
        else:
            print("Finished exploring. Oxygen system not found :[")

    def show_area(self):
        _, ax = plt.subplots()
        for p, v in self.area.items():
            if p == (0, 0):
                ax.annotate("D", xy=p)
            elif v == 0:
                ax.annotate("#", xy=p)
            elif v == 2:
                ax.annotate("X", xy=p)
        for p in self.path:
            ax.annotate(".", xy=p, c="C1")
        ax.set_xlim(self.xlim)
        ax.set_ylim(self.ylim)
        ax.axis("off")
        plt.show()

    def find_path(self):
        """Calculate shortest route to Oxygen System."""
        self.path = [self.position]
        while self.position != self.oxygen_system:
            self.move()
            if self.position == self.path[-1]:
                continue
            elif self.position in self.path:
                del self.path[-1]
            else:
                self.path.append(self.position)


def oxygen_propagation(area):
    """Model of oxygen propagation."""
    free_space = {p for p, v in area.items() if v in [1, 2]}
    origin = next(p for p, v in area.items() if v == 2)
    oxy_space = {origin}
    time = 0
    while oxy_space != free_space:
        time += 1
        for x, y in oxy_space.copy():
            near = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            oxy_space = oxy_space.union({p for p in near if area[p] != 0})
    return time


def tests():
    d = RepairDroid()
    assert d.direction == "north"
    d.turn_right()
    assert d.direction == "east"
    d.turn_right()
    assert d.direction == "south"
    d.turn_right()
    assert d.direction == "west"
    d.turn_right()
    assert d.direction == "north"
    d.turn_left()
    assert d.direction == "west"
    d.turn_left()
    assert d.direction == "south"
    d.turn_left()
    assert d.direction == "east"
    d.turn_left()
    assert d.direction == "north"
    assert d.position == (0, 0)
    assert d.get_destination() == (0, 1)
    d.turn_left()
    d.turn_left()
    assert d.get_destination() == (0, -1)
    d.turn_right()
    assert d.get_destination() == (-1, 0)
    d.turn_right()
    d.turn_right()
    assert d.get_destination() == (1, 0)

    walls = [(1,0), (2,0), (3,0), (0,1), (4,1), (0,2), (2,2), (5,2),
             (0,3), (3,3), (4,3), (1,4), (2,4)]
    spaces = [(1,1), (3,1), (1,2), (3,2), (4,2), (1,3), (2,3)]
    oxygen = (2,1)
    area = {p: 0 for p in walls}
    area.update({p: 1 for p in spaces})
    area[oxygen] = 2
    time_to_ox = oxygen_propagation(area)
    assert time_to_ox == 4, time_to_ox


if __name__ == "__main__":
    tests()
