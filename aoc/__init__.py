from configparser import ConfigParser
from pathlib import Path

root = Path(__file__).parent.parent
config = ConfigParser()
config.read(root / "config.txt")
