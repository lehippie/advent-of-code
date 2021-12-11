"""Day 7: Some Assembly Required."""

from aoc.puzzle import Puzzle


class Circuit:
    def __init__(self, connections: dict):
        self.connections = connections
        self._wires = {}
        self._mask = 0xFFFF

    def __getitem__(self, wire):
        if wire.isdigit():
            return int(wire)
        if wire not in self._wires:
            try:
                result = int(self.connections[wire])
            except ValueError:
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
            self._wires[wire] = result & self._mask
        return self._wires[wire]

    def __setitem__(self, key, value):
        self._wires[key] = value


class Puzzle07(Puzzle):
    def parser(self):
        connections = {}
        for line in self.input:
            value, wire = line.split(" -> ")
            connections[wire] = value
        return connections

    def part_one(self):
        self.signal = Circuit(self.input)["a"]
        return self.signal

    def part_two(self):
        circuit = Circuit(self.input)
        circuit["b"] = self.signal
        return circuit["a"]


if __name__ == "__main__":
    Puzzle07(solutions=(3176, 14710)).solve()
