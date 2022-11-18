#!/usr/bin/env python

"""Create a new puzzle.

Usage:
    {name} [(<year> <day>)]
    {name} --help

Arguments:
    <year>, <day>       Date of the new day (default: today).

Options:
    -h, --help          Show this help.
"""

import re
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen

from docopt import docopt

from aoc import ROOT, CONFIG


TEMPLATE = '''"""{title}."""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        pass

    def part_one(self):
        return super().part_one()

    def part_two(self):
        return super().part_two()


solutions = (None, None)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
'''


def day_title(year, day):
    request = Request(
        url=f"https://adventofcode.com/{year}/day/{int(day)}",
        headers={"cookie": f"session={CONFIG['www']['session']}"},
    )
    with urlopen(request) as response:
        response = response.read().decode("utf-8")
        return re.findall(r"--- (Day.*) ---", response)[0]


def create_file(year, day):
    puzzle_path = ROOT / str(year) / f"{day:>02}.py"
    if puzzle_path.exists():
        answer = input("Puzzle file already exists. Overwrite? [y/N] ")
        if not answer.lower().startswith("y"):
            print("Aborted.")
            return
    puzzle_path.parent.mkdir(parents=True, exist_ok=True)
    puzzle_path.write_text(TEMPLATE.format(title=day_title(year, day)))
    print(f"New puzzle created at {puzzle_path}")


if __name__ == "__main__":
    args = docopt(__doc__.format(name=Path(__file__).name))
    now = datetime.now()

    if args["<year>"] is None:
        if now.month != 12:
            print("We're not in December yet. Please enter year and day manually.")
            exit()
        args["<year>"] = now.year
        args["<day>"] = now.day

    date = datetime(int(args["<year>"]), 12, int(args["<day>"]))
    if 1 <= date.day <= 25 and datetime(2015, 12, 1) <= date <= now:
        create_file(date.year, date.day)
    else:
        print(f"No existing puzzle on day {date.day} of year {date.year}.")
