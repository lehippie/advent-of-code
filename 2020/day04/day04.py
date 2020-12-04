"""Day 4: Passport Processing."""

import re
from collections import Counter
from pathlib import Path


INPUT_FILE = "passports_batch.txt"
RULES = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": {"cm": (150, 193), "in": (59, 76)},
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": r"^[0-9]{9}$",
}


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    data = [{}]
    with filepath.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                data.append({})
                continue
            for field in line.split(" "):
                key, value = field.split(":")
                data[-1][key] = value
    return data


def check_fields(passport):
    """Verify that required fields are present."""
    return set(RULES).issubset(set(passport))


def check_height(height):
    """Verify correct height format."""
    unit = height[-2:]
    if unit in RULES["hgt"]:
        mini, maxi = RULES["hgt"][unit]
        return mini <= int(height[:-2]) <= maxi
    else:
        return False


def passport_validity(passport):
    """Apply more strict rules."""
    if (check_fields(passport)
        and RULES["byr"][0] <= int(passport["byr"]) <= RULES["byr"][1]
        and RULES["iyr"][0] <= int(passport["iyr"]) <= RULES["iyr"][1]
        and RULES["eyr"][0] <= int(passport["eyr"]) <= RULES["eyr"][1]
        and check_height(passport["hgt"])
        and re.match(RULES["hcl"], passport["hcl"])
        and passport["ecl"] in RULES["ecl"]
        and re.match(RULES["pid"], passport["pid"])
    ):
        return True
    return False


def tests():
    """Day tests."""
    test_passports = load_input("test_input.txt")
    assert len(test_passports) == 4
    test_validity = [check_fields(p) for p in test_passports]
    assert test_validity == [True, False, True, False]
    test_invalids = load_input("test_invalids.txt")
    assert any(passport_validity(p) for p in test_invalids) == False
    test_valids = load_input("test_valids.txt")
    assert all(passport_validity(p) for p in test_valids) == True


def part_one(passports_batch):
    """Part One solution."""
    counts = Counter(check_fields(p) for p in passports_batch)
    print(f"There are {counts[True]} passports with required fields.")
    assert counts[True] == 222


def part_two(passports_batch):
    """Part Two solution."""
    counts = Counter(passport_validity(p) for p in passports_batch)
    print(f"There are {counts[True]} valid passports.")
    assert counts[True] == 140


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
