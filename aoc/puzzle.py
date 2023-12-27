"""Advent of Code puzzle solver."""

import inspect
import json
import time
from pathlib import Path

from aoc import ROOT
from aoc.inputs import load_input, read_file

SOLUTIONS_FILE = ROOT / "solutions.json"


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of Code
    puzzles.

    Attributes defined at init:
        input           Store the puzzle input as a list of strings
                        or as a string if it contains only one line.

    Methods:
        parser          Method called at instance init to manipulate
                        the puzzle input.
        part_one, part_two
                        Placeholders for solving both parts of the
                        puzzle.
        solve           Run puzzle parts and compare their returned
                        values to already found solutions to prevent
                        regressions.
    """

    def __init__(self, test_input: str = ""):
        """Puzzle class constructor.

        Arguments:
            test_input  File containing the test input to be used in
                        place of the one in `inputs` folder.
        """
        puzzle = Path(inspect.getmodule(self).__file__)
        self.year, self.day = int(puzzle.parts[-2]), int(puzzle.stem)
        if test_input:
            self.input = read_file(puzzle.parent / test_input)
        else:
            self.input = load_input(self.year, self.day)
        self.parser()

    def parser(self):
        pass

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def solve(self, solutions: list = []) -> None:
        """Run puzzle parts and give answer or warn for regressions."""
        parts = (self.part_one, self.part_two)
        if not solutions:
            with open(SOLUTIONS_FILE) as f:
                solutions = json.load(f)[f"{self.year}"][f"{self.day}"]

        for k, (part, solution) in enumerate(zip(parts, solutions), 1):
            start = time.time()
            answer = part()
            duration = round(1000 * (time.time() - start), 3)
            if solution is None:
                print(f"Part {k}: {answer} ({duration} ms)")
                return
            if answer != solution:
                print(
                    f"Regression in part {k}:",
                    f"{answer} instead of {solution} ({duration} ms)",
                )
                return
            print(f"Part {k} solved ({duration} ms)")
        print("Day solved \o/")
