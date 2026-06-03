#!/usr/bin/env python

"""Compute puzzle solving durations of each puzzle part which have a
solution but no known timing, and update README.md's table.

To update old puzzle timings, delete the corresponding lines in
timings.json before running.
To recalculate everything, delete timings.json and run again.
"""

import json
import re
import sys
from datetime import date
from importlib import import_module
from time import time

from aoc import ROOT, SOLUTIONS, puzzle_dates

TIMINGS = ROOT / "timings.json"
if not TIMINGS.exists():
    TIMINGS.write_text("{}")


def puzzle_timing(year: str, day: str, solutions: list) -> list[float | None]:
    """Calculate the timing of a puzzle.

    Arguments:
        year, day: Date of the puzzle.
        solutions: Solutions for that day.

    Returns:
        Time to process parts of the puzzle in milliseconds.
        Without solution, part timing is set to None.
    """
    puzzle = import_module(f"{year}.{day:>02}").Today()
    timing = []
    for part, solution in zip((puzzle.part_one, puzzle.part_two), solutions):
        start = time()
        answer = part()
        part_duration = round(1000 * (time() - start), 3)
        timing.append(part_duration if answer == solution else None)
    return timing


def calculate_timings() -> dict[str, dict[str, list[float | None]]]:
    """Calculate the timings of all solved puzzle.

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
            if all(d is None for d in day_solutions):
                continue
            if day not in timings[year]:
                timings[year][day] = [None for _ in day_solutions]
            if any(s and not t for s, t in zip(day_solutions, timings[year][day])):
                timings[year][day] = puzzle_timing(year, day, day_solutions)
                print(f"{year}-{day}: {timings[year][day]} ms")

    return timings


def write_timing_file(timings: dict[str, dict[str, list[float | None]]]):
    """Write the timings in a json file.

    Arguments:
        timings: Timings dict with format {<year>: {<day>: [t1, t2]}}.
    """
    timings = {y: {f"{k:>02}": v for k, v in d.items()} for y, d in timings.items()}
    s = json.dumps(timings, indent=2, sort_keys=True)
    # Remove leading zeros for one-digit days (needed before for sorting)
    s = re.sub(r'"0', '"', s)
    # Remove indents inside days
    s = re.sub(r"\[\n\s{6}", "[", s)
    s = re.sub(r",\n\s{6}", ", ", s)
    s = re.sub(r"\n\s{4}\]", "]", s)
    with open(TIMINGS, "w") as f:
        f.write(s)


def get_emoji(timing: float | None) -> str:
    """Define emojis for timings representation in `README.md`.

    Arguments:
        timing: puzzle solving duration in milliseconds.

    Returns:
        Emoji corresponding to input timing.
    """
    if timing is None:
        return ":x:"
    if timing < 5:
        return ":zap:"
    if timing < 1000:
        return ":green_square:"
    if timing < 5000:
        return ":blue_square:"
    if timing < 30000:
        return ":orange_square:"
    if timing < 60000:
        return ":red_square:"
    return ":skull:"


def update_readme(timings: dict) -> None:
    """Integrate the timings table in `README.md`.

    Arguments:
        timings: Dict of timings.
    """
    header = (
        "# advent-of-code\n\nAdvent of Code solutions in python 3\n\n"
        ":zap: < 5 ms < :green_square: < 1 s < :blue_square: < 5 s < "
        ":orange_square: < 30 s < :red_square: < 1 min < :skull:"
        "&emsp;&emsp;:x: = Unsolved\n\n"
    )
    footer = (
        f"\n\n_(last update: {date.today().isoformat()} - "
        "computed on an Intel i5 13600K)_\n"
    )
    dates = puzzle_dates()
    years = sorted(set(y for y, _ in dates))
    table = ["||" + "|".join(map(str, years)) + "|"]
    table.append("|:---:|" + "".join(":---:|" for _ in years))
    for day in range(1, max(d for _, d in dates) + 1):
        table.append(f"|{day}|")
        for year in years:
            if (year, day) not in dates:
                table[-1] += "|"
                continue
            try:
                times = timings[f"{year}"][f"{day}"]
                if any(t is not None for t in times):
                    table[-1] += "".join(get_emoji(t) for t in times) + "|"
                else:
                    table[-1] += ":x:|"
            except KeyError:
                table[-1] += ":x:|"

    readme = ROOT / "README.md"
    readme.write_text(header + "\n".join(table) + footer)


if __name__ == "__main__":
    sys.path.append(".")  # Allow puzzle imports
    sys.path.append("./2019")  # Allow 2019 puzzles to import their Intcode computer
    timings = calculate_timings()
    write_timing_file(timings)
    update_readme(timings)
