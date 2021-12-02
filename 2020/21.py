"""Day 21: Allergen Assessment."""

from aoc.puzzle import Puzzle


class Puzzle21(Puzzle):
    def parser(self):
        self.foods = []
        self.ingredients = set()
        self.allergens = {}
        for line in self.input:
            ingr, alrg = line.split(" (")
            ingr = set(ingr.split())
            alrg = set(alrg[9:-1].split(", "))
            self.foods.append(ingr)
            self.ingredients.update(ingr)
            for a in alrg:
                self.allergens[a] = self.allergens.get(a, ingr).intersection(ingr)
        print(sorted(self.allergens))

    def part_one(self):
        possibly_unsafe = set().union(*self.allergens.values())
        safe = self.ingredients.difference(possibly_unsafe)
        safe_count = 0
        for food in self.foods:
            safe_count += len(food.intersection(safe))
        return safe_count

    def part_two(self):
        while any(len(i) > 1 for i in self.allergens.values()):
            for allergen, ingredients in self.allergens.items():
                if len(ingredients) > 1:
                    continue
                found = next(iter(ingredients))
                for other_allergen in (a for a in self.allergens if a != allergen):
                    self.allergens[other_allergen].discard(found)
        return ",".join(next(iter(self.allergens[a])) for a in sorted(self.allergens))


if __name__ == "__main__":
    Puzzle21(solutions=(2317, "kbdgs,sqvv,slkfgq,vgnj,brdd,tpd,csfmb,lrnz")).solve()
