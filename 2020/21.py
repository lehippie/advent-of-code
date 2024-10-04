"""Day 21: Allergen Assessment."""

from copy import deepcopy
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        """Foods are stored in a list as sets of ingredients.
        Existing ingredients are stored in a set.
        Allergens are stored as keys of a dictionnary where values
        are the common ingredients in foods where they appear.
        """
        self.foods = []
        self.ingredients = set()
        self.allergens = {}
        for line in self.input:
            ingr, alrg = line.split(" (contains ")
            ingr = set(ingr.split())
            alrg = set(alrg[:-1].split(", "))
            self.foods.append(ingr)
            self.ingredients.update(ingr)
            for a in alrg:
                self.allergens[a] = self.allergens.get(a, ingr).intersection(ingr)

    def part_one(self):
        """Safe ingredients are the ones that are not risky, meaning
        they do not appear in allergens dictionnary.
        """
        risky = set.union(*self.allergens.values())
        return sum(len(food.difference(risky)) for food in self.foods)

    def part_two(self):
        """Iteratively filter each allergens' possible ingredients
        with the ones that have only one possibility.
        """
        allergens = deepcopy(self.allergens)
        while any(len(i) > 1 for i in allergens.values()):
            for alrg, ingr in allergens.items():
                if len(ingr) == 1:
                    for other in (a for a in allergens if a != alrg):
                        allergens[other].difference_update(ingr)
        return ",".join(allergens[a].pop() for a in sorted(allergens))


if __name__ == "__main__":
    Today().solve()
