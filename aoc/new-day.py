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
from datetime import date
from pathlib import Path

from docopt import docopt

from aoc import ROOT, download_day


TEMPLATE = '''"""{title}"""

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
    Today(test_input="test.txt").solve([None, None])
    # Today().solve()
'''


def create_file(year: int, day: int) -> None:
    """Create a file to solve the puzzle of given day."""
    puzzle_path = ROOT / f"{year}" / f"{day:>02}.py"
    if puzzle_path.exists():
        answer = input("Puzzle file already exists. Overwrite? [y/N] ")
        if not answer.lower().startswith("y"):
            print("Aborted.")
            return
    title = re.findall(r"--- Day.* ---", download_day(year, day))[0]
    puzzle_path.parent.mkdir(parents=True, exist_ok=True)
    puzzle_path.write_text(TEMPLATE.format(title=title))
    print(f"New puzzle created at {puzzle_path}")


if __name__ == "__main__":
    args = docopt(__doc__.format(name=Path(__file__).name))
    if args["<year>"]:
        puzzle = date(int(args["<year>"]), 12, int(args["<day>"]))
    else:
        puzzle = date.today()

    if 2015 <= puzzle.year <= 2023 and 1 <= puzzle.day <= 25:
        create_file(puzzle.year, puzzle.day)
    else:
        print(f"No puzzle for day {puzzle.day} of year {puzzle.year}")
