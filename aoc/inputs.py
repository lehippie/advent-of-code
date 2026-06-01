"""Puzzle inputs (down)loader."""

from aoc import ROOT, download_input

INPUTS_DIR = ROOT / "inputs"


def load_input(year: int, day: int) -> list | str:
    """Load input from dedicated folder. If not found, download and save it.

    Arguments:
        year, day: Date of the puzzle.

    Returns:
        List containing the lines of the puzzle input.
        If there is only one line, returns it as a string.
    """
    input_path = INPUTS_DIR / f"{year}-{day:>02}.txt"

    if not input_path.exists():
        puzzle_input = download_input(year, day)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(puzzle_input)
        print(f"Input saved in {input_path}")

    with open(input_path) as f:
        content = [line.rstrip("\n\r") for line in f]
    if len(content) == 1:
        return content[0]
    return content
