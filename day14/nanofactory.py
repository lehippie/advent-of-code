"""Nanofactory library."""

from math import ceil


class Factory:
    """Chemical factory.
    
    Arguments:
        reactions           List of reactions the factory can perform.
        final_product       Chemical to fabricate.
        raw_material        Available reactive.
    """

    def __init__(self, reactions, final_product="FUEL", raw_material="ORE"):
        self.reactions = self.parse_input(reactions)
        self.final_product = final_product
        self.raw_material = raw_material
        self.direct_reaction = self.simplify(
            reaction=self.reactions[final_product],
            reactive=raw_material,
        )


    @classmethod
    def from_file(cls, file, **kwargs):
        """Init a Factory from a file where each line is a reaction."""
        with open(file) as f:
            reactions = [line.strip() for line in f]
        return cls(reactions, **kwargs)


    @staticmethod
    def parse_input(reactions, reac_sep=",", prod_sep="=>"):
        """Read reactions and extract content."""
        parsed = {}
        for reaction in reactions:
            reactives, product = reaction.split(prod_sep)
            prod_q, product = product.strip().split(" ")
            parsed[product] = {"_q": int(prod_q)}
            reactives = reactives.split(reac_sep)
            for reactive in reactives:
                chem_q, chemical = reactive.strip().split(" ")
                parsed[product][chemical] = int(chem_q)
        return parsed


    @staticmethod
    def is_simplified(reaction, reactive):
        """Check if <reactive> is the only needed reactive of <reaction>."""
        status = {c: q for c, q in reaction.items() if q > 0}
        return set(status.keys()) == set(["_q", reactive])


    def simplify(self, reaction, reactive):
        """Make <reactive> the only one needed in <reaction>."""
        reaction = reaction.copy()
        while not self.is_simplified(reaction, reactive):
            for chemical, needed_quantity in reaction.copy().items():
                if (chemical in ["_q", reactive] or needed_quantity <= 0):
                    continue
                source = self.reactions[chemical]
                how_many = ceil(needed_quantity / source["_q"])
                reaction[chemical] -= source["_q"] * how_many
                for src_chemical, src_q in source.items():
                    if src_chemical != "_q":
                        reaction[src_chemical] = (
                            reaction.get(src_chemical, 0)
                            + src_q * how_many
                        )
        return {c: q for c, q in reaction.items() if q != 0}


    def is_producible(self, product_quantity, raw_material_quantity):
        """Can <product_quantity> be produced from <raw_material_quantity>."""
        target_reaction = {
            c: q * product_quantity
            for c, q in self.reactions[self.final_product].items()
        }
        target_reaction = self.simplify(target_reaction, self.raw_material)
        return target_reaction[self.raw_material] <= raw_material_quantity


    def produce(self, raw_material_quantity=10**12):
        """How many <final_product> can be producted from <raw_material>."""
        low = raw_material_quantity // self.direct_reaction[self.raw_material]
        high = low * 2
        while self.is_producible(high, raw_material_quantity):
            low = high
            high = low * 2
        while high - low != 1:
            mid = (high + low) // 2
            if self.is_producible(mid, raw_material_quantity):
                low = mid
            else:
                high = mid
        return low


def tests():
    from pathlib import Path
    test_dir = Path(__file__).parent / "test_reactions"
    
    fac = Factory.from_file(test_dir / "1.txt")
    assert fac.direct_reaction["ORE"] == 31

    fac = Factory.from_file(test_dir / "2.txt")
    assert fac.direct_reaction["ORE"] == 165

    fac = Factory.from_file(test_dir / "3.txt")
    assert fac.direct_reaction["ORE"] == 13312
    assert fac.produce() == 82892753

    fac = Factory.from_file(test_dir / "4.txt")
    assert fac.direct_reaction["ORE"] == 180697
    assert fac.produce() == 5586022

    fac = Factory.from_file(test_dir / "5.txt")
    assert fac.direct_reaction["ORE"] == 2210736
    assert fac.produce() == 460664


if __name__ == "__main__":
    tests()
