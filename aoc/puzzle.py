"""Advent of Code puzzle solver."""

import inspect
from pathlib import Path
from aoc.inputs import load_input


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
        input_data=None,
        solutions=(None, None),
    ):
        """Puzzle class constructor.

        Arguments:
            input_data      List of strings OR string. If set to None,
                            it is fetched from "inputs" folder based
                            on the path to where the instance is
                            created (ex: /.../2020/01.py).
            solutions       Already found solutions used by <solve>
                            classmethod to prevent regressions.
        """
        if input_data is None:
            f = Path(inspect.getmodule(self).__file__)
            input_data = load_input(f.parts[-2], f.stem)
        self.input = input_data
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
        for k, (part, solution) in enumerate(zip(parts, self.solutions)):
            answer = part()
            if solution is None:
                if verbose:
                    print(f"Part {k + 1} answer: {answer} ?")
                return False
            elif answer != solution:
                if verbose:
                    print(
                        f"Regression in part {k + 1}:",
                        f"got {answer} instead of {solution}.",
                    )
                return False
        if verbose:
            print("Day completed \o/")
        return True
