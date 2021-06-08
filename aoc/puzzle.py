"""Base puzzle class."""

from aoc.inputs import load_input


class Puzzle:
    """Puzzle class.

    This class is made to be inherited from to solve Advent of
    Code puzzles.

    Methods:
        part_one, part_two -- placeholders to be surcharged in
            child classes.
        parse_input -- apply callable defined by <parser> argument
            to each element of the input.
        tests -- perform tests for both parts.
        solve -- print answers for both parts and compare them to
            previously found solutions.

    Attributes:
        input -- str or list of str used to store tests or puzzle
            inputs.
    """

    def __init__(
        self,
        parser=lambda x: x,
        tests={"part_one": [], "part_two": []},
        solution_one=None,
        solution_two=None,
    ):
        """Puzzle class constructor.

        Arguments:
            parser -- callable to be applied to each element of the
                puzzle input. Default is to do nothing.
            tests -- dictionnary containing tests for both parts. Values
                must be a list of tuples, each containing a test input
                and its corresponding solution.
            solution_one, solution_two -- already found solutions, used
                by the "solve" method to check for regression.
        """
        self.input = None
        self.parser = parser
        self.tests = tests
        self.solution_one = solution_one
        self.solution_two = solution_two

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def parse_input(self):
        """Apply defined parser to the input."""
        if isinstance(self.input, str):
            self.input = self.parser(self.input)
        else:
            self.input = list(map(self.parser, self.input))

    def test(self):
        """Run tests against their solution."""
        parts = (self.part_one, self.part_two)
        for p, part in enumerate(self.tests):
            for test, solution in self.tests[part]:
                self.input = test
                self.parse_input()
                answer = parts[p]()
                if not answer == solution:
                    print(f"Test failed in {part}:")
                    print(f"  {test} gives {answer} instead of {solution}.")
                    return False
        return True

    def solve(self):
        """Run puzzle parts and print status."""
        # --- Puzzle input ---
        self.input = load_input()
        self.parse_input()

        # --- Part One ---
        answer_one = self.part_one()
        if self.solution_one is None:
            print("Part One answer:", answer_one, "?")
        elif answer_one != self.solution_one:
            print(
                "Regression in part one:",
                f"got {answer_one} instead of {self.solution_one}.",
            )
        else:
            # --- Part Two ---
            answer_two = self.part_two()
            if self.solution_two is None:
                print("Part Two answer:", answer_two, "?")
            elif answer_two != self.solution_two:
                print(
                    "Regression in part two:",
                    f"got {answer_two} instead of {self.solution_two}.",
                )
            else:
                print("Day completed \o/")
