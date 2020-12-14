"""Puzzle."""

from math import prod
from pathlib import Path


INPUT_FILE = "bus_timestamps.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.rstrip() for line in f]
    start = int(data[0])
    buses = [int(b) if b != "x" else None for b in data[1].split(",")]
    return start, buses


# --- Part One ---

def next_bus(start, buses):
    ts = {}
    for bus in buses:
        if bus is None:
            continue
        ts[bus] = next(
            t for t in range(start, start + bus + 1)
            if t % bus == 0
        )
    earliest = min(ts, key=ts.get)
    return earliest, ts[earliest] - start

def part_one(buses):
    """Part One solution."""
    bus_id, wait = next_bus(buses[0], buses[1])
    print(f"ID * waiting time = {bus_id * wait}")
    assert bus_id * wait == 3789


# --- Part Two ---

def shuttle_contest(buses):
    buses = [[b, k] for k, b in enumerate(buses) if b is not None]
    buses = sorted(buses, key=lambda x: x[0], reverse=True)
    cycle = buses[0][0]
    ts = buses[0][0] - buses[0][1]
    for k in range(2, len(buses) + 1):
        road = buses[:k]
        while not all((ts + k) % b == 0 for b, k in road):
            ts += cycle
        cycle = prod(b[0] for b in road)
    return ts

def part_two(buses):
    """Part Two solution."""
    ts = shuttle_contest(buses[1])
    print(f"Result to shuttle compagny contest: {ts}")
    assert ts == 667437230788118


# --- Tests ---

def tests():
    # Part One
    test_start, test_buses = load_input("test_input.txt")
    bus_id, wait = next_bus(test_start, test_buses)
    assert wait * bus_id == 295
    # Part Two
    ts = shuttle_contest(test_buses)
    assert ts == 1068781, ts
    ts = shuttle_contest([17,None,13,19])
    assert ts == 3417, ts
    ts = shuttle_contest([67,7,59,61])
    assert ts == 754018, ts
    ts = shuttle_contest([67,None,7,59,61])
    assert ts == 779210, ts
    ts = shuttle_contest([67,7,None,59,61])
    assert ts == 1261476, ts
    ts = shuttle_contest([1789,37,47,1889])
    assert ts == 1202161486, ts


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
