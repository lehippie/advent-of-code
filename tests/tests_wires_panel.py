"""Tests of wires panel."""

import env
from lib import wires_panel as wp


wire1 = wp.wire_coords('R8,U5,L5,D3')
assert wire1 == {(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0),
                 (8,1), (8,2), (8,3), (8,4), (8,5), (7,5), (6,5), (5,5),
                 (4,5), (3,5),(3,4), (3,3), (3,2)}
wire2 = wp.wire_coords('U7,R6,D4,L4')
assert wire2 == {(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (1,7),
                 (2,7), (3,7), (4,7), (5,7), (6,7), (6,6), (6,5), (6,4),
                 (6,3), (5,3),(4,3), (3,3), (2,3)}
intersects = list(wire1 & wire2)
assert wp.manhattan(intersects[0]) == 6
assert wp.manhattan(intersects[1]) == 11

assert wp.distance('R8,U5,L5,D3', 'U7,R6,D4,L4') == 6
assert wp.distance('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83') == 159
assert wp.distance('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135
