"""--- Day 10: Pipe Maze ---"""

from aoc.puzzle import Puzzle

PIPES = {
    "|": (-1, 1),
    "-": (-1j, 1j),
    "L": (-1, 1j),
    "J": (-1, -1j),
    "7": (1, -1j),
    "F": (1, 1j),
}


class Today(Puzzle):
    def parser(self):
        self.sketch = {}  # Full sketch with complex numbers
        self.pipes = {}  # Pipes with their connections
        for r, row in enumerate(self.input):
            for c, pipe in enumerate(row):
                position = r + c * 1j
                self.sketch[position] = pipe
                if pipe == "S":
                    self.start = position
                elif pipe in PIPES:
                    self.pipes[position] = [position + p for p in PIPES[pipe]]
        # Add the starting position to the pipes
        self.pipes[self.start] = [k for k, v in self.pipes.items() if self.start in v]
        # Replace the "S" in the sketch by the correct pipe shape
        self.sketch[self.start] = next(
            pipe
            for pipe, links in PIPES.items()
            if set(p - self.start for p in self.pipes[self.start]) == set(links)
        )

    def part_one(self):
        """BFS applied to the pipes from "S". Farthest point is the
        floor of the length of the loop divided by 2.
        """
        frontier = [self.start]
        self.loop = {self.start}
        while frontier:
            current = frontier.pop(0)
            for pipe in self.pipes[current]:
                if pipe not in self.loop:
                    frontier.append(pipe)
                    self.loop.add(pipe)
        return len(self.loop) // 2

    def part_two(self):
        """For each line, we start on the outside of the loop and
        alternate between inside/outise each time we cross pipes
        of the loop (|, L+7 or F+J).
        """
        enclosed = 0
        for r in range(len(self.input)):
            crossed = 0
            on_loop = ""
            for c in range(len(self.input[0])):
                pos = r + c * 1j
                if pos in self.loop:
                    if self.sketch[pos] in {"L", "F"}:
                        on_loop = self.sketch[pos]
                    elif (
                        self.sketch[pos] == "|"
                        or (on_loop == "L" and self.sketch[pos] == "7")
                        or (on_loop == "F" and self.sketch[pos] == "J")
                    ):
                        crossed += 1
                elif pos not in self.loop and crossed % 2:
                    enclosed += 1
        return enclosed


solutions = (6867, 595)

if __name__ == "__main__":
    Today(solutions=solutions).solve()
