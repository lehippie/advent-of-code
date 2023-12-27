"""--- Day 20: Pulse Propagation ---"""

from collections import deque
from copy import deepcopy
from math import prod, lcm
from aoc.puzzle import Puzzle


def push_button(modules, counts):
    """Update `modules` states and pulse `counts` during a button press."""
    instructions = deque([("broad", False, m) for m in modules["broad"]])
    counts[False] += len(modules["broad"]) + 1
    while instructions:
        src, pulse, mod = instructions.popleft()
        if modules[mod][0]:
            modules[mod][1][src] = pulse
            sent = not all(modules[mod][1].values())
            instructions.extend((mod, sent, d) for d in modules[mod][2] if d in modules)
            counts[sent] += len(modules[mod][2])
        elif not pulse:
            modules[mod][1] = not modules[mod][1]
            instructions.extend(
                (mod, modules[mod][1], d) for d in modules[mod][2] if d in modules
            )
            counts[modules[mod][1]] += len(modules[mod][2])


def detect_highs(modules, to_check):
    """Process a button press and check if a high pulse is sent by
    one of the modules to check.
    """
    highs = []
    instructions = deque([("broad", False, m) for m in modules["broad"]])
    while instructions:
        src, pulse, mod = instructions.popleft()
        if pulse and src in to_check:
            highs.append(src)
        if modules[mod][0]:
            modules[mod][1][src] = pulse
            sent = not all(modules[mod][1].values())
            instructions.extend((mod, sent, d) for d in modules[mod][2] if d in modules)
        elif not pulse:
            modules[mod][1] = not modules[mod][1]
            instructions.extend(
                (mod, modules[mod][1], d) for d in modules[mod][2] if d in modules
            )
    return highs


class Today(Puzzle):
    def parser(self):
        self.modules = {}
        for line in self.input:
            module, destinations = line.split(" -> ")
            destinations = destinations.split(", ")
            if module == "broadcaster":
                broadcaster = destinations
            elif module[0] == "%":
                # Flip-flops are saved with False as their first element
                self.modules[module[1:]] = [False, False, destinations]
            elif module[0] == "&":
                # Conjunctors are saved with True as their first element
                self.modules[module[1:]] = [True, {}, destinations]
        # Initialize all conjunctors
        for m, (_, _, destinations) in self.modules.items():
            for d in destinations:
                if d in self.modules and self.modules[d][0]:
                    self.modules[d][1][m] = False
        self.modules["broad"] = broadcaster

    def part_one(self):
        modules = deepcopy(self.modules)
        counts = {True: 0, False: 0}
        for _ in range(1000):
            push_button(modules, counts)
        return prod(counts.values())

    def part_two(self):
        """Looking at the graph of the input, we see that the <rx>
        module has a single input module, itself having 4 conjunctors
        as inputs. Each depends on series of flip-flops acting as
        counters.
        By detecting when each of the 4 conjuctors sends an high pulse
        to <rx>'s input module, we can calculate the lcm of them to
        answer the puzzle.
        """
        modules = deepcopy(self.modules)
        to_sync = deepcopy(next(m[1] for m in modules.values() if "rx" in m[2]))
        press = 0
        while True:
            press += 1
            highs = detect_highs(modules, to_sync)
            for h in highs:
                to_sync[h] = press
            if all(to_sync.values()):
                return lcm(*to_sync.values())


if __name__ == "__main__":
    Today().solve()
