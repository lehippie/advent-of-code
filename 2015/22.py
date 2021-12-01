"""Day 22: Wizard Simulator 20XX."""

from copy import deepcopy
from aoc.puzzle import Puzzle


SPELLS_COSTS = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}


class Character:
    def __init__(self, hp=50, damage=0, armor=0):
        self.hp = hp
        self.damage = damage
        self.armor = armor


class Wizard(Character):
    def __init__(self, mana=500, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mana = mana
        self.shield_active = 0
        self.poison_active = 0
        self.recharge_active = 0

    def available_spells(self):
        spells = []
        for spell, cost in SPELLS_COSTS.items():
            if (
                self.mana < cost
                or (spell == "Shield" and self.shield_active > 1)
                or (spell == "Poison" and self.poison_active > 1)
                or (spell == "Recharge" and self.recharge_active > 1)
            ):
                continue
            spells.append(spell)
        return spells


class Fight:
    def __init__(self, hero: Wizard, boss: Character, hard_mode=False):
        self.hero = hero
        self.boss = boss
        self.mana_spent = 0
        self.next_spell = None
        self.spells = []
        self.hard_mode = hard_mode

    def apply_effects(self):
        if self.hero.shield_active:
            self.hero.shield_active -= 1
            if not self.hero.shield_active:
                self.hero.armor = 0
        if self.hero.poison_active:
            self.hero.poison_active -= 1
            self.boss.hp -= 3
        if self.hero.recharge_active:
            self.hero.recharge_active -= 1
            self.hero.mana += 101

    def hero_turn(self):
        self.spells.append(self.next_spell)
        self.hero.mana -= SPELLS_COSTS[self.next_spell]
        self.mana_spent += SPELLS_COSTS[self.next_spell]
        if self.next_spell == "Magic Missile":
            self.boss.hp -= 4
        elif self.next_spell == "Drain":
            self.boss.hp -= 2
            self.hero.hp += 2
        elif self.next_spell == "Shield":
            self.hero.armor = 7
            self.hero.shield_active = 6
        elif self.next_spell == "Poison":
            self.hero.poison_active = 6
        elif self.next_spell == "Recharge":
            self.hero.recharge_active = 5

    def next_turn(self, spell):
        if self.hard_mode:
            self.hero.hp -= 1
            if self.hero.hp <= 0:
                return "lost"
        self.next_spell = spell
        for action in (self.apply_effects, self.hero_turn, self.apply_effects):
            action()
            if self.boss.hp <= 0:
                return "won"
        self.hero.hp -= max(1, self.boss.damage - self.hero.armor)
        if self.hero.hp <= 0:
            return "lost"

    def __str__(self):
        return " > ".join(self.spells)


def least_mana_fight(initial_fight: Fight):
    fights = [initial_fight]
    while fights:
        current_fight = fights.pop(0)
        for spell in current_fight.hero.available_spells():
            fight = deepcopy(current_fight)
            result = fight.next_turn(spell)
            if result == "won":
                # print(fight.mana_spent, fight)
                return fight.mana_spent
            elif result is None:
                fights.append(fight)


class Puzzle22(Puzzle):
    def parser(self):
        stats = list(map(lambda x: int(x.split(" ")[-1]), self.input))
        return {"hp": stats[0], "damage": stats[1]}

    def part_one(self, hard_mode=False):
        fight = Fight(Wizard(), Character(**self.input), hard_mode)
        return least_mana_fight(fight)

    def part_two(self):
        return self.part_one(hard_mode=True)


if __name__ == "__main__":
    Puzzle22(solutions=(1269, 1309)).solve()
