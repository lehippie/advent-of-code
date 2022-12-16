"""Day 16: Proboscidea Volcanium."""

from collections import defaultdict, deque
from itertools import combinations
from aoc.puzzle import Puzzle


def bfs(graph, start, goal):
    """Time to go open valve <goal> from <start>."""
    frontier = deque([(start, 0)])
    reached = set(start)
    while frontier:
        position, minutes = frontier.popleft()
        for destination in graph[position]:
            if destination == goal:
                return minutes + 2
            if destination not in reached:
                reached.add(destination)
                frontier.append((destination, minutes + 1))


class Today(Puzzle):
    def parser(self):
        self.flow = {}
        self.tunnels = {}
        for line in self.input:
            valve, tunnel = line.split(";")
            v = valve.split()[1]
            self.flow[v] = int(valve.split("=")[-1])
            self.tunnels[v] = [t.replace(",", "") for t in tunnel.split()[4:]]

    def part_one(self):
        """Valves with flow rate 0 are just tunnels. We only care
        about the shortest paths between each pair of closed valves
        with positive flow rates.
        The new graph is then explored fully to find the best path.
        """
        valves = {v for v, f in self.flow.items() if f}
        self.graph = defaultdict(dict)
        self.graph["AA"] = {v: bfs(self.tunnels, "AA", v) for v in valves}
        for v1, v2 in combinations(valves, 2):
            minutes = bfs(self.tunnels, v1, v2)
            self.graph[v1][v2] = minutes
            self.graph[v2][v1] = minutes

        max_pressure = 0
        paths = [("AA", set(), 0, 0)]
        while paths:
            position, opened, time, pressure = paths.pop()
            for valve, move in self.graph[position].items():
                if valve in opened:
                    continue
                T = time + move
                if T < 30:
                    P = pressure + (30 - T) * self.flow[valve]
                    paths.append((valve, opened.union({valve}), T, P))
                max_pressure = max(max_pressure, P)
        return max_pressure

    def part_two(self):
        return NotImplemented


solutions = (1580, None)

if __name__ == "__main__":
    test = Today(
        solutions=(1651, 1707),
        input_data=[
            "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
            "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
            "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
            "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
            "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
            "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
            "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
            "Valve HH has flow rate=22; tunnel leads to valve GG",
            "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
            "Valve JJ has flow rate=21; tunnel leads to valve II",
        ],
    ).solve()
    Today(solutions=solutions).solve()
