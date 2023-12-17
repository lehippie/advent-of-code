"""Advent of Code puzzle solver."""

import inspect
import time
from pathlib import Path

from aoc.inputs import read_file, load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of Code
    puzzles.

    Attributes defined at init:
        input           Store the puzzle input as a list of strings
                        or as a string if it contains only one line.
        solutions       Solutions for both part.

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

    def __init__(
        self,
        infile=None,
        solutions=(None, None),
    ):
        """Puzzle class constructor.

        Arguments:
            infile      Name of the file containing input data. If set
                        to None, it is fetched from repo_root/inputs/
                        based on the path to where the instance is
                        created (ex: .../2020/01.py).
            solutions   Already found solutions used by <solve> method
                        to prevent regressions.
        """
        f = Path(inspect.getmodule(self).__file__)
        if infile is None:
            self.input = load_input(int(f.parts[-2]), int(f.stem))
        else:
            self.input = read_file(f.parent / infile)
        self.parser()
        self.solutions = solutions

    def parser(self):
        pass

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def solve(self, verbose=True):
        """Run puzzle parts and warn for regressions."""
        parts = (self.part_one, self.part_two)
        for k, (part, solution) in enumerate(zip(parts, self.solutions), 1):
            start = time.time()
            answer = part()
            duration = round(1000 * (time.time() - start), 3)
            if solution is None:
                if verbose:
                    print(f"Part {k} answer: {answer} ({duration} ms)")
                return False
            elif answer != solution:
                if verbose:
                    print(
                        f"Regression in part {k}:",
                        f"{answer} instead of {solution} ({duration} ms)",
                    )
                return False
            elif verbose:
                print(f"Part {k} solved ({duration} ms)")
        return True
