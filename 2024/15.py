"""--- Day 15: Warehouse Woes ---"""

from itertools import chain, count, takewhile
from aoc.puzzle import Puzzle


class Today(Puzzle):
    def parser(self):
        self.walls, self.boxes = set(), set()
        self.moves = []
        directions = {"^": -1, "v": 1, "<": -1j, ">": 1j}
        for r, row in enumerate(self.input):
            if row.startswith("#"):
                for c, cell in enumerate(row):
                    if cell == "@":
                        self.robot = r + c * 1j
                    elif cell == "#":
                        self.walls.add(r + c * 1j)
                    elif cell == "O":
                        self.boxes.add(r + c * 1j)
            elif row:
                self.moves.extend(directions[m] for m in row)

    def part_one(self):
        """If a robot tries to push a box, it is possible if there is
        no wall after all the following boxes.
        """
        robot = self.robot
        boxes = self.boxes.copy()
        for move in self.moves:
            step = robot + move
            if step not in boxes and step not in self.walls:
                robot = step
            elif step in boxes:
                after = next(
                    step + k * move for k in count(1) if step + k * move not in boxes
                )
                if after not in self.walls:
                    robot = step
                    boxes.remove(step)
                    boxes.add(after)
        return int(sum(100 * b.real + b.imag for b in boxes))

    def part_two(self):
        """Same as in part one but we have to check all spaces that
        follows the boxes in contact with the one pushed in case of
        vertical move.
        """
        # Parse the wide warehouse
        robot = self.robot + self.robot.imag * 1j
        walls = set()
        for wall in self.walls:
            walls.add(wall + wall.imag * 1j)
            walls.add(wall + (wall.imag + 1) * 1j)
        boxes = []
        for box_id in self.boxes:
            boxes.append({box_id + box_id.imag * 1j, box_id + (box_id.imag + 1) * 1j})

        # Handle robot moves
        for move in self.moves:
            all_boxes = set(chain(*boxes))
            is_box = lambda x: x in all_boxes

            step = robot + move
            if step in walls:
                continue
            if step not in all_boxes:
                robot = step
                continue

            # Horizontal push
            if move == 1j or move == -1j:
                afters = [*takewhile(is_box, (step + k * move for k in count(1)))]
                if afters[-1] + move not in walls:
                    robot = step
                    for box_id in {
                        k
                        for k, box in enumerate(boxes)
                        if any(p in box for p in afters)
                    }:
                        boxes[box_id] = {p + move for p in boxes[box_id]}

            # Vertical push
            else:
                box_id = next(k for k, b in enumerate(boxes) if step in b)
                pushed = {box_id}
                frontier = set(boxes[box_id])
                while frontier:
                    check = frontier.pop() + move
                    if check in walls:
                        break
                    elif check in all_boxes:
                        box_id = next(k for k, b in enumerate(boxes) if check in b)
                        pushed.add(box_id)
                        frontier.update(boxes[box_id])
                else:
                    robot = step
                    for box_id in pushed:
                        boxes[box_id] = {p + move for p in boxes[box_id]}

        return int(sum(100 * b1.real + min(b1.imag, b2.imag) for b1, b2 in boxes))


if __name__ == "__main__":
    Today().solve()
