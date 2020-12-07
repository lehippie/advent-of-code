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
    """Return seat ID."""
    return int(
        boarding_pass.replace("B", "1")
                     .replace("F", "0")
                     .replace("R", "1")
                     .replace("L", "0"),
        base=2
    )


def part_one(passes):
    """Part One solution."""
    seats_ids = [decode_seat(p) for p in passes]
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
    assert decode_seat("FBFBBFFRLR") == 357
    assert decode_seat("BFFFBBFRRR") == 567
    assert decode_seat("FFFBBBFRRR") == 119
    assert decode_seat("BBFFBBFRLL") == 820


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    seats_ids = part_one(puzzle_input)
    part_two(seats_ids)
