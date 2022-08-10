#!/usr/bin/env python

"""Compute time of solved puzzles.

Usage:
    {name} [(<year> <day>)]
    {name} all [--erase]
    {name} --help

Arguments:
    <year>, <day>       Date of the new day (default: today).
    all                 Compute timing for all puzzles and save
                        them in a file.

Options:
    -e, --erase         With argument <all>, erase previously
                        calculated timings.
    -h, --help          Show this help.
"""

import json
import re
from datetime import datetime
from importlib import import_module
from pathlib import Path
from timeit import Timer

from docopt import docopt

from aoc import ROOT


TIMING_FILE = ROOT / "timings.json"


def timing(year, day, verbose=True):
    day = f"{day:>02}"
    module = import_module(f"{year}.{day}")
    puzzle = module.Today(solutions=module.solutions)
    out = [None, None]
    for k, part in enumerate((puzzle.part_one, puzzle.part_two)):
        if puzzle.solutions[k]:
            timer = Timer(part)
            loops, seconds = timer.autorange()
            out[k] = round(1000 * seconds / loops, 3)
            if verbose:
                print(f"Part {k+1}: {out[k]} ms")
        elif verbose:
            print(f"Part {k+1}: unsolved")
    return out


def read_timing_file(filepath=TIMING_FILE):
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_timing_file(timings, filepath=TIMING_FILE):
    s = json.dumps(timings, indent=2)
    s = re.sub(r"\[\n\s+([0-9.]+),\n\s+([0-9.]+)\n\s+\]", r"[\1, \2]", s)
    with open(filepath, "w") as f:
        f.write(s)


def time_them_all(erase="False"):
    times = read_timing_file()
    for year in sorted(ROOT.glob("20*")):
        y = year.name
        print(y)
        if y not in times:
            times[y] = {}
        for day in sorted(year.glob("*.py")):
            d = day.stem
            if erase or d not in times[y]:
                try:
                    times[y][d] = timing(y, d, verbose=False)
                except:
                    continue
            print(f"  {d}: {times[y][d][0]:>8.3f} ms |{times[y][d][1]:>8.3f} ms")
    write_timing_file(times)


if __name__ == "__main__":
    args = docopt(__doc__.format(name=Path(__file__).name))

    if args["all"]:
        time_them_all(erase=args["--erase"])
    else:
        if args["<year>"] is None:
            now = datetime.now()
            args["<year>"] = str(now.year)
            args["<day>"] = now.day

        puzzle_path = ROOT / args["<year>"] / f"{args['<day>']:>02}.py"
        if puzzle_path.exists():
            timing(args["<year>"], args["<day>"])
        else:
            print(f"Puzzle not found: {puzzle_path}")
