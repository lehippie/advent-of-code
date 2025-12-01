"""--- Day 24: Crossed Wires ---"""

from operator import __and__, __or__, __xor__
from aoc.puzzle import Puzzle

OP = {"AND": __and__, "OR": __or__, "XOR": __xor__}


class Wires:
    def __init__(self, wires):
        self.wires = wires.copy()

    def __getitem__(self, key):
        if not isinstance(self.wires[key], int):
            op, w1, w2 = self.wires[key]
            self.wires[key] = OP[op](self[w1], self[w2])
        return self.wires[key]


class Today(Puzzle):
    def parser(self):
        self.wires = {}
        for line in self.input:
            if ":" in line:
                wire, value = line.split(": ")
                self.wires[wire] = int(value)
            elif "->" in line:
                inputs, output = line.split(" -> ")
                w1, op, w2 = inputs.split()
                self.wires[output] = (op, w1, w2)

    def part_one(self):
        wires = Wires(self.wires)
        number = 0
        for bit in sorted((w for w in self.wires if w[0] == "z"), reverse=True):
            number *= 2
            number += wires[bit]
        return number

    def part_two(self):
        """Thanks to https://en.wikipedia.org/wiki/Adder_(electronics),
        for teaching about the gates logic of adding two binary numbers.
        Theory for the n-th adder:
            x XOR y -> a
            x AND y -> b
            a XOR carry_{n-1} -> z
            a AND carry_{n-1} -> c
            b OR c -> carry_{n}
        
        Theory for the starting adder (without previous carry):
            x XOR y -> z
            x AND y -> carry_{1}
        
        By looking at the wiring of the 5 gates for each bit adder,
        misconnections could be found.
        """
        return super().part_two()


if __name__ == "__main__":
    test = Today(
        test_input="""x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""
    )
    r1 = test.part_one()
    assert r1 == 2024, r1
    # r2 = test.part_two()
    # assert r2 == expected_result, r2

    Today().solve()
