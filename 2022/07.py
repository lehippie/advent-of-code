"""Day 7: No Space Left On Device."""

from aoc.puzzle import Puzzle


class Dir(list):
    def size(self):
        """Recursive size calculation for list class."""
        return sum(c.size() if isinstance(c, Dir) else c[0] for c in self)


class Today(Puzzle):
    def parser(self):
        """Group commands and outputs together."""
        self.commands = "|".join(self.input).split("$ ")
        self.commands = [c.rstrip("|").split("|") for c in self.commands if c]

    def create_tree(self):
        """Read commands and outputs to construct a tree. Absolute
        paths are used because directories with the same name can
        exists in different places.
        """
        self.tree = {"/": Dir()}
        for cmd, *output in self.commands:
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
                        self.tree[dname] = Dir()
                        self.tree[cwd].append(self.tree[dname])
                    else:
                        size, fname = thing.split()
                        self.tree[cwd].append((int(size), fname))

    def part_one(self):
        self.create_tree()
        self.sizes = [d.size() for d in self.tree.values()]
        return sum(s for s in self.sizes if s <= 100000)

    def part_two(self):
        freespace = 70000000 - max(self.sizes)
        return next(s for s in sorted(self.sizes) if freespace + s >= 30000000)


solutions = (1086293, 366028)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
