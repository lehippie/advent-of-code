"""Day 23: Crab Cups."""


# --- Part One ---

def part_one(cups, moves=100):
    for _ in range(moves):
        try:
            dest = cups.index(next(cup for cup in range(cups[0]-1, 0, -1)
                                       if cup not in cups[1:4]))
        except StopIteration:
            dest = cups.index(max(cups[4:]))
        cups = cups[4:dest+1] + cups[1:4] + cups[dest+1:] + [cups[0]]
    one = cups.index(1)
    return "".join(str(c) for c in cups[one+1:] + cups[:one])


# --- Part Two ---

def part_two(cups, moves=10000000, maxi=1000000):
    init = cups + list(range(max(cups)+1, maxi+1))
    cups = [None for _ in range(maxi + 1)]
    for c, n in zip(init, init[1:] + [init[0]]):
        cups[c] = n
        
    cur = init[0]
    for _ in range(moves):
        picked = (cups[cur], cups[cups[cur]], cups[cups[cups[cur]]])
        try:
            dest = next(cup for cup in range(cur-1, 0, -1)
                            if cup not in picked)
        except StopIteration:
            dest = next(cup for cup in range(maxi, 0, -1)
                            if cup not in picked)
        cups[cur] = cups[picked[-1]]
        cups[picked[-1]] = cups[dest]
        cups[dest] = picked[0]
        cur = cups[cur]
    return cups[1] * cups[cups[1]]


# --- Tests & Run ---

def tests():
    test = list(map(int, "389125467"))
    assert part_one(test, 10) == "92658374"
    assert part_one(test) == "67384529"
    assert part_two(test) == 149245887792


if __name__ == "__main__":
    tests()

    puzzle_input = list(map(int, "583976241"))

    result_one = part_one(puzzle_input)
    print("Part One answer:", result_one)
    assert result_one == "24987653"

    result_two = part_two(puzzle_input)
    print("Part Two answer:", result_two)
    assert result_two == 442938711161
