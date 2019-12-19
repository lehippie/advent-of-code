"""Wires panel functions."""


def wire_coords(wire_path):
    """Convert the list of directions into a set of coordinates."""
    path = [(0,0)]
    wire_path = wire_path.split(',')
    generator = ((p[0], int(p[1:])) for p in wire_path)  
    for d, n in generator:
        for _ in range(n):
            if d == 'U':
                path.append((path[-1][0], path[-1][1] + 1))
            if d == 'D':
                path.append((path[-1][0], path[-1][1] - 1))
            if d == 'L':
                path.append((path[-1][0] - 1, path[-1][1]))
            if d == 'R':
                path.append((path[-1][0] + 1, path[-1][1]))
    return set(path[1:])


def manhattan(X):
    """Manhattan distance from tuple X to origin."""
    return  abs(X[0]) + abs(X[1])


def distance(wire1_path, wire2_path):
    """Calculate the distance between two wires' path."""
    wire1 = wire_coords(wire1_path)
    wire2 = wire_coords(wire2_path)
    dists = [manhattan(M) for M in list(wire1 & wire2)]
    return min(dists)
