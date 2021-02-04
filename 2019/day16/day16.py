"""Day 16: Flawed Frequency Transmission."""

from pathlib import Path


# --- Parsing input ---

def parse_input(filename):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        data = f.readline().strip()
    return data


# --- Part One ---

def gen_plus(k, limit):
    start = k - 1
    stop = 2*k
    step = 4*k + 4
    while start < limit - 1:
        yield (start, min(stop, limit - 1))
        start = start + step
        stop = stop + step


def gen_minus(k, limit):
    start = 3*k + 1
    stop = 4*k + 2
    step = 4*k + 4
    while start < limit - 1:
        yield (start, min(stop, limit - 1))
        start = start + step
        stop = stop + step


def fft(signal, skip=0):
    csum = signal + [0]
    for k in range(1, len(signal)):
        csum[k] = csum[k] + csum[k-1]
    for k in range(skip, len(signal)):
        signal[k] = abs(
            sum(csum[b] - csum[a] for a, b in gen_plus(k, len(signal)))
            - sum(csum[b] - csum[a] for a, b in gen_minus(k, len(signal)))
        ) % 10
    return signal


def part_one(signal, phases=100, skip=0):
    signal = list(map(int, signal))
    for _ in range(phases):
        signal = fft(signal, skip)
    return "".join(map(str, signal[skip:skip+8]))


# --- Part Two ---

def part_two(signal):
    offset = int(signal[:7])
    real_signal = signal * 10000
    return part_one(real_signal, skip=offset)


# --- Tests & Run ---

def tests():
    assert part_one("12345678", 4) == "01029498"
    assert part_one("80871224585914546619083218645595") == "24176176"
    assert part_one("19617804207202209144916044189917") == "73745418"
    assert part_one("69317163492948606335995924319873") == "52432133"
    assert part_two("03036732577212944063491565474664") == "84462026"
    assert part_two("02935109699940807407585447034323") == "78725270"
    assert part_two("03081770884921959731165446850517") == "53553731"


if __name__ == "__main__":
    tests()

    puzzle_input = parse_input("signal.txt")

    result_one = part_one(puzzle_input)
    print("Part One answer:", result_one)
    assert result_one == "63794407"

    result_two = part_two(puzzle_input)
    print("Part Two answer:", result_two)
    assert result_two == "77247538"
