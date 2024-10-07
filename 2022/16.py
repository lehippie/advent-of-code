"""Day 16: Proboscidea Volcanium."""

from collections import defaultdict, deque
from itertools import combinations
from aoc.puzzle import Puzzle


def bfs(graph, current, goal):
    """Return time from <current> valve to open <goal> valve."""
    frontier = deque([(current, 0)])
    reached = {current}
    while frontier:
        position, time = frontier.popleft()
        for destination in graph[position]:
            if destination == goal:
                return time + 2
            if destination not in reached:
                reached.add(destination)
                frontier.append((destination, time + 1))


def max_pressure(graph, flows, valves, minutes=30):
    """Return maximum pressure released using <valves>."""
    max_released = 0
    frontier = [("AA", set(), 0, 0)]
    while frontier:
        position, opened, time, pressure = frontier.pop()
        if pressure > max_released:
            max_released = pressure
        for valve, move_time in graph[position].items():
            if valve in opened or valve not in valves:
                continue
            if (T := time + move_time) < minutes:
                P = pressure + (minutes - T) * flows[valve]
                frontier.append((valve, opened.union({valve}), T, P))
    return max_released


class Today(Puzzle):
    def parser(self):
        self.flows = {}
        self.tunnels = {}
        for line in self.input:
            valve, tunnel = line.split(";")
            v = valve.split()[1]
            self.flows[v] = int(valve.split("=")[-1])
            self.tunnels[v] = [t.replace(",", "") for t in tunnel.split()[4:]]

    def part_one(self):
        """Valves with flow rate 0 are just tunnels so we only care
        about the paths between each pair of useful valves.
        """
        self.valves = {v for v, f in self.flows.items() if f}
        self.graph = defaultdict(dict)
        for v1, v2 in combinations(self.valves, 2):
            self.graph[v1][v2] = bfs(self.tunnels, v1, v2)
            self.graph[v2][v1] = self.graph[v1][v2]
        self.graph["AA"] = {v: bfs(self.tunnels, "AA", v) for v in self.valves}
        return max_pressure(self.graph, self.flows, self.valves)

    def part_two(self):
        """We need to find the better pair of disjoint sets of valves.
        For that, all paths that can be explored in 26 minutes are
        considered.
        For paths with same valves but not in the same order, we keep
        the permutation leading to the max released pressure (stored
        as a frozenset to use as dict key).
        """
        paths = {}
        frontier = [(["AA"], [0])]
        while frontier:
            path, times = frontier.pop()
            for valve, move_time in self.graph[path[-1]].items():
                if valve not in path and (T := times[-1] + move_time) < 26:
                    new_path = path + [valve]
                    new_times = times + [T]
                    frontier.append((new_path, new_times))
                    valves = frozenset(new_path[1:])
                    P = max_pressure(self.graph, self.flows, valves, 26)
                    if valves not in paths or P > paths[valves]:
                        paths[valves] = P
        return max(
            p1 + p2
            for (s1, p1), (s2, p2) in combinations(paths.items(), 2)
            if not s1.intersection(s2)
        )


if __name__ == "__main__":
    Today().solve()
