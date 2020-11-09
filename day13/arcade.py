"""Arcade library."""


class Arcade():
    """Arcade cabinet class.

    Arguments:
        program     Intcode program to run.
    """

    def __init__(self, program=[]):
        """Init arcade cabinet."""
        self.program = program
        self.tiles = {}
        self.score = 0


    def get_next_tile(self):
        """Read Intcode program to get tile info."""
        x = self.program.run(halt_on_output=True)
        y = self.program.run(halt_on_output=True)
        tile_id = self.program.run(halt_on_output=True)
        return x, y, tile_id


    def draw_tile(self, x, y, tile_id):
        """Draw tile from intcode output."""
        self.tiles[(x, y)] = tile_id


    def joystick(self):
        """Provite input according to joystick position."""
        try:
            ball = next(x for (x, y), i in self.tiles.items() if i ==  4)
            paddle = next(x for (x, y), i in self.tiles.items() if i ==  3)
        except StopIteration:
            return 0
        
        if ball < paddle:
            return -1
        elif ball > paddle:
            return 1
        else:
            return 0


    def run(self):
        """Run the game."""
        while not self.program.finished:
            x, y, tile_id = self.get_next_tile()
            if x == -1 and y == 0:
                self.score = tile_id
            else:
                self.draw_tile(x, y, tile_id)
            if self.program.waiting_for_input:
                self.program.execute_next(input_values=self.joystick())
    

def tests():
    a = Arcade()
    a.draw_tile(1, 2, 3)
    a.draw_tile(6, 5, 4)
    assert a.tiles == {(1, 2): 3, (6, 5): 4}


if __name__ == '__main__':
    tests()
