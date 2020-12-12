"""Day 12: Rain Risk."""

from pathlib import Path


INPUT_FILE = "navigation_instructions.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.rstrip() for line in f]
    return data


# --- Part One ---

class ProbableBoat:
    turn_right = {
        "north": "east",
        "east": "south",
        "south": "west",
        "west": "north"
    }
    turn_left = {v: k for k, v in turn_right.items()}

    def __init__(self, instructions):
        self.instrutions = instructions.copy()
        self.position = [0, 0]
        self.direction = "east"

    @property
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


def part_one(puzzle_input):
    """Part One solution."""
    boat = ProbableBoat(puzzle_input)
    boat.navigate()
    print(f"We moved up to {boat.manhattan_distance}.")
    assert boat.manhattan_distance == 508


# --- Part Two ---

class RealBoat(ProbableBoat):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.waypoint = [10, 1]

    def move(self, value):
        self.position = [
            p + value*w
            for p, w in zip(self.position, self.waypoint)
        ]

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


def part_two(puzzle_input):
    """Part Two solution."""
    boat = RealBoat(puzzle_input)
    boat.navigate()
    print(f"We moved up to {boat.manhattan_distance} with real instructions.")
    assert boat.manhattan_distance == 30761


# --- Tests ---

def tests():
    # Part One
    test = ProbableBoat(load_input("test_input.txt"))
    test.navigate()
    assert test.manhattan_distance == 25
    # Part Two
    test = RealBoat(load_input("test_input.txt"))
    test.navigate()
    assert test.manhattan_distance == 286


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
