"""--- Day 19: Aplenty ---"""

from math import prod
from collections import defaultdict
from aoc.puzzle import Puzzle


COMP = {"<": lambda i, j: i < j, ">": lambda i, j: i > j}


def accepted(part, workflows, name="in"):
    for rating, check, limit, next_step in workflows[name]:
        if COMP[check](part[rating], limit):
            if next_step == "A":
                return True
            if next_step == "R":
                return False
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
                self.workflows[name].append((rule[0], rule[1], int(number), result))
            self.workflows[name].append(("x", ">", 0, rules[-1]))

        self.parts = []
        for part in parts.split("\n"):
            self.parts.append({p[0]: int(p[2:]) for p in part.strip("{}").split(",")})

    def part_one(self):
        return sum(
            sum(part.values()) for part in self.parts if accepted(part, self.workflows)
        )

    def part_two(self):
        """Pathfinding through the workflows."""
        count = 0
        frontier = [("in", {r: (1, 4000) for r in "xmas"})]
        while frontier:
            name, parts = frontier.pop()
            if name == "A":
                count += prod(b - a + 1 for a, b in parts.values())
                continue
            if name == "R":
                continue
            for rating, check, limit, next_step in self.workflows[name]:
                m, M = parts[rating]
                if m < limit < M:
                    if check == "<":
                        ranges = [(m, limit - 1), (limit, M)]
                    else:
                        ranges = [(m, limit), (limit + 1, M)]
                else:
                    ranges = [[m, M]]

                for rm, rM in ranges:
                    if (check == "<" and rM < limit) or (check == ">" and rm > limit):
                        new_parts = parts.copy()
                        new_parts[rating] = (rm, rM)
                        frontier.append((next_step, new_parts))
                    else:
                        parts[rating] = (rm, rM)
        return count


solutions = (421983, 129249871135292)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
