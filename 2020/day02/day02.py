"""Day 2: Password Philosophy."""

from collections import Counter
from pathlib import Path


def is_valid(password_line, policy):
    """Check if a password is valid according to its policy."""
    values, letter, password = password_line.split(" ")
    v1, v2 = [int(v) for v in values.split("-")]
    letter = letter[0]
    if policy == "sled":
        count = Counter(password)
        return v1 <= count[letter] <= v2
    if policy == "toboggan":
        return (password[v1-1] == letter) != (password[v2-1] == letter)


def count_valid_passwords(passwords_file, policy="sled"):
    """Count valid password in given file.

    <policy> can be "sled" or "toboggan".
    """
    filepath = Path(__file__).parent / passwords_file
    with filepath.open() as f:
        validity = [is_valid(line, policy) for line in f]
    count = Counter(validity)
    return count[True]


def tests():
    assert count_valid_passwords("test_input.txt") == 2
    assert count_valid_passwords("test_input.txt", "toboggan") == 1


def part_one():
    valid_count = count_valid_passwords("passwords_list.txt")
    print(f"There are {valid_count} valid passwords (Sled policy).")
    assert valid_count == 628


def part_two():
    valid_count = count_valid_passwords("passwords_list.txt", "toboggan")
    print(f"There are {valid_count} valid passwords (Toboggan policy).")
    assert valid_count == 705


if __name__ == "__main__":
    tests()
    part_one()
    part_two()
