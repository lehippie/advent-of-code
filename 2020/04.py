"""Day 4: Passport Processing."""

import re
from aoc.puzzle import Puzzle


RULES = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": {"cm": (150, 193), "in": (59, 76)},
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": r"^[0-9]{9}$",
}


def check_height(height):
    unit = height[-2:]
    if unit in RULES["hgt"]:
        mini, maxi = RULES["hgt"][unit]
        return mini <= int(height[:-2]) <= maxi
    else:
        return False


def passport_validity(passport):
    if (
        set(RULES).issubset(set(passport))
        and RULES["byr"][0] <= int(passport["byr"]) <= RULES["byr"][1]
        and RULES["iyr"][0] <= int(passport["iyr"]) <= RULES["iyr"][1]
        and RULES["eyr"][0] <= int(passport["eyr"]) <= RULES["eyr"][1]
        and check_height(passport["hgt"])
        and re.match(RULES["hcl"], passport["hcl"])
        and passport["ecl"] in RULES["ecl"]
        and re.match(RULES["pid"], passport["pid"])
    ):
        return True
    return False


class Puzzle04(Puzzle):
    def parser(self):
        data = [{}]
        for line in self.input:
            if not line:
                data.append({})
                continue
            for field in line.split(" "):
                key, value = field.split(":")
                data[-1][key] = value
        return data

    def part_one(self):
        return sum(set(RULES).issubset(set(p)) for p in self.input)

    def part_two(self):
        return sum(passport_validity(p) for p in self.input)


if __name__ == "__main__":
    Puzzle04(solutions=(222, 140)).solve()
