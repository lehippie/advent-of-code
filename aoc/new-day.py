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


if __name__ == "__main__":
    # test = Today(test_input="""parse_lines_here""")
    # r1 = test.part_one()
    # assert r1 == expected_result, r1
    # r2 = test.part_two()
    # assert r2 == expected_result, r2

    Today().solve()
'''


def check_date(puzzle: date) -> bool:
    """Verify if a puzzle exists on given date.

    Arguments:
        puzzle: `datetime.date` of the puzzle.

    Returns:
        True if a puzzle is available on given date, False otherwise.
    """
    if 2015 <= puzzle.year <= 2024 and puzzle.day <= 25:
        return True
    if puzzle.year == 2025 and puzzle.day <= 12:
        return True
    return False


def create_puzzle_file(year: int, day: int) -> None:
    """Create a template file to solve <puzzle> day.

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
    args = docopt(__doc__)

    if args["<year>"]:
        puzzle = date(int(args["<year>"]), 12, int(args["<day>"]))
    else:
        puzzle = date.today()

    if check_date(puzzle):
        create_puzzle_file(puzzle.year, puzzle.day)
    else:
        print(f"There is no puzzle on day {puzzle.day} of {puzzle.year}")
