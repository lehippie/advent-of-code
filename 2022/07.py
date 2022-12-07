"""Day 7: No Space Left On Device."""

from aoc.puzzle import Puzzle


class Dir(list):
    @property
    def size(self):
        return sum(c.size if isinstance(c, Dir) else c[0] for c in self)


def explore_tree(commands):
    tree = {"/": Dir()}
    for cmd, *output in commands:
        if "cd" in cmd:
            destination = cmd[3:]
            if destination == "/":
                cwd = destination
            elif destination == "..":
                cwd = cwd[: cwd.rfind("/")]
            else:
                cwd = f"{cwd}/{destination}"
        elif cmd == "ls":
            for thing in output:
                if thing.startswith("dir"):
                    dname = f"{cwd}/{thing[4:]}"
                    tree[dname] = Dir()
                    tree[cwd].append(tree[dname])
                else:
                    size, fname = thing.split()
                    tree[cwd].append((int(size), fname))
    return tree


class Today(Puzzle):
    def parser(self):
        cmds = "|".join(self.input).split("$ ")
        self.commands = [c.rstrip("|").split("|") for c in cmds if c]

    def part_one(self):
        tree = explore_tree(self.commands)
        self.sizes = [d.size for d in tree.values()]
        return sum(s for s in self.sizes if s <= 100000)

    def part_two(self):
        freespace = 70000000 - max(self.sizes)
        return next(s for s in sorted(self.sizes) if freespace + s >= 30000000)


solutions = (1086293, 366028)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
