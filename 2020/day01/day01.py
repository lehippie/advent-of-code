"""Day 1: Report Repair."""

from itertools import combinations
from pathlib import Path


def find_entries_by_sum(entries_file, how_many=2, aim=2020):
    """Find two values in <entries> that sum to <aim>."""
    filepath = Path(__file__).parent / entries_file
    with filepath.open() as f:
        entries = [int(line) for line in f]
    return next(c for c in combinations(entries, how_many)
                if sum(c) == aim)


def tests():
    a, b = find_entries_by_sum("test_input.txt")
    assert a * b == 514579
    a, b, c = find_entries_by_sum("test_input.txt", 3)
    assert a * b * c == 241861950


def part_one():
    a, b = find_entries_by_sum("expense_report.txt")
    result = a * b
    print(f"Multiplying the 2 entries that sum to 2020 gives {result}")
    assert result == 751776


def part_two():
    a, b, c = find_entries_by_sum("expense_report.txt", 3)
    result = a * b * c
    print(f"Multiplying the 3 entries that sum to 2020 gives {result}")
    assert result == 42275090


if __name__ == "__main__":
    tests()
    part_one()
    part_two()
