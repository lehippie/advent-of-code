"""Day 15: Rambunctious Recitation."""


# --- Part One ---

def part_one(starting_numbers: list, limit=2020):
    spoken = [None] * limit
    for i, n in enumerate(starting_numbers[:-1]):
        spoken[n] = i + 1
    last = starting_numbers[-1]
    for turn in range(len(starting_numbers), limit):
        if spoken[last] is None:
            spoken[last] = turn
            last = 0
        else:
            age = turn - spoken[last]
            spoken[last] = turn
            last = age
    return last


# --- Part Two ---

def part_two(starting_numbers):
    return part_one(starting_numbers, 30000000)


# --- Tests ---

def tests():
    # Part One
    assert part_one([0,3,6]) == 436
    assert part_one([1,3,2]) == 1
    assert part_one([2,1,3]) == 10
    assert part_one([1,2,3]) == 27
    assert part_one([2,3,1]) == 78
    assert part_one([3,2,1]) == 438
    assert part_one([3,1,2]) == 1836
    # Part Two
    assert part_two([0,3,6]) == 175594
    assert part_two([1,3,2]) == 2578
    assert part_two([2,1,3]) == 3544142
    assert part_two([1,2,3]) == 261214
    assert part_two([2,3,1]) == 6895259
    assert part_two([3,2,1]) == 18
    assert part_two([3,1,2]) == 362


if __name__ == "__main__":
    tests()

    puzzle_input = [6,19,0,5,7,13,1]

    result_one = part_one(puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 468

    result_two = part_two(puzzle_input)
    print(f"Part Two answer: {result_two}")
    assert result_two == 1801753
