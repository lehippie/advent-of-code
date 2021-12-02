"""Day 12: Rain Risk."""

from aoc.puzzle import Puzzle


class ProbableBoat:
    turn_right = {"north": "east", "east": "south", "south": "west", "west": "north"}
    turn_left = {v: k for k, v in turn_right.items()}

    def __init__(self, instructions):
        self.instrutions = instructions.copy()
        self.position = [0, 0]
        self.direction = "east"

    def manhattan_distance(self):
        return sum(abs(p) for p in self.position)

    def move(self, direction, value):
        if direction == "north":
            self.position[1] += value
        elif direction == "south":
            self.position[1] -= value
        elif direction == "east":
            self.position[0] += value
        elif direction == "west":
            self.position[0] -= value

    def turn(self, direction, value):
        for _ in range(value):
            if direction == "right":
                self.direction = self.turn_right[self.direction]
            elif direction == "left":
                self.direction = self.turn_left[self.direction]

    def navigate(self):
        for instruction in self.instrutions:
            action, value = instruction[0], int(instruction[1:])
            if action == "N":
                self.move("north", value)
            elif action == "S":
                self.move("south", value)
            elif action == "E":
                self.move("east", value)
            elif action == "W":
                self.move("west", value)
            elif action == "L":
                self.turn("left", value // 90)
            elif action == "R":
                self.turn("right", value // 90)
            elif action == "F":
                self.move(self.direction, value)


class RealBoat(ProbableBoat):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.waypoint = [10, 1]

    def move(self, value):
        self.position = [p + value * w for p, w in zip(self.position, self.waypoint)]

    def move_waypoint(self, direction, value):
        if direction == "north":
            self.waypoint[1] += value
        elif direction == "south":
            self.waypoint[1] -= value
        elif direction == "east":
            self.waypoint[0] += value
        elif direction == "west":
            self.waypoint[0] -= value

    def turn_waypoint(self, direction, value):
        for _ in range(value):
            if direction == "right":
                self.waypoint = [self.waypoint[1], -self.waypoint[0]]
            elif direction == "left":
                self.waypoint = [-self.waypoint[1], self.waypoint[0]]

    def navigate(self):
        for instruction in self.instrutions:
            action, value = instruction[0], int(instruction[1:])
            if action == "N":
                self.move_waypoint("north", value)
            elif action == "S":
                self.move_waypoint("south", value)
            elif action == "E":
                self.move_waypoint("east", value)
            elif action == "W":
                self.move_waypoint("west", value)
            elif action == "L":
                self.turn_waypoint("left", value // 90)
            elif action == "R":
                self.turn_waypoint("right", value // 90)
            elif action == "F":
                self.move(value)


class Puzzle12(Puzzle):
    def part_one(self):
        boat = ProbableBoat(self.input)
        boat.navigate()
        return boat.manhattan_distance()

    def part_two(self):
        boat = RealBoat(self.input)
        boat.navigate()
        return boat.manhattan_distance()


if __name__ == "__main__":
    Puzzle12(solutions=(508, 30761)).solve()
