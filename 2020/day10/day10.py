"""Day 10: Adapter Array."""

from collections import Counter
from pathlib import Path


INPUT_FILE = "adapters_joltages.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        data = list(map(int, f))
    return data


# --- Part One ---

def joltage_differences(joltages):
    j = sorted(joltages + [0, max(joltages) + 3])
    return Counter(a - b for a, b in zip(j[1:], j[:-1]))


def part_one(adapters_joltages):
    """Part One solution."""
    differences = joltage_differences(adapters_joltages)
    result = differences[1] * differences[3]
    print(f"1-jolt by 3-jolt differences gives {result}.")
    assert result == 2201


# --- Part Two ---
def count_arrangements(joltages):
    end_jolt = max(joltages) + 3
    jolts = set(joltages + [0, end_jolt])
    tree = Counter({0: 1})
    count = 0
    while tree:
        new_tree = Counter()
        for n, q in tree.items():
            new_tree.update({j: q for j in jolts.intersection(range(n+1, n+4))})
        count += new_tree.pop(end_jolt, 0)
        tree = new_tree
    return count


def part_two(adapters_joltages):
    """Part Two solution."""
    arrangements_count = count_arrangements(adapters_joltages)
    print(f"There are {arrangements_count} possible arrangements.")
    assert arrangements_count == 169255295254528


# --- Tests ---

def tests():
    # Part One
    test01 = load_input("test_input_01.txt")
    assert joltage_differences(test01) == {1: 7, 3: 5}
    test02 = load_input("test_input_02.txt")
    assert joltage_differences(test02) == {1: 22, 3: 10}
    # Part Two
    assert count_arrangements(test01) == 8
    assert count_arrangements(test02) == 19208


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
