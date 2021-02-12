"""Day 17: Set and Forget."""

from itertools import product
from pathlib import Path

from intcode import Intcode


# --- Parsing input ---

def parse_input(filename):
    return Intcode.from_file(Path(__file__).parent / filename)


# --- Part One ---

def alignement_parameter(view):
    return sum(
        row * col
        for row, col in product(range(1, len(view)-1),
                                range(1, len(view[0])-1))
        if (view[row][col] == "#"
            and view[row][col-1] == "#"
            and view[row][col+1] == "#"
            and view[row-1][col] == "#"
            and view[row+1][col] == "#")
    )


def part_one(ascii_program: Intcode):
    ascii_outputs = ascii_program.run(halt_on_output=False)
    view = "".join(chr(a) for a in ascii_outputs).strip().split("\n")
    # print("\n".join(view))
    return alignement_parameter(view)


# --- Part Two ---

def part_two(ascii_program: Intcode):
    ascii_program.reset()
    ascii_program[0] = 2
    main = "A,A,B,C,B,C,B,C,A,C\n"
    A = "R,6,L,8,R,8\n"
    B = "R,4,R,6,R,6,R,4,R,4\n"
    C = "L,8,R,6,L,10,L,10\n"
    feed = "n\n"
    input_ints = list(map(ord, main + A + B + C + feed))
    return ascii_program.run(input_values=input_ints, halt_on_output=False)[-1]


# --- Tests & Run ---

def tests():
    test = ["..#..........",
            "..#..........",
            "#######...###",
            "#.#...#...#.#",
            "#############",
            "..#...#...#..",
            "..#####...^.."]
    assert alignement_parameter(test) == 76


if __name__ == "__main__":
    tests()

    ascii_program = parse_input("ascii.txt")

    result_one = part_one(ascii_program)
    print("Part One answer:", result_one)
    assert result_one == 8520

    result_two = part_two(ascii_program)
    print("Part Two answer:", result_two)
    assert result_two == 926819
