from configparser import ConfigParser
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).parent.parent
CONFIG = ConfigParser()
CONFIG.read(ROOT / "config.txt")
REQUEST_HEADER = {
    "User-Agent": "github.com/lehippie/advent-of-code by dahip@gmx.fr",
    "cookie": f"session={CONFIG['www']['session']}",
}


def download(url):
    request = Request(url=url, headers=REQUEST_HEADER)
    with urlopen(request) as response:
        return response.read().decode("utf-8")


def download_day(year: int, day: int):
    return download(f"https://adventofcode.com/{year}/day/{day}")


def download_input(year: int, day: int):
    return download(f"https://adventofcode.com/{year}/day/{day}/input")
