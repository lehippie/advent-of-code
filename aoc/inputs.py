"""Puzzle inputs management."""

import inspect
from pathlib import Path
from urllib.request import Request, urlopen

from aoc import root, config

INPUTS_DIR = root / "inputs"
AOC_URL = "https://adventofcode.com"


def read_file(filepath):
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    if len(content) == 1:
        return content[0]
    return content


def download_input(year, day):
    request = Request(
        url=f"{AOC_URL}/{year}/day/{int(day)}/input",
        headers={"cookie": f"session={config['www']['session']}"},
    )
    with urlopen(request) as response:
        puzzle_input = response.read().decode("utf-8")
    return puzzle_input


def load_input():
    script = Path(inspect.stack()[-1].filename)
    year = script.parts[-2]
    day = script.stem
    input_path = INPUTS_DIR / year / (day + ".txt")
    if not input_path.exists():
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(download_input(year, day))
        print(f"Input for puzzle {year}/{day} saved.")
    return read_file(input_path)
