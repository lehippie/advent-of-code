"""Day 23: Amphipod."""

from heapq import heappop, heappush
from aoc.puzzle import Puzzle


AMPHIPODS = "ABCD"
ENERGY = (1, 10, 100, 1000)
ROOMS_POSITIONS = (2, 4, 6, 8)
HALLWAY_SPACES = (0, 1, 3, 5, 7, 9, 10)


def possible_moves(burrow, s=2):
    """Generate possible moves from a given <burrow> with rooms of size <s> and
    generate each new state with its corresponding energy spending.
    """
    hallway = burrow[:11]
    rooms = [burrow[k : k + s] for k in range(11, len(burrow), s)]

    # --- Each amphipod in the hallway try to go in its room ---
    for pos, amph in enumerate(hallway):
        if amph not in AMPHIPODS:
            continue
        idx = AMPHIPODS.index(amph)
        rpos = ROOMS_POSITIONS[idx]
        path = hallway[pos + 1 : rpos + 1] if pos < rpos else hallway[rpos:pos]
        if path == "." * len(path) and set(rooms[idx]).issubset(("*", amph)):
            destinations = rooms[idx].rfind("*")
            spending = ENERGY[idx] * (len(path) + destinations + 1)
            new_hallway = list(hallway)
            new_hallway[pos] = "."
            new_rooms = rooms.copy()
            new_rooms[idx] = amph.join(new_rooms[idx].rsplit("*", 1))
            yield "".join(new_hallway + new_rooms), spending

    # --- Amphipods misplaced in a room goes into the hallway ---
    for idx, room in enumerate(rooms):
        if set(room).issubset(("*", AMPHIPODS[idx])):
            continue
        rpos = ROOMS_POSITIONS[idx]
        pos, amph = next((p, a) for p, a in enumerate(room) if a != "*")
        # Explore hallway in both direction to find available spaces
        destinations = []
        for h in HALLWAY_SPACES:
            if h < rpos:
                continue
            if hallway[h] == ".":
                destinations.append(h)
            else:
                break
        for h in HALLWAY_SPACES[::-1]:
            if h > rpos:
                continue
            if hallway[h] == ".":
                destinations.append(h)
            else:
                break

        for dest in destinations:
            spending = ENERGY[AMPHIPODS.index(amph)] * (pos + 1 + abs(rpos - dest))
            new_hallway = list(hallway)
            new_hallway[dest] = amph
            new_rooms = rooms.copy()
            new_rooms[idx] = new_rooms[idx].replace(amph, "*", 1)
            yield "".join(new_hallway + new_rooms), spending


class Today(Puzzle):
    def parser(self):
        hallway = self.input[1][1:-1]
        rooms = ["".join(l[r + 1] for l in self.input[2:-1]) for r in ROOMS_POSITIONS]
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
        start = (
            self.start[:12]
            + "DD"
            + self.start[12:14]
            + "CB"
            + self.start[14:16]
            + "BA"
            + self.start[16:18]
            + "AC"
            + self.start[18]
        )
        goal = "...........AAAABBBBCCCCDDDD"
        burrows = [(0, start)]
        cache = dict()
        while burrows:
            energy, burrow = heappop(burrows)
            if burrow == goal:
                return energy
            for next_burrow, spending in possible_moves(burrow, s=4):
                new_energy = energy + spending
                if next_burrow not in cache or new_energy < cache[next_burrow]:
                    cache[next_burrow] = new_energy
                    heappush(burrows, (new_energy, next_burrow))


if __name__ == "__main__":
    Today().solve()
