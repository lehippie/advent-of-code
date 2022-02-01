"""Day 8: Seven Segment Search."""

from aoc.puzzle import Puzzle


class Display:
    def __init__(self, digits, output):
        self.digits = digits
        self.output = output
        self.signals = [None] * 10

    def deduce_signals(self):
        unknown = sorted(self.digits, key=len)
        self.signals[1] = unknown.pop(0)
        self.signals[7] = unknown.pop(0)
        self.signals[4] = unknown.pop(0)
        self.signals[8] = unknown.pop()
        for digit in unknown:
            if len(digit) == 5:
                if digit.issuperset(self.signals[7]):
                    self.signals[3] = digit
                elif len(digit.intersection(self.signals[4])) == 3:
                    self.signals[5] = digit
                else:
                    self.signals[2] = digit
            else:
                if digit.issuperset(self.signals[4]):
                    self.signals[9] = digit
                elif digit.issuperset(self.signals[1]):
                    self.signals[0] = digit
                else:
                    self.signals[6] = digit

    def decode_output(self):
        return "".join(str(self.signals.index(d)) for d in self.output)


class Today(Puzzle):
    def parser(self):
        self.displays = []
        for entry in self.input:
            digits, output = map(str.split, entry.split(" | "))
            digits = [set(d) for d in digits]
            output = [set(out) for out in output]
            self.displays.append(Display(digits, output))

    def part_one(self):
        unique_count = 0
        for display in self.displays:
            unique_count += sum(len(d) in {2, 3, 4, 7} for d in display.output)
        return unique_count

    def part_two(self):
        outputs = 0
        for display in self.displays:
            display.deduce_signals()
            outputs += int(display.decode_output())
        return outputs


solutions = (383, 998900)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
