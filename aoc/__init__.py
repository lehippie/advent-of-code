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
    """Download an url source code."""
    request = Request(url=url, headers=REQUEST_HEADER)
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def download_day(year: int, day: int) -> str:
    """Download the instructions of given day."""
    return download(f"https://adventofcode.com/{year}/day/{day}")


def download_input(year: int, day: int) -> str:
    """Download your personnal input of given day."""
    return download(f"https://adventofcode.com/{year}/day/{day}/input")
