"""Day 8: Seven Segment Search."""

from aoc.puzzle import Puzzle


class Display:
    def __init__(self, segments, output):
        self.segments = sorted(segments, key=len)
        self.output = output
        self.digits = [None] * 10

    def repair(self):
        """Associate sets of segments with their digit. 1, 7, 4 and 8
        have unique lengths. 7 is included in 3, 4 in 9, etc...
        """
        self.digits[1] = self.segments.pop(0)
        self.digits[7] = self.segments.pop(0)
        self.digits[4] = self.segments.pop(0)
        self.digits[8] = self.segments.pop()
        for digit in self.segments:
            if len(digit) == 5:
                if digit.issuperset(self.digits[7]):
                    self.digits[3] = digit
                elif len(digit.intersection(self.digits[4])) == 3:
                    self.digits[5] = digit
                else:
                    self.digits[2] = digit
            else:
                if digit.issuperset(self.digits[4]):
                    self.digits[9] = digit
                elif digit.issuperset(self.digits[1]):
                    self.digits[0] = digit
                else:
                    self.digits[6] = digit

    def decode_output(self):
        return "".join(str(self.digits.index(d)) for d in self.output)


class Today(Puzzle):
    def parser(self):
        """Store display's visible segments and output in sets."""
        self.displays = []
        for entry in self.input:
            segments, output = map(str.split, entry.split(" | "))
            segments = [set(d) for d in segments]
            output = [set(out) for out in output]
            self.displays.append(Display(segments, output))

    def part_one(self):
        easy_digits_count = 0
        for display in self.displays:
            easy_digits_count += sum(len(d) in {2, 3, 4, 7} for d in display.output)
        return easy_digits_count

    def part_two(self):
        outputs = 0
        for display in self.displays:
            display.repair()
            outputs += int(display.decode_output())
        return outputs


solutions = (383, 998900)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
