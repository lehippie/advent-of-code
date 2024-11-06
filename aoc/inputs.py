"""Puzzle inputs management."""

from aoc import ROOT, download_input

INPUTS_DIR = ROOT / "inputs"


def read_file(filepath: str) -> list | str:
    """Read file content.

    Arguments:
        filepath: Path to the file to read.

    Returns:
        List containing the lines of the file.
        If there is only one line, returns it as a string.
    """
    with open(filepath) as f:
        content = [line.rstrip("\n\r") for line in f]
    if len(content) == 1:
        return content[0]
    return content


def load_input(year: int, day: int) -> list | str:
    """Load input from `inputs` folder (download it if not saved yet).

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
    return read_file(input_path)
