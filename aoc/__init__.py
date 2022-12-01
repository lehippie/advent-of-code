from configparser import ConfigParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONFIG = ConfigParser()
CONFIG.read(ROOT / "config.txt")
REQUEST_HEADER = {
    "User-Agent": "github.com/lehippie/advent-of-code by dahip@gmx.fr",
    "cookie": f"session={CONFIG['www']['session']}",
}
