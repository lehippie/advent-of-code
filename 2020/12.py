"""Day 12: Rain Risk."""

from aoc.puzzle import Puzzle


TURN_RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
TURN_LEFT = {v: k for k, v in TURN_RIGHT.items()}


class ProbableShip:
    def __init__(self, instructions):
        self.instrutions = instructions
        self.position = [0, 0]
        self.direction = "E"

    def move(self, direction, value):
        if direction == "N":
            self.position[1] += value
        elif direction == "S":
            self.position[1] -= value
        elif direction == "E":
            self.position[0] += value
        elif direction == "W":
            self.position[0] -= value

    def turn(self, direction, value):
        for _ in range(value // 90):
            if direction == "R":
                self.direction = TURN_RIGHT[self.direction]
            elif direction == "L":
                self.direction = TURN_LEFT[self.direction]

    def forward(self, value):
        self.move(self.direction, value)

    def navigate(self):
        for instruction in self.instrutions:
            action, value = instruction[0], int(instruction[1:])
            if action in TURN_RIGHT:
                self.move(action, value)
            elif action in {"L", "R"}:
                self.turn(action, value)
            elif action == "F":
                self.forward(value)
        return self.manhattan_distance()

    def manhattan_distance(self):
        return sum(abs(p) for p in self.position)


class ActualShip(ProbableShip):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.waypoint = [10, 1]

    def move(self, direction, value):
        """Move method now act on the waypoint."""
        if direction == "N":
            self.waypoint[1] += value
        elif direction == "S":
            self.waypoint[1] -= value
        elif direction == "E":
            self.waypoint[0] += value
        elif direction == "W":
            self.waypoint[0] -= value

    def turn(self, direction, value):
        """Turn method now rotate the waypoint around the ship."""
        for _ in range(value // 90):
            if direction == "R":
                self.waypoint = [self.waypoint[1], -self.waypoint[0]]
            elif direction == "L":
                self.waypoint = [-self.waypoint[1], self.waypoint[0]]

    def forward(self, value):
        """Forward method moves the ship in the direction of the waypoint."""
        self.position = [p + value * w for p, w in zip(self.position, self.waypoint)]


class Today(Puzzle):
    def part_one(self):
        return ProbableShip(self.input).navigate()

    def part_two(self):
        return ActualShip(self.input).navigate()


solutions = (508, 30761)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
