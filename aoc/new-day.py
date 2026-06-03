#!/usr/bin/env python

"""Create a new puzzle solver.

Usage:
    new-day.py [(<year> <day>)]
    new-day.py --help

Arguments:
    <year>, <day>       Date of the puzzle to create.
                        Default: today.

Options:
    -h, --help          Show this help.
"""

import re
from datetime import date

from docopt import docopt

from aoc import ROOT, check_date, download_day

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
    # r1 = test.part_one()
    # assert r1 == expected_result, r1
    # r2 = test.part_two()
    # assert r2 == expected_result, r2

    Today().solve()
'''


def create_puzzle_file(year: int, day: int) -> None:
    """Create a template file to solve <puzzle> day.

    Arguments:
        year, day: Date of the puzzle.
    """
    puzzle_path = ROOT / f"{year}" / f"{day:>02}.py"
    if puzzle_path.exists():
        answer = input("Puzzle file already exists. Overwrite? [y/N] ")
        if not answer.lower().startswith("y"):
            exit("Aborted.")
    title = re.findall(r"--- Day.* ---", download_day(year, day))[0]
    puzzle_path.parent.mkdir(parents=True, exist_ok=True)
    puzzle_path.write_text(TEMPLATE.format(title=title))
    print(f"New puzzle created at {puzzle_path}")


if __name__ == "__main__":
    args = docopt(__doc__)

    if args["<year>"]:
        year = int(args["<year>"])
        day = int(args["<day>"])
    else:
        today = date.today()
        year = today.year
        day = today.day

    if check_date(year, day):
        create_puzzle_file(year, day)
    else:
        print(f"There is no puzzle on day {day} of {year}")
