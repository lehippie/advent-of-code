"""Advent of Code puzzle solver."""

from aoc.inputs import load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from, to solve Advent of Code
    puzzles.

    Methods:
        parser  --  placeholder for optional method to manipulate
            puzzle input at class init.
        part_one, part_two  --  placeholders for solutions of both
            parts of the puzzle.
        solve  --  run both parts and compare them to already found
            solutions.

    Attributes:
        solutions  --  stores puzzle solutions as a tuple.
        input  --  stores puzzle input as a list of strings or as a
            string if there is only one line.
    """

    def __init__(
        self,
        puzzle_input=None,
        solutions=(None, None),
    ):
        """Puzzle class constructor.

        Arguments:
            puzzle_input  --  str or list of str used to store puzzle
                inputs. If set to None, it is fetched from default
                inputs folder.
            solutions  --  already found solutions used by the "solve"
                method to prevent regression.
        """
        if puzzle_input is None:
            puzzle_input = load_input()
        self.input = puzzle_input
        self.input = self.parser()
        self.solutions = solutions

    def parser(self):
        return self.input

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def solve(self):
        """Run puzzle parts and print status."""
        parts = (self.part_one, self.part_two)
        for k, (part, solution) in enumerate(zip(parts, self.solutions)):
            answer = part()
            if solution is None:
                print(f"Part {k+1} answer: {answer} ?")
                return
            elif answer != solution:
                print(
                    f"Regression in part {k+1}:",
                    f"got {answer} instead of {solution}.",
                )
                return
        print("Day completed \o/")
