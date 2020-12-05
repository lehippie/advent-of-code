"""Day 5: Binary Boarding."""

from pathlib import Path


INPUT_FILE = "nearby_boarding_passes.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = [line.strip() for line in f]
    return data


def decode_seat(boarding_pass):
    """Return row, column and ID of a seat."""
    row = boarding_pass[:7].replace("B", "1").replace("F", "0")
    row = int(row, base=2)
    col = boarding_pass[-3:].replace("R", "1").replace("L", "0")
    col = int(col, base=2)
    return (row, col, row * 8 + col)


def part_one(passes):
    """Part One solution."""
    seats_ids = [decode_seat(p)[2] for p in passes]
    max_sid = max(seats_ids)
    print(f"{max_sid} is the maximum seat ID nearby.")
    assert max_sid == 928
    return seats_ids


def part_two(seats_ids):
    """Part Two solution."""
    my_sid = next(s for s in range(min(seats_ids) + 1, max(seats_ids))
                    if s not in seats_ids)
    print(f"My seat's ID is {my_sid}.")
    assert my_sid == 610


def tests():
    """Day tests."""
    assert decode_seat("FBFBBFFRLR") == (44, 5, 357)
    assert decode_seat("BFFFBBFRRR") == (70, 7, 567)
    assert decode_seat("FFFBBBFRRR") == (14, 7, 119)
    assert decode_seat("BBFFBBFRLL") == (102, 4, 820)


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    seats_ids = part_one(puzzle_input)
    part_two(seats_ids)
