"""Day 21: RPG Simulator 20XX."""

from itertools import chain, combinations
from aoc.puzzle import Puzzle


SHOP = {  # Cost, Damage, Armor
    "Weapons": {
        "Dagger": (8, 4, 0),
        "Shortsword": (10, 5, 0),
        "Warhammer": (25, 6, 0),
        "Longsword": (40, 7, 0),
        "Greataxe": (74, 8, 0),
    },
    "Armor": {
        "Leather": (13, 0, 1),
        "Chainmail": (31, 0, 2),
        "Splintmail": (53, 0, 3),
        "Bandedmail": (75, 0, 4),
        "Platemail": (102, 0, 5),
    },
    "Rings": {
        "Damage +1": (25, 1, 0),
        "Damage +2": (50, 2, 0),
        "Damage +3": (100, 3, 0),
        "Defense +1": (20, 0, 1),
        "Defense +2": (40, 0, 2),
        "Defense +3": (80, 0, 3),
    },
}
NONE = (0, 0, 0)


class Character:
    def __init__(self, hp=100, damage=0, armor=0):
        self.full_hp = hp
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def attack(self, other):
        other.hp -= max(1, self.damage - other.armor)

    def beats(self, other):
        step = 1
        while self.hp > 0 and other.hp > 0:
            if step % 2:
                self.attack(other)
            else:
                other.attack(self)
            step += 1
        return other.hp <= 0

    def revive(self):
        self.__init__(self.full_hp, self.damage, self.armor)


def equipped_player():
    for cw, dw, aw in SHOP["Weapons"].values():
        for ca, da, aa in chain([NONE], SHOP["Armor"].values()):
            for (cr1, dr1, ar1), (cr2, dr2, ar2) in chain(
                [(NONE, NONE)],
                [(r, NONE) for r in SHOP["Rings"].values()],
                combinations(SHOP["Rings"].values(), 2),
            ):
                yield cw + ca + cr1 + cr2, Character(
                    damage=dw + da + dr1 + dr2,
                    armor=aw + aa + ar1 + ar2,
                )


class Today(Puzzle):
    def parser(self):
        boss_stats = list(map(lambda x: int(x.split(" ")[-1]), self.input))
        self.boss = Character(*boss_stats)

    def part_one(self):
        costs = set()
        for cost, player in equipped_player():
            self.boss.revive()
            if player.beats(self.boss):
                costs.add(cost)
        return min(costs)

    def part_two(self):
        costs = set()
        for cost, player in equipped_player():
            self.boss.revive()
            if not player.beats(self.boss):
                costs.add(cost)
        return max(costs)


solutions = (121, 201)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
