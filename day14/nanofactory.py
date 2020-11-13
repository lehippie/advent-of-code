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
        self.reactor = self.reactions[final_product].copy()
        self.raw_material = raw_material


    @classmethod
    def from_file(cls, file, **kwargs):
        """Init a Factory from a file where each line is a reaction."""
        with open(file) as f:
            reactions = [line.strip() for line in f]
        return cls(reactions, **kwargs)


    def parse_input(self, reactions, reac_sep=",", prod_sep="=>"):
        """Read reactions and extract content."""
        parsed = {}
        for reaction in reactions:
            reactives, product = reaction.split(prod_sep)
            prod_q, product = product.strip().split(" ")
            parsed[product] = {"quantity": int(prod_q)}
            reactives = reactives.split(reac_sep)
            for reactive in reactives:
                chem_q, chemical = reactive.strip().split(" ")
                parsed[product][chemical] = int(chem_q)
        return parsed


    def run_one_cycle(self):
        """Update reactor by replacing one level of needed chemicals"""
        for chemical, needed in self.reactor.copy().items():
            if chemical in ["quantity", self.raw_material] or needed < 0:
                continue
            source = self.reactions[chemical]
            how_many = ceil(needed / source["quantity"])
            self.reactor[chemical] -= source["quantity"] * how_many
            for src_chem, src_q in source.items():
                if src_chem == "quantity":
                    continue
                self.reactor[src_chem] = self.reactor.get(src_chem, 0)
                self.reactor[src_chem] += src_q * how_many
        self.reactor = {c: q for c, q in self.reactor.items() if q != 0}        


    @property
    def is_simplified(self):
        """Check if <raw_material> is the only reactive.."""
        status = {c: q for c, q in self.reactor.items() if q > 0}
        return set(status.keys()) == set(["quantity", self.raw_material])


    def simplify(self):
        """Do cycles until needed reactives are converted to <raw_materials>."""
        while not self.is_simplified:
            self.run_one_cycle()
        return self.reactor[self.raw_material]

    
    # def produce(self, raw_quantity=1000000000000):
    #     """Calculate how many <final_product> can be produced."""
    #     if not self.is_simplified():
    #         self.simplify()
    #     return raw_quantity // self.simplify()


def tests():
    from pathlib import Path
    test_dir = Path(__file__).parent / "test_reactions"
    
    fac = Factory.from_file(test_dir / "1.txt")
    assert fac.simplify() == 31, fac.simplify()

    fac = Factory.from_file(test_dir / "2.txt")
    assert fac.simplify() == 165, fac.simplify()

    fac = Factory.from_file(test_dir / "3.txt")
    assert fac.simplify() == 13312, fac.simplify()
    # assert fac.produce() == 82892753, fac.produce()

    fac = Factory.from_file(test_dir / "4.txt")
    assert fac.simplify() == 180697, fac.simplify()
    # assert fac.produce() == 5586022, fac.produce()

    fac = Factory.from_file(test_dir / "5.txt")
    assert fac.simplify() == 2210736, fac.simplify()
    # assert fac.produce() == 460664, fac.produce()


if __name__ == "__main__":
    tests()
