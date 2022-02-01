#!/usr/bin/env python

"""Computation time of solved puzzles."""

import json
from importlib import import_module
from timeit import repeat

from aoc import ROOT


REPEATS = 10
TIMING_FILE = ROOT / "timings.json"


def read_timing_file(filepath=TIMING_FILE):
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_timing_file(timings, filepath=TIMING_FILE):
    with open(filepath, "w") as f:
        json.dump(timings, f, indent=2)


def timing(year, day, repeats=REPEATS):
    day = f"{day:>02}"
    module = import_module(f"{year}.{day}")
    puzzle = module.Today(solutions=module.solutions)
    if puzzle.solve(verbose=False):
        out = [None, None]
        for k, part in enumerate((puzzle.part_one, puzzle.part_two)):
            out[k] = repeat(part, repeat=repeats, number=1)
            out[k] = round(1000 * min(out[k]), 3)
        return out
    else:
        raise IOError(f"Unsolved puzzle: {year}.{day}")


def main():
    timings = read_timing_file()
    for year in sorted(ROOT.glob("20*")):
        if year.name not in timings:
            timings[year.name] = {}
        for day in sorted(year.glob("*.py")):
            if day.stem not in timings[year.name]:
                try:
                    timings[year.name][day.stem] = timing(year.name, day.stem)
                except:
                    continue
                print(
                    f"{year.name}.{day.stem} =",
                    f"{timings[year.name][day.stem][0]:>8.3f} ms |",
                    f"{timings[year.name][day.stem][1]:>8.3f} ms",
                )
    write_timing_file(timings)


if __name__ == "__main__":
    main()
