"""Advent of Code puzzle solver."""

import inspect
from pathlib import Path
from aoc.inputs import load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of Code
    puzzles.

    Methods:
        parser  --  method called at instance init to manipulate the
            puzzle input stored in <input> attribute. Returned object
            is stored in  <input> attribute.
        part_one, part_two  --  placeholders for solving parts of the
            puzzle. Solutions have to be returned for <solve> method
            to do its verification job.
        solve  --  run puzzle parts and compare answers to already
            found solutions.

    Attributes defined at init:
        input  --  stores puzzle input as a list of strings or as a
            string if there is only one line.
        solutions  --  stores puzzle solutions as a tuple.
    """

    def __init__(
        self,
        input_data=None,
        solutions=(None, None),
    ):
        """Puzzle class constructor.

        Arguments:
            input_data  --  list of str OR str.
                If set to None, tries to fetch it from default inputs
                folder based on the name of the file where the
                instance is created (ex: "2020/01.py").
            solutions  --  already found solutions used by <solve>
                method to prevent regressions.
        """
        if input_data is None:
            f = Path(inspect.getmodule(self).__file__)
            input_data = load_input(f.parts[-2], f.stem)
        self.input = input_data
        self.input = self.parser()
        self.solutions = solutions

    def parser(self):
        return self.input

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
