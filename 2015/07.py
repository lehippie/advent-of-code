"""Day 7: Some Assembly Required."""

from aoc.puzzle import Puzzle


class Circuit:
    def __init__(self, connections: dict):
        self.connections = connections
        self.wires_values = {}
        self._mask = 0xFFFF

    def __getitem__(self, wire):
        """Recursively look back throuht connections from
        needed wire to numerical values.

        Calculated values are cached for next lookups.
        """
        if wire not in self.wires_values:
            if wire.isdigit():
                result = int(wire)
            else:
                operation = self.connections[wire].split()
                if "AND" in operation:
                    result = self[operation[0]] & self[operation[2]]
                elif "OR" in operation:
                    result = self[operation[0]] | self[operation[2]]
                elif "NOT" in operation:
                    result = ~self[operation[1]]
                elif "LSHIFT" in operation:
                    result = self[operation[0]] << int(operation[2])
                elif "RSHIFT" in operation:
                    result = self[operation[0]] >> int(operation[2])
                else:
                    result = self[operation[0]]
            self.wires_values[wire] = result & self._mask
        return self.wires_values[wire]

    def __setitem__(self, key, value):
        self.wires_values[key] = value


class Today(Puzzle):
    def parser(self):
        self.connections = {}
        for line in self.input:
            value, wire = line.split(" -> ")
            self.connections[wire] = value

    def part_one(self):
        self.signal = Circuit(self.connections)["a"]
        return self.signal

    def part_two(self):
        circuit = Circuit(self.connections)
        circuit["b"] = self.signal
        return circuit["a"]


if __name__ == "__main__":
    Today().solve()
