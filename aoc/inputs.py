"""Puzzle inputs management."""

from urllib.request import Request, urlopen

from aoc import ROOT, REQUEST_HEADER


INPUTS_DIR = ROOT / "inputs"


def read_file(filepath):
    """Read file content.

    Arguments:
        filepath        String OR Path object.

    Returns:
        List of string, one for each line in the file.
            OR
        String if the file contains only one line.
    """
    with open(filepath) as f:
        content = [line.rstrip("\n\r") for line in f]
    if len(content) == 1:
        return content[0]
    return content


def download_input(year, day):
    """Get puzzle input from Advent of Code website.

    Authentification is done with the session cookie parsed from
    configuration file (see "config.txt.example").

    Arguments:
        year, day       Date of the puzzle to download.

    Returns:
        String containing the response from the website.
    """
    request = Request(
        url=f"https://adventofcode.com/{year}/day/{int(day)}/input",
        headers=REQUEST_HEADER,
    )
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def load_input(year, day):
    """Get puzzle input from inputs folder (download it if absent).

    Arguments:
        year, day       Date of the puzzle to load.

    Returns:
        List of string, one for each line in the puzzle input.
            OR
        String if the puzzle input is only one line.
    """
    input_path = INPUTS_DIR / f"{year}" / f"{day.zfill(2)}.txt"
    if not input_path.exists():
        puzzle_input = download_input(year, day)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(puzzle_input)
        print(f"Input saved in {input_path}")
    return read_file(input_path)
