#!/usr/bin/env python

"""Computation time of solved puzzles."""

import json
from importlib import import_module
from pathlib import Path
from timeit import repeat

from aoc import ROOT


REPEATS = 10
TIMING_FILE = Path(__file__).parent / "timings.json"


def read_timing_file(filepath=TIMING_FILE):
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_timeing_file(timings, filepath=TIMING_FILE):
    with open(filepath, "w") as f:
        json.dump(timings, f, indent=4)


def timing(year, day, repeats=REPEATS):
    m = import_module(f"{year}.{day:>02}")
    p = m.__dict__[f"Puzzle{day:>02}"]()
    out = [None, None]
    for k, part in enumerate((p.part_one, p.part_two)):
        out[k] = repeat(part, repeat=repeats, number=1)
        out[k] = round(1000 * min(out[k]), 3)
    return out


def main():
    timings = read_timing_file()
    for year in sorted(ROOT.glob("20*")):
        if year.name not in timings:
            timings[year.name] = {}
        for day in sorted(year.glob("*.py")):
            if day.stem not in timings[year.name]:
                timings[year.name][day.stem] = timing(year.name, day.stem)
                print(
                    f"{year.name}.{day.stem} =",
                    f"{timings[year.name][day.stem][0]:>8.3f} ms |",
                    f"{timings[year.name][day.stem][1]:>8.3f} ms",
                )
    write_timeing_file(timings)


if __name__ == "__main__":
    main()
