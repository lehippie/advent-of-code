"""Advent of Code puzzle solver."""

import inspect
import json
from pathlib import Path
from time import process_time

from aoc import SOLUTIONS
from aoc.inputs import load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of Code puzzles.

    Attributes defined:
        input: Store the puzzle input as a list of strings (one per line) or
            as a string (one line inputs).

    Methods:
        parser: Called at init to manipulate the puzzle input.
        part_one, part_two: Placeholders for solving parts of the puzzle.
        solve: Run puzzle parts and compare their returned values to already
            found solutions to prevent regressions.
    """

    def __init__(self, test_input: str = None):
        """Puzzle class constructor.

        Arguments:
            test_input: String to use in place of the real input.
        """
        if test_input is None:
            puzzle = Path(inspect.getmodule(self).__file__)
            self.year, self.day = int(puzzle.parts[-2]), int(puzzle.stem)
            self.input = load_input(self.year, self.day)
        else:
            self.input = test_input.splitlines()
            if len(self.input) == 1:
                self.input = self.input[0]
        self.parser()

    def parser(self):
        pass

    def part_one(self):
        return NotImplemented

    def part_two(self):
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
            "one_part_day": [part_solution]
          }
        }
        """
        with open(SOLUTIONS) as f:
            try:
                solutions = json.load(f)[f"{self.year}"][f"{self.day}"]
            except KeyError:
                solutions = [None, None]

        for k, (part, solution) in enumerate(
            zip((self.part_one, self.part_two), solutions)
        ):
            start = process_time()
            answer = part()
            duration = process_time() - start

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
        print("Day solved \o/")
