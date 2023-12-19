"""--- Day 19: Aplenty ---"""

from collections import defaultdict
from aoc.puzzle import Puzzle


COMP = {"<": lambda i, j: i < j, ">": lambda i, j: i > j}


def accepted(part, workflows, name="in"):
    if name == "A":
        return True
    if name == "R":
        return False
    for check, number, next_step in workflows[name]:
        if COMP[check[1]](part[check[0]], number):
            return accepted(part, workflows, next_step)


class Today(Puzzle):
    def parser(self):
        workflows, parts = "\n".join(self.input).split("\n\n")

        self.workflows = defaultdict(list)
        for wf in workflows.split("\n"):
            name, rules = wf.split("{")
            rules = rules[:-1].split(",")
            for rule in rules[:-1]:
                number, result = rule[2:].split(":")
                self.workflows[name].append((rule[:2], int(number), result))
            self.workflows[name].append(("x>", 0, rules[-1]))

        self.parts = []
        for part in parts.split("\n"):
            self.parts.append({p[0]: int(p[2:]) for p in part.strip("{}").split(",")})

    def part_one(self):
        return sum(
            sum(part.values()) for part in self.parts if accepted(part, self.workflows)
        )

    def part_two(self):
        return super().part_two()


solutions = (421983, None)

if __name__ == "__main__":
    Today(infile="test.txt", solutions=(19114, 167409079868000)).solve()
    # Today(solutions=solutions).solve()
