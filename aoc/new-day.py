#!/usr/bin/env python

"""Create a new puzzle.

Usage:
    {name} [(<year> <day>)]
    {name} --help

Arguments:
    <year>, <day>       Date of the puzzle to create.
                        Default: today.

Options:
    -h, --help          Show this help.
"""

import re
from datetime import date
from pathlib import Path

from docopt import docopt

from aoc import ROOT, download_day


TODAY = date.today()
TEMPLATE = '''"""{title}"""

from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        pass

    def part_one(self):
        return super().part_one()

    def part_two(self):
        return super().part_two()


if __name__ == "__main__":
    # test = Today(test_input="""parse_lines_here""")
    # a = test.part_one()
    # assert a == expected_result, a

    Today().solve()
'''


def check_date(puzzle_date: date) -> bool:
    """Verify if a puzzle exists on given date.

    Arguments:
        puzzle: `datetime.date` of the puzzle.

    Returns:
        True if a puzzle is available on given date, False otherwise.
    """
    if puzzle_date.day > 25:
        return False

    if date(TODAY.year, 12, 1) <= TODAY <= date(TODAY.year, 12, 25):
        last_puzzle = TODAY
    elif TODAY.month == 12:
        last_puzzle = date(TODAY.year, 12, 25)
    else:
        last_puzzle = date(TODAY.year - 1, 12, 25)

    return date(2015, 12, 1) <= puzzle_date <= last_puzzle


def create_puzzle_file(year: int, day: int) -> None:
    """Create a basic file to solve <puzzle> day.

    Arguments:
        year, day: Date of the puzzle.
    """
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
    elif TODAY.month == 12 and TODAY.day < 26:
        puzzle = TODAY
    else:
        raise IOError("Today is not a puzzle day.")

    if check_date(puzzle):
        create_puzzle_file(puzzle.year, puzzle.day)
    else:
        print(f"There is no puzzle on day {puzzle.day} of {puzzle.year}")
