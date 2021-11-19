"""Puzzle inputs management.

Inputs are saved in a single folder defined here.
"""

import inspect
from pathlib import Path
from urllib.request import Request, urlopen

from aoc import ROOT, CONFIG


def read_file(filepath):
    """Read file content.

    Arguments:
        filepath  --  str OR Path object.

    Returns:
        List of string, one for each line in the file.
            OR
        String if the file contains only one line.
    """
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    if len(content) == 1:
        return content[0]
    return content


def download_input(year: int, day: int) -> str:
    """Get puzzle input from advent of code website.

    Arguments:
        year, day  --  integers representing the date of the puzzle
            that needs to be downloaded.

    Returns:
        String containing the response from the website.

    Authentification is done with the session cookie parsed from
    configuration file.
    """
    request = Request(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"cookie": f"session={CONFIG['www']['session']}"},
    )
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def load_input(year: int = None, day: int = None):
    """Get puzzle input from inputs folder for given date.

    Arguments:
        year, day  --  integers representing the date of the puzzle
            to load.

    If <year> or <day> is missing, tries to infer them from the path
    of the calling script.
    If the file is not already in the inputs folder, it will be saved
    for future use.
    """
    if None in (year, day):
        script = Path(inspect.stack()[-1].filename)
        try:
            year = int(script.parts[-2])
            day = int(script.stem)
        except ValueError:
            print(f"Cannot infer puzzle date from puzzle path '{script}'")
            raise
    input_path = ROOT / "inputs" / f"{year}" / f"{day:02}.txt"
    if not input_path.exists():
        puzzle_input = download_input(year, day)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(puzzle_input)
        print(f"Input saved in {input_path}.")
    return read_file(input_path)
