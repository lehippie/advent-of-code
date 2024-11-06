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

SOLUTIONS = ROOT / "solutions.json"
if not SOLUTIONS.exists():
    SOLUTIONS.write_text("{}")

TIMINGS = ROOT / "timings.json"
if not TIMINGS.exists():
    TIMINGS.write_text("{}")


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
    return download(f"https://adventofcode.com/{year}/day/{day}")


def download_input(year: int, day: int) -> str:
    """Download personnal puzzle input.
    
    Arguments:
        year, day: Date of the puzzle.
    
    Returns:
        Source of the input web page.
    """
    return download(f"https://adventofcode.com/{year}/day/{day}/input")
