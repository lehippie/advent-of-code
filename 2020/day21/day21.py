"""Day 21: Allergen Assessment."""

from pathlib import Path


INPUT_FILE = "foods.txt"

def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    foods = []
    ingredients = set()
    allergens = {}
    with filepath.open() as f:
        for line in f:
            ingr, alrg = line.split(" (")
            ingr = set(ingr.split())
            alrg = set(alrg[9:-2].split(", "))
            foods.append(ingr)
            ingredients.update(ingr)
            for a in alrg:
                allergens[a] = allergens.get(a, ingr).intersection(ingr)
    return foods, ingredients, allergens


# --- Part One ---

def part_one(foods, ingredients, allergens):
    possibly_unsafe = set().union(*allergens.values())
    safe = ingredients.difference(possibly_unsafe)
    safe_count = 0
    for food in foods:
        safe_count += len(food.intersection(safe))
    return safe_count


# --- Part Two ---

def part_two(allergens):
    while any(len(i) > 1 for i in allergens.values()):
        for allergen, ingredients in allergens.items():
            if len(ingredients) > 1:
                continue
            found = next(iter(ingredients))
            for other_allergen in (a for a in allergens if a != allergen):
                allergens[other_allergen].discard(found)
    return ",".join(next(iter(allergens[a])) for a in sorted(allergens))


# --- Tests & Run ---

def tests():
    test = load_input("test.txt")
    assert part_one(*test) == 5
    assert part_two(test[2]) == "mxmxvkd,sqjhc,fvjkl"


if __name__ == "__main__":
    tests()

    puzzle_input = load_input(INPUT_FILE)

    result_one = part_one(*puzzle_input)
    print(f"Part One answer: {result_one}")
    assert result_one == 2317

    result_two = part_two(puzzle_input[2])
    print(f"Part Two answer: {result_two}")
    assert result_two == "kbdgs,sqvv,slkfgq,vgnj,brdd,tpd,csfmb,lrnz"
