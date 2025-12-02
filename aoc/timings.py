#!/usr/bin/env python

"""Compute the time to solve puzzles.

Analysis of `solutions.json` and `timings.json` files to time newly
solved puzzle parts and add them to `README.md`'s table.

Usage:
    {name} [(<year> <day>)] [--erase]
    {name} --help

Arguments:
    <year>, <day>       Date of the puzzle to create.
                        Default: all puzzle without timing.

Options:
    -e, --erase         Recalculate previous timings.
    -h, --help          Show this help.
"""

import json
import re
import sys
from datetime import date
from importlib import import_module
from pathlib import Path
from time import time

from docopt import docopt

from aoc import ROOT, SOLUTIONS, TIMINGS


def puzzle_timing(year: int | str, day: int | str, solutions: list) -> list[float]:
    """Calculate the timing of a puzzle.

    Arguments:
        year, day: Date of the puzzle.
        solutions: Solutions for that day.

    Returns:
        Time to process parts of the puzzle. Without solution, parts' timing
        is set to None.
    """
    puzzle = import_module(f"{year}.{day:>02}").Today()
    timing = []
    for part, solution in zip((puzzle.part_one, puzzle.part_two), solutions):
        start = time()
        answer = part()
        part_duration = round(1000 * (time() - start), 3)
        timing.append(part_duration if answer == solution else None)
    return timing


def get_timings(erase: bool = False) -> dict:
    """Calculate the timings of all solved puzzle.

    Arguments:
        erase: If True, previous known timings are recalculated.

    Returns:
        Dict of timings with same structure as `solutions.json`.
    """
    with open(SOLUTIONS) as f:
        solutions = json.load(f)
    with open(TIMINGS) as f:
        timings = json.load(f)

    for year, year_solutions in solutions.items():
        if year not in timings:
            timings[year] = {}

        for day, day_solutions in year_solutions.items():
            if day not in timings[year]:
                timings[year][day] = [None for _ in day_solutions]
            if not any(d is not None for d in day_solutions):
                continue
            if erase or any(
                s and not t for s, t in zip(day_solutions, timings[year][day])
            ):
                timings[year][day] = puzzle_timing(year, day, day_solutions)
                print(f"{year}-{day}: {timings[year][day]} ms")

    return timings


def write_timing_file(timings: dict):
    """Write the timings in a json file.

    Arguments:
        timings: Timings dict with format {<year>: {<day>: [t1, t2]}}.
    """
    timings = {y: {f"{k:>02}": v for k, v in d.items()} for y, d in timings.items()}
    s = json.dumps(timings, indent=2, sort_keys=True)
    s = re.sub(r'"0', '"', s)
    s = re.sub(r"\[\n\s{6}", "[", s)
    s = re.sub(r",\n\s{6}", ", ", s)
    s = re.sub(r"\n\s{4}\]", "]", s)
    with open(TIMINGS, "w") as f:
        f.write(s)


def get_emoji(timing: float) -> str:
    """Define emojis for timings representation in `README.md`.

    Arguments:
        timing: time to solve a puzzle part.

    Returns:
        Emoji corresponding to given solving time interval.
    """
    if timing is None:
        return ":x:"
    if timing < 1:
        return ":zap:"
    if timing < 1000:
        return ":green_square:"
    if timing < 5000:
        return ":blue_square:"
    if timing < 60000:
        return ":orange_square:"
    if timing < 300000:
        return ":red_square:"
    return ":skull:"


def update_readme(timings: dict) -> None:
    """Integrate the timings table in `README.md`.

    Arguments:
        timings: Dict of timings.
    """
    header = (
        "# advent-of-code\n\nAdvent of Code solutions in python 3\n\n"
        ":zap: < 1 ms&emsp;:green_square: < 1 s&emsp;:blue_square: < 5 s&emsp;"
        ":orange_square: < 1 min&emsp;:red_square: < 5 min&emsp;:skull: > 5 min&emsp;"
        ":x: unsolved\n\n"
    )
    footer = (
        f"\n\n_(last update: {date.today().isoformat()} - "
        "computed on an Intel i5 13600K)_\n"
    )
    years = sorted(timings)
    table = ["||" + "|".join(years) + "|"]
    table.append("|:---:|" + "".join(":---:|" for _ in years))
    for day in range(1, 26):
        table.append(f"|{day}|")
        for year in years:
            try:
                times = timings[year][f"{day}"]
                if any(t is not None for t in times):
                    table[-1] += "".join(get_emoji(t) for t in times) + "|"
                else:
                    table[-1] += ":x:|"
            except KeyError:
                pass

    readme = ROOT / "README.md"
    readme.write_text(header + "\n".join(table) + footer)


if __name__ == "__main__":
    args = docopt(__doc__.format(name=Path(__file__).name))
    sys.path.append(".")  # Allow puzzle imports
    sys.path.append("./2019")  # Allow local import of intcode computer
    timings = get_timings(args["--erase"])
    write_timing_file(timings)
    update_readme(timings)
