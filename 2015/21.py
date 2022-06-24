"""Day 21: RPG Simulator 20XX."""

from itertools import chain, combinations
from aoc.puzzle import Puzzle


SHOP = {
    "Weapons": {  # Cost, Damage
        "Dagger": (8, 4),
        "Shortsword": (10, 5),
        "Warhammer": (25, 6),
        "Longsword": (40, 7),
        "Greataxe": (74, 8),
    },
    "Armor": {  # Cost, Armor
        "None": (0, 0),
        "Leather": (13, 1),
        "Chainmail": (31, 2),
        "Splintmail": (53, 3),
        "Bandedmail": (75, 4),
        "Platemail": (102, 5),
    },
    "Rings": {  # Cost, Damage, Armor
        "Damage +1": (25, 1, 0),
        "Damage +2": (50, 2, 0),
        "Damage +3": (100, 3, 0),
        "Defense +1": (20, 0, 1),
        "Defense +2": (40, 0, 2),
        "Defense +3": (80, 0, 3),
    },
}
NORING = (0, 0, 0)


class Character:
    def __init__(self, hp=100, damage=0, armor=0):
        self.full_hp = hp
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, other):
        other.hp -= max(1, self.damage - other.armor)

    def beats(self, other):
        """Calculate combat and return True in case of victory."""
        turn = 1
        while self.hp > 0 and other.hp > 0:
            if turn % 2:
                self.attack(other)
            else:
                other.attack(self)
            turn += 1
        return other.hp <= 0

    def revive(self):
        self.__init__(self.full_hp, self.damage, self.armor)


def equipments():
    """Generator yielding possible combinations of damage, armor
    and the corresponding amount of gold spent.
    """
    for weapon_cost, damage in SHOP["Weapons"].values():
        for armor_cost, armor in SHOP["Armor"].values():
            for (lr_cost, lr_dmg, lr_armor), (rr_cost, rr_dmg, rr_armor) in chain(
                [(NORING, NORING)],
                [(ring, NORING) for ring in SHOP["Rings"].values()],
                combinations(SHOP["Rings"].values(), 2),
            ):
                yield (
                    damage + lr_dmg + rr_dmg,
                    armor + lr_armor + rr_armor,
                    weapon_cost + armor_cost + lr_cost + rr_cost,
                )


class Today(Puzzle):
    def parser(self):
        boss_stats = list(map(lambda x: int(x.split(" ")[-1]), self.input))
        self.boss = Character(*boss_stats)

    def part_one(self):
        costs = set()
        for damage, armor, gold in equipments():
            player = Character(damage=damage, armor=armor)
            self.boss.revive()
            if player.beats(self.boss):
                costs.add(gold)
        return min(costs)

    def part_two(self):
        costs = set()
        for damage, armor, gold in equipments():
            player = Character(damage=damage, armor=armor)
            self.boss.revive()
            if not player.beats(self.boss):
                costs.add(gold)
        return max(costs)


solutions = (121, 201)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
