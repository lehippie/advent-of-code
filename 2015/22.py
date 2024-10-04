"""Day 22: Wizard Simulator 20XX."""

from collections import deque
from copy import deepcopy
from math import inf
from aoc.puzzle import Puzzle


SPELLS = {  # Name: Cost
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}


class Character:
    def __init__(self, hp=50, mana=500, damage=0, armor=0):
        self.hp = hp
        self.mana = mana
        self.damage = damage
        self.armor = armor


class Fight:
    def __init__(self, hero: Character, boss: Character, hard_mode=False):
        self.hero = hero
        self.boss = boss
        self.effects = {"Shield": 0, "Poison": 0, "Recharge": 0}
        self.cost = 0
        self.spells = []
        self.hard_mode = hard_mode

    @property
    def state(self):
        return (self.hero.hp, self.hero.mana, self.boss.hp, *self.effects.values())

    def combat_step(self, spell):
        """Perform hero and boss turns.

        During his turn, the hero will cast <spell>.
        If the fight ended, return result from the hero perspective.
        """
        if self.hard_mode:
            self.hero.hp -= 1
            if self.hero.hp <= 0:
                return "lost"
        for action in (self.apply_effects, self.hero_action, self.apply_effects):
            action(spell)
            if self.boss.hp <= 0:
                return "won"
        self.hero.hp -= max(1, self.boss.damage - self.hero.armor)
        if self.hero.hp <= 0:
            return "lost"

    def apply_effects(self, *args):
        if self.effects["Shield"]:
            self.effects["Shield"] -= 1
            if not self.effects["Shield"]:
                self.hero.armor = 0
        if self.effects["Poison"]:
            self.effects["Poison"] -= 1
            self.boss.hp -= 3
        if self.effects["Recharge"]:
            self.effects["Recharge"] -= 1
            self.hero.mana += 101

    def hero_action(self, spell):
        self.spells.append(spell)
        self.hero.mana -= SPELLS[spell]
        self.cost += SPELLS[spell]
        if spell == "Magic Missile":
            self.boss.hp -= 4
        elif spell == "Drain":
            self.boss.hp -= 2
            self.hero.hp += 2
        elif spell == "Shield":
            self.hero.armor = 7
            self.effects["Shield"] = 6
        elif spell == "Poison":
            self.effects["Poison"] = 6
        elif spell == "Recharge":
            self.effects["Recharge"] = 5

    def available_spells(self):
        """Generator yielding available spells at the start of
        the combat step, based on mana and effects. Effects are
        available even at 1 because they can be casted just after
        wearing off.
        """
        for spell, cost in SPELLS.items():
            if self.hero.mana >= cost and self.effects.get(spell, 0) <= 1:
                yield spell


def least_mana_winner(initial_fight: Fight):
    """BFS while keeping trck of seen states to limit exploration."""
    fights = deque([initial_fight])
    states = set(initial_fight.state)
    best = deepcopy(initial_fight)
    best.cost = inf
    while fights:
        current_fight = fights.popleft()
        if current_fight.cost >= best.cost:
            continue
        for spell in current_fight.available_spells():
            fight = deepcopy(current_fight)
            result = fight.combat_step(spell)
            state = fight.state
            if result == "won" and fight.cost < best.cost:
                best = fight
            elif result is None and state not in states and fight.cost < best.cost:
                states.add(state)
                fights.append(fight)
    # print(best.cost, " > ".join(best.spells))
    return best.cost


class Today(Puzzle):
    def parser(self):
        stats = list(map(lambda x: int(x.split(" ")[-1]), self.input))
        self.boss_stats = {"hp": stats[0], "damage": stats[1]}

    def part_one(self, hard_mode=False):
        fight = Fight(Character(), Character(**self.boss_stats), hard_mode)
        return least_mana_winner(fight)

    def part_two(self):
        return self.part_one(hard_mode=True)


if __name__ == "__main__":
    Today().solve()
