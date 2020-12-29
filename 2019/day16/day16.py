"""Day 16: Flawed Frequency Transmission."""

from itertools import chain, repeat
from pathlib import Path


# --- Parsing input ---

def parse_input(filename):
    filepath = Path(__file__).parent / filename
    with open(filepath) as f:
        data = f.readline().strip()
    return data


# --- Part One ---

def gen_plus(k, limit):
    start = k
    stop = 2*k + 1
    offset = 4*k +4
    for rep in range(limit):
        for idx in range(start + rep*offset, stop + rep*offset):
            if idx >= limit:
                return
            yield idx

def gen_minus(k, limit):
    start = 3*k + 2
    stop = 4*k + 3
    offset = 4*k +4
    for rep in range(limit):
        for idx in range(start + rep*offset, stop + rep*offset):
            if idx >= limit:
                return
            yield idx

def fft(signal):
    for k in range(len(signal)):
        signal[k] = abs(
            sum(signal[l] for l in gen_plus(k, len(signal)))
            - sum(signal[l] for l in gen_minus(k, len(signal)))
        ) % 10
    return signal

def part_one(signal, phases=100):
    signal = list(map(int, signal))
    for _ in range(phases):
        signal = fft(signal)
    return "".join(map(str, signal[:8]))


# --- Part Two ---

def part_two(signal):
    offset = int(signal[:7])
    signal = "".join(chain.from_iterable(repeat(signal, 10000)))
    output = part_one(signal)
    return "".join(map(str, output[offset:offset+8]))


# --- Tests & Run ---

def tests():
    assert part_one("12345678", 4) == "01029498"
    assert part_one("80871224585914546619083218645595") == "24176176"
    assert part_one("19617804207202209144916044189917") == "73745418"
    assert part_one("69317163492948606335995924319873") == "52432133"
    assert part_two("03036732577212944063491565474664") == "84462026"
    print("ok", 1)
    assert part_two("02935109699940807407585447034323") == "78725270"
    print("ok", 2)
    assert part_two("03081770884921959731165446850517") == "53553731"
    print("ok", 3)


if __name__ == "__main__":
    tests()

    puzzle_input = parse_input("signal.txt")

    result_one = part_one(puzzle_input)
    print("Part One answer:", result_one)
    assert result_one == "63794407"

    result_two = part_two(puzzle_input)
    print("Part Two answer:", result_two)
    assert result_two
