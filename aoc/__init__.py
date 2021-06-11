from configparser import ConfigParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
CONFIG = ConfigParser()
CONFIG.read(ROOT / "config.txt")
