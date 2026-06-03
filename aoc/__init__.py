from configparser import ConfigParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).parents[1]
CONFIG = ConfigParser()
CONFIG.read(ROOT / "config.txt")
REQUEST_HEADER = {
    "cookie": f"session={CONFIG['www']['session']}",
    "User-Agent": CONFIG["www"]["user-agent"],
}

INPUTS_DIR = ROOT / "inputs"
SOLUTIONS = ROOT / "solutions.json"
if not SOLUTIONS.exists():
    SOLUTIONS.write_text("{}")


def puzzle_dates() -> set[tuple[int, int]]:
    """Return a set of valid (year, day) puzzles."""
    dates = set()
    for year in range(2015, 2025):
        dates.update([(year, day) for day in range(1, 26)])
    dates.update([(2025, day) for day in range(1, 13)])
    return dates


def check_date(year: int, day: int) -> bool:
    """Verify if a puzzle exists on given date.

    Arguments:
        year, day: Date of the puzzle.

    Returns:
        True if a puzzle is available on given date, False otherwise.
    """
    return (year, day) in puzzle_dates()


def download(url: str) -> str:
    """Download url's source code.

    Arguments:
        url: Web page to download.

    Returns:
        Source of the web page.
    """
    request = Request(url=url, headers=REQUEST_HEADER)
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def download_day(year: int, day: int) -> str:
    """Download puzzle instructions.

    Arguments:
        year, day: Date of the puzzle.

    Returns:
        Source of the puzzle instructions web page.
    """
    if check_date(year, day):
        return download(f"https://adventofcode.com/{year}/day/{day}")
    else:
        raise IOError(f"There is no puzzle on day {day} of {year}")


def download_input(year: int, day: int) -> str:
    """Download personnal puzzle input.

    Arguments:
        year, day: Date of the puzzle.

    Returns:
        Source of the input web page.
    """
    if check_date(year, day):
        return download(f"https://adventofcode.com/{year}/day/{day}/input")
    else:
        raise IOError(f"There is no puzzle on day {day} of {year}")


def load_input(year: int, day: int) -> list[str]:
    """Load input from dedicated folder. If not found, download and save it.

    Arguments:
        year, day: Date of the puzzle.

    Returns:
        List of the lines of the puzzle input.
    """
    input_path = INPUTS_DIR / f"{year}-{day:>02}.txt"

    if not input_path.exists():
        puzzle_input = download_input(year, day)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_text(puzzle_input)
        print(f"Input saved in {input_path}")

    with open(input_path) as f:
        content = [line.rstrip("\n\r") for line in f]
    return content
