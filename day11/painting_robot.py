"""Emergency Hull Painting Robot library."""


class PaintingRobot():
    """Emergency hull painting robot class."""

    def __init__(self, posx=0, posy=0, face='n'):
        """Init PaintingRobot."""
        self.posx = posx
        self.posy = posy
        self.face = face
        self.panels = {(self.posx, self.posy): 0}


    def look(self):
        """Return current panel color."""
        return self.panels.get((self.posx, self.posy), 0)


    def paint(self, color):
        """Paint current panel."""
        if color in (1, 'white'):
            self.panels[(self.posx, self.posy)] = 1
        elif color in (0, 'black'):
            self.panels[(self.posx, self.posy)] = 0
        else:
            raise IOError(f"Incorrect color '{color}'.")


    def rotate(self, direction):
        """Rotate according to direction."""
        if direction not in (0, 1):
            if direction == 'right':
                direction = 1
            elif direction == 'left':
                direction = 0
            else:
                raise IOError(f"Incorrect direction '{direction}'.")

        if self.face == 'n':
            self.face = 'e' if direction else 'w'
        elif self.face == 'e':
            self.face = 's' if direction else 'n'
        elif self.face == 's':
            self.face = 'w' if direction else 'e'
        elif self.face == 'w':
            self.face = 'n' if direction else 's'


    def move(self):
        """Move forward by one panel."""
        if self.face == 'n':
            self.posy += 1
        if self.face == 'e':
            self.posx += 1
        if self.face == 's':
            self.posy += -1
        if self.face == 'w':
            self.posx += -1


    def action(self, color, direction):
        """Paint, rotate and move."""
        self.paint(color)
        self.rotate(direction)
        self.move()
        return self.look()


if __name__ == '__main__':
    from painting_robot_tests import tests
    tests()
