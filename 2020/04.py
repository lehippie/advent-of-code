"""Day 4: Passport Processing."""

import re
from aoc.puzzle import Puzzle


RULES = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": {"cm": (150, 193), "in": (59, 76)},
    "hcl": re.compile(r"^#[0-9a-f]{6}$"),
    "ecl": ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": re.compile(r"^[0-9]{9}$"),
}


def passport_validity(p):
    return bool(
        set(RULES).issubset(p)
        and RULES["byr"][0] <= int(p["byr"]) <= RULES["byr"][1]
        and RULES["iyr"][0] <= int(p["iyr"]) <= RULES["iyr"][1]
        and RULES["eyr"][0] <= int(p["eyr"]) <= RULES["eyr"][1]
        and p["hgt"][-2:] in RULES["hgt"]
        and (
            RULES["hgt"][p["hgt"][-2:]][0]
            <= int(p["hgt"][:-2])
            <= RULES["hgt"][p["hgt"][-2:]][1]
        )
        and RULES["hcl"].match(p["hcl"])
        and p["ecl"] in RULES["ecl"]
        and RULES["pid"].match(p["pid"])
    )


class Today(Puzzle):
    def parser(self):
        self.passports = [{}]
        for line in self.input:
            if not line:
                self.passports.append({})
                continue
            for field in line.split(" "):
                key, value = field.split(":")
                self.passports[-1][key] = value

    def part_one(self):
        return sum(set(RULES).issubset(p) for p in self.passports)

    def part_two(self):
        return sum(passport_validity(p) for p in self.passports)


if __name__ == "__main__":
    Today().solve()
