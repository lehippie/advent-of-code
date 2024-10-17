"""--- Day 14: Space Stoichiometry ---"""

from collections import defaultdict
from math import ceil
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        """Convert reactions in format na A, nb B => nc C in a dict
        with format {C: [nc, {A: na, B: nb}]}.
        """
        self.reactions = {}
        for reaction in self.input:
            reactives, product = reaction.split(" => ")
            quantity, product = product.split(" ")
            self.reactions[product] = [int(quantity), {}]
            reactives = reactives.split(", ")
            for reactive in reactives:
                quantity, chemical = reactive.split(" ")
                self.reactions[product][1][chemical] = int(quantity)

    def part_one(self, fuel_amount=1):
        """In the FUEL-producing reaction, we replace the chemical needed
        by their reactives until only ORE remains.
        Surplus of chemicals are stored as negative values in the needed
        dict to be used afterwards.
        """
        needed = defaultdict(int)
        for chemical, amount in self.reactions["FUEL"][1].items():
            needed[chemical] += amount * fuel_amount

        while not all(q < 0 for c, q in needed.items() if c != "ORE"):
            for product, quantity_needed in needed.copy().items():
                if product == "ORE" or quantity_needed < 0:
                    continue
                quantity_produced, reactives = self.reactions[product]
                reaction_amount = ceil(quantity_needed / quantity_produced)
                needed[product] -= reaction_amount * quantity_produced
                if not needed[product]:
                    del needed[product]
                for chemical, q in reactives.items():
                    needed[chemical] += q * reaction_amount
        return needed["ORE"]

    def part_two(self):
        """Part one gave us a function giving the ORE needed to produce a
        specific amount of FUEL. To find the maximum FUEL produced by 1 trillon
        ORE, we can use dichotomy between two values that needs respectively
        less and more than 1 trillion ORE.
        To init the interval, the minimum is 1 trillion divided by part_one
        result, and the maximum is searched as the next multiple of the minimum
        needing more than 1 trillon ORE.
        """
        cargo = 1000000000000
        mini = cargo // self.part_one(1)
        maxi = next(mini * k for k in range(2, 10) if self.part_one(mini * k) > cargo)
        while maxi - mini != 1:
            mid = (maxi + mini) // 2
            if self.part_one(mid) <= cargo:
                mini = mid
            else:
                maxi = mid
        return mini


if __name__ == "__main__":
    Today().solve()
