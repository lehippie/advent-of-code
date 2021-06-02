"""Base puzzle class."""


class Puzzle:
    def __init__(self, tests=None, solution_one=None, solution_two=None):
        self.tests = tests
        self.solution_one = solution_one
        self.solution_two = solution_two
        self.input = None

    def part_one(self):
        return NotImplemented

    def part_two(self):
        return NotImplemented

    def test(self):
        """Peform test checks."""
        parts = (self.part_one, self.part_two)
        for p, part in enumerate(self.tests):
            for test, solution in self.tests[part]:
                self.input = test
                answer = parts[p]()
                if not answer == solution:
                    print("Test failed in", part)
                    print(f"{test} gives {answer} instead of {solution}.")
                    return False
        print("Tests passed!")
        return True

    def solve(self):
        """Run puzzle parts."""
        answer_one = self.part_one()
        if self.solution_one is None:
            print("Part One answer:", answer_one, "?")
        elif answer_one != self.solution_one:
            print(
                "Regression in part one:",
                f"got {answer_one} instead of {self.solution_one}.",
            )
        else:
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
