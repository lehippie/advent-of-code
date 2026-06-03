"""Advent of Code puzzle solver."""

import inspect
import json
from pathlib import Path
from time import time

from aoc import SOLUTIONS, load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of Code puzzles.
    In order to fetch inputs automatically, child classes must be created in
    files having the puzzle day number as names, themselves placed in
    directories with years as names.

    Attributes defined:
        input: Store the puzzle input lines as a list of strings.

    Methods:
        parser: Called at init to manipulate the puzzle input.
        part_one, part_two: Placeholders for solving parts of the puzzle.
        solve: Run puzzle parts and compare their returned values to already
            found solutions to prevent regressions.
    """

    def __init__(self, test_input: str = "") -> None:
        """Puzzle class constructor.

        Arguments:
            test_input: String to use in place of the real input.
        """
        if test_input == "":
            module = inspect.getmodule(self)
            if module is not None and module.__file__ is not None:
                puzzle = Path(module.__file__)
            else:
                raise ModuleNotFoundError("Can't find puzzle day file.")
            self.year, self.day = int(puzzle.parts[-2]), int(puzzle.stem)
            self.input = load_input(self.year, self.day)
        else:
            self.input = test_input.splitlines()
        self.parser()

    def parser(self) -> None:
        pass

    def part_one(self) -> int | str:
        """Placeholder for solving part one. Child method should
        return an int or a string to be compatible with json.
        """
        return NotImplemented

    def part_two(self) -> int | str:
        """Placeholder for solving part two. Child method should
        return an int or a string to be compatible with json.
        """
        return NotImplemented

    def solve(self) -> None:
        """Run puzzle parts and give answer or warn for regressions.

        Already found solutions must be stored in the `solutions.json` file
        located at the root of the repository with the following format:

        {
          "<year>": {
            "<completed_day>": [<part1_solution>, <part2_solution>],
            "<partially_completed_day>": [<part1_solution>, null],
            ...
            "<one_part_day>": [<part_solution>]
          }
        }
        """
        with open(SOLUTIONS) as f:
            try:
                solutions = json.load(f)[str(self.year)][str(self.day)]
            except KeyError:
                solutions = [None, None]

        for k, (part, solution) in enumerate(
            zip((self.part_one, self.part_two), solutions)
        ):
            start = time()
            answer = part()
            duration = time() - start

            if duration < 1:
                duration = f"{round(1000 * duration, 3)} ms"
            elif 1 < duration < 60:
                duration = f"{round(duration, 3)} s"
            else:
                m, s = divmod(int(duration), 60)
                duration = f"{m} min {s} s"

            if solution is None:
                print(f"Part {k + 1}: {answer} ({duration})")
                return
            if answer != solution:
                print(
                    f"Regression in part {k + 1}:",
                    f"{answer} instead of {solution} ({duration})",
                )
                return
            print(f"Part {k + 1} solved ({duration})")
        print(r"Day solved \o/")
