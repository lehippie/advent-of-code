"""Day 25: Combo Breaker."""


# --- Part One ---

def transform(subject_number, loop):
    value = 1
    for _ in range(loop):
        value = (value * subject_number) % 20201227
    return value


def part_one(public_keys):
    value = 1
    loop = 0
    while value not in public_keys:
        value = (value * 7) % 20201227
        loop += 1
    return transform(
        public_keys[(public_keys.index(value) + 1) % 2],
        loop
    )


# --- Tests & Run ---

def tests():
    test = (5764801, 17807724)
    assert part_one(test) == 14897079


if __name__ == "__main__":
    tests()

    puzzle_input = (13233401, 6552760)

    result_one = part_one(puzzle_input)
    print("Part One answer:", result_one)
    assert result_one == 17673381
