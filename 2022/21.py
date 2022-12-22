"""Day 21: Monkey Math."""

from copy import deepcopy
from operator import add, sub, mul, floordiv
from aoc.puzzle import Puzzle

OP = {"+": add, "-": sub, "*": mul, "/": floordiv}
NOP = {"+": "-", "-": "+", "*": "/", "/": "*"}


class Today(Puzzle):
    def parser(self):
        self.monkeys = {}
        for line in self.input:
            monkey, yell = line.split(": ")
            self.monkeys[monkey] = int(yell) if yell.isdigit() else yell.split()

    def part_one(self):
        """Separate monkeys in yellers and waiters and recursively
        calculate what waiters must yell.
        """
        yellers, waiters = {}, {}
        for monkey, yell in self.monkeys.items():
            if isinstance(yell, int):
                yellers[monkey] = yell
            else:
                waiters[monkey] = yell
        while "root" in waiters:
            for monkey, (m1, op, m2) in deepcopy(waiters).items():
                if m1 in yellers and m2 in yellers:
                    yellers[monkey] = OP[op](yellers[m1], yellers[m2])
                    del waiters[monkey]
        return yellers["root"]

    def part_two(self):
        """Explore the graph of yelling monkeys to find the chain
        leading to 'humn'. The other side of the root equality can
        be calculated and the equation solved by following the chain
        until only 'humn' remains.
        """
        monkeys = deepcopy(self.monkeys)
        del monkeys["humn"]
        root1, _, root2 = monkeys.pop("root")

        frontier = [[root1], [root2]]
        while frontier:
            chain = frontier.pop(0)
            if chain[-1] == "humn":
                break
            if isinstance(monkeys[chain[-1]], int):
                continue
            next1, _, next2 = monkeys[chain[-1]]
            frontier.append(chain + [next1])
            frontier.append(chain + [next2])

        def calculate(monkey):
            """Get the number yelled when 'humn' is not needed."""
            yell = monkeys[monkey]
            if isinstance(yell, int):
                return yell
            m1, op, m2 = yell
            return OP[op](calculate(m1), calculate(m2))

        def solve(result, number, op, side):
            """Reduce the result of the equation according the
            operator and the side where the number is.
            """
            if op == "+" or op == "*" or side == "right":
                return OP[NOP[op]](result, number)
            return OP[op](number, result)

        result = calculate(root1 if root2 == chain[0] else root2)
        while len(chain) > 1:
            m1, op, m2 = monkeys[chain.pop(0)]
            if m1 == chain[0]:
                number = calculate(m2)
                result = solve(result, number, op, "right")
            else:
                number = calculate(m1)
                result = solve(result, number, op, "left")
        return result


solutions = (145167969204648, 3330805295850)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
