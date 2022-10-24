"""Day 23: Amphipod."""

from heapq import heappop, heappush
from aoc.puzzle import Puzzle


ROOMS = (2, 4, 6, 8)
AMPHIPODS = {
    "A": {"room": ROOMS[0], "energy": 1},
    "B": {"room": ROOMS[1], "energy": 10},
    "C": {"room": ROOMS[2], "energy": 100},
    "D": {"room": ROOMS[3], "energy": 1000},
}


def possible_moves(burrow, hall_len=11):
    """Generate possible moves from a given <burrow> and return each
    new state with its corresponding energy used.
    """
    print(burrow)
    hallway = burrow[:hall_len]
    print(hallway)
    rooms = [burrow[k : k + 2] for k in range(hall_len, len(burrow), 2)]
    print(rooms)
    for k, amph in enumerate(a for a in hallway if a in AMPHIPODS):
        print(k, amph)


class Today(Puzzle):
    def parser(self):
        hallway = self.input[1][1:-1]
        rooms = ["".join(l[r + 1] for l in self.input[2:-1]) for r in ROOMS]
        self.start = hallway + "".join(rooms)

    def part_one(self):
        goal = "...........AABBCCDD"
        burrows = [(0, self.start)]
        cache = dict()
        while burrows:
            energy, burrow = heappop(burrows)
            if burrow == goal:
                return energy
            for next_burrow, spending in possible_moves(burrow):
                new_energy = energy + spending
                if next_burrow not in cache or new_energy < cache[next_burrow]:
                    cache[next_burrow] = new_energy
                    heappush(burrows, (new_energy, next_burrow))

    def part_two(self):
        return super().part_two()


solutions = (None, None)

if __name__ == "__main__":
    t = Today(
        input_data=[
            "#############",
            "#...........#",
            "###B#C#B#D###",
            "  #A#D#C#A#",
            "  #########",
        ]
    )
    assert t.part_one() == 12521
    Today(solutions=solutions).solve()
