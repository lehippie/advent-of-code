#!/usr/bin/env python

"""Compute the time to solve puzzles.

This script analyze the solutions.json and timings.json files and
add to the latter the solved puzzles not yet timed.

Usage:
    {name} [--erase]
    {name} --help

Options:
    -e, --erase         Recalculate previous timings.
    -h, --help          Show this help.
"""

import json
import re
import sys
from importlib import import_module
from pathlib import Path
from timeit import timeit

from docopt import docopt

from aoc import SOLUTIONS, TIMINGS


def write_timing_file(timings: dict):
    """Write the timings in a json file.

    Arguments:
        timings: Timings dict with format {<year>: {<day>: [t1, t2]}}.
    """
    s = json.dumps(timings, indent=2)
    s = re.sub(r"\[\n\s{6}", "[", s)
    s = re.sub(r",\n\s{6}", ", ", s)
    s = re.sub(r"\n\s{4}\]", "]", s)
    with open(TIMINGS, "w") as f:
        f.write(s)


def get_time(year, day, solutions):
    """Calculate the timing of a puzzle."""
    day = f"{day:>02}"
    puzzle = import_module(f"{year}.{day}").Today()
    return [
        round(1000 * timeit(part, number=1), 3)
        for part in zip([puzzle.part_one, puzzle.part_two], solutions)
    ]


def get_all_times(erase=False):
    """Calculate the timing of all fully solved puzzle."""
    with open(SOLUTIONS) as f:
        solutions = json.load(f)
    with open(TIMINGS) as f:
        timings = json.load(f)

    for year, year_solutions in solutions.items():
        print(year)
        if year not in timings:
            timings[year] = {}

        for day, day_solutions in year_solutions.items():
            if day not in timings[year]:
                timings[year][day] = []
            if None in day_solutions:
                print(f"{day} skipped (incomplete)")
                continue
            if not timings[year][day] or erase:
                timings[year][day] = get_time(year, day, day_solutions)
                print(f"{day}: {timings[year][day]} ms")

    return timings


if __name__ == "__main__":
    args = docopt(__doc__.format(name=Path(__file__).name))
    sys.path.append("./2019")  # To allow local import of intcode computer
    times = get_all_times(args["--erase"])
    write_timing_file(times)
