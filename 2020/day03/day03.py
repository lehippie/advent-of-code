"""Day 3: Toboggan Trajectory."""

from collections import Counter
from math import prod
from pathlib import Path


INPUT = "tree_map.txt"
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    with filepath.open() as f:
        return [line.strip() for line in f]


def count_trees(tree_map, right, down):
    """Count trees along the <right>, <down> slope."""
    return Counter(
        tree_map[y][(k * right) % len(tree_map[0])]
        for k, y in enumerate(range(0, len(tree_map), down))
    )["#"]


def tests():
    """Day tests."""
    test_map = load_input("test_input.txt")
    counts = [count_trees(test_map, *s) for s in SLOPES]
    assert counts == [2, 7, 3, 4, 2]
    assert prod(counts) == 336


def part_one(tree_map):
    """Part One solution."""
    count = count_trees(tree_map, 3, 1)
    print(f"{count} trees are encountered following slope (3, 1).")
    assert count == 276


def part_two(tree_map):
    """Part Two solution."""
    mult = prod(count_trees(tree_map, *s) for s in SLOPES)
    print(f"Multiplying encountered trees gives {mult} for given slopes.")
    assert mult == 7812180000


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT)
    part_one(puzzle_input)
    part_two(puzzle_input)
