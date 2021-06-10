"""Advent of Code puzzle solver."""

from aoc.inputs import load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from, to solve Advent of Code
    puzzles.

    Methods:
        part_one, part_two -- placeholders to be surcharged in child
            classes.
        solve -- run both parts and compare them to already found
            solutions.
    """

    def __init__(
        self,
        puzzle_input=None,
        parser=None,
        parse_lines=True,
        solutions=(None, None),
    ):
        """Puzzle class constructor.

        Arguments:
            puzzle_input -- str or list of str used to store puzzle
                inputs. If set to None, it is fetched from default
                inputs folder.
            parser -- optionnal callable to be applied to each line of
                the puzzle input. Default is to do nothing.
            parse_lines -- flag applying the <parser> to each line
                instead of the entire input. Default is True.
            solutions -- already found solutions, used by the "solve"
                method to check for regression.
        """
        if puzzle_input is None:
            puzzle_input = load_input()
        if parser is not None:
            if parse_lines:
                puzzle_input = [parser(line) for line in puzzle_input]
            else:
                puzzle_input = parser(puzzle_input)
        self.input = puzzle_input
        self.solutions = solutions

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
