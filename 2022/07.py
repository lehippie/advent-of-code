"""Day 7: No Space Left On Device."""

from aoc.puzzle import Puzzle


class Dir(list):
    def size(self):
        """Recursive size method for lists."""
        return sum(c.size() if isinstance(c, Dir) else c[0] for c in self)


def create_tree(commands):
    """Read commands and their outputs to construct a directory tree.
    Absolute paths are used because directories with the same name
    can exists in different places.
    """
    tree = {"root": Dir()}
    for cmd, *output in commands:
        if "cd" in cmd:
            destination = cmd[3:]
            if destination == "/":
                cwd = "root"
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
        """Group commands and outputs together."""
        self.commands = "|".join(self.input).split("$ ")
        self.commands = [c.rstrip("|").split("|") for c in self.commands if c]

    def part_one(self):
        tree = create_tree(self.commands)
        self.sizes = [d.size() for d in tree.values()]
        return sum(s for s in self.sizes if s <= 100000)

    def part_two(self):
        freespace = 70000000 - max(self.sizes)
        return next(s for s in sorted(self.sizes) if freespace + s >= 30000000)


if __name__ == "__main__":
    Today().solve()
