"""--- Day 17: Set and Forget ---"""

from itertools import product
from aoc.puzzle import Puzzle
from intcode import Intcode


class Today(Puzzle):
    def parser(self):
        self.program = list(map(int, self.input.split(",")))

    def part_one(self):
        ascii_program = Intcode(self.program)
        ascii_program.run(pause_on_output=False)
        view = "".join(map(chr, ascii_program.outputs)).strip().split("\n")
        # print("\n".join(view))
        return sum(
            row * col
            for row, col in product(range(1, len(view) - 1), range(1, len(view[0]) - 1))
            if (
                view[row][col] == "#"
                and view[row][col - 1] == "#"
                and view[row][col + 1] == "#"
                and view[row - 1][col] == "#"
                and view[row + 1][col] == "#"
            )
        )

    def part_two(self):
        """Reto-engineering the scaffolding to manually find the routine and
        functions.
        """
        ascii_program = Intcode(self.program)
        ascii_program.memory[0] = 2
        main = "A,A,B,C,B,C,B,C,A,C\n"
        A = "R,6,L,8,R,8\n"
        B = "R,4,R,6,R,6,R,4,R,4\n"
        C = "L,8,R,6,L,10,L,10\n"
        feed = "n\n"
        ascii_program.inputs = list(map(ord, main + A + B + C + feed))
        ascii_program.run(pause_on_output=False)
        return ascii_program.outputs[-1]


if __name__ == "__main__":
    Today().solve()
