"""Space Image Format library."""

import numpy as np
import matplotlib.pyplot as plt


class Sif():
    """Space Image Format class."""

    def __init__(self, image_data, width, height):
        self.raw_data = image_data
        self.width = width
        self.height = height
        self.nbpix = self.width * self.height
        self.layers = self.process_raw_data()
        self.nb_layers = len(self.layers)
        self.image = self.process_image()

    def process_raw_data(self):
        """Convert raw data into list of layers."""
        layers_data = [self.raw_data[i:i + self.nbpix]
                       for i in range(0, len(self.raw_data), self.nbpix)]
        out = [[l[j:j + self.width]
                for j in range(0, len(l), self.width)]
               for l in layers_data]
        return out

    def __str__(self):
        out = []
        for i, l in enumerate(self.layers):
            head = f"Layer {i+1}: "
            for r in l:
                if r is l[0]:
                    out.append(head + r)
                else:
                    out.append(r.rjust(len(head) + len(r)))
        return '\n'.join(out)

    def process_image(self):
        """Decode the image."""
        out = []
        for r in range(self.height):
            line = []
            for c in range(self.width):
                v = next(self.layers[l][r][c]
                         for l in range(self.nb_layers)
                         if self.layers[l][r][c] != '2')
                line.append(v)
            out.append(''.join(line))
        return out

    def print(self):
        """Print image."""
        print('\n'.join(self.image))

    def show(self):
        """Show image."""
        img = np.array([list(map(int, d)) for d in self.image])
        plt.rcParams['toolbar'] = 'None'
        _, ax = plt.subplots(
            figsize=(3, 3 * self.height / self.width),
            facecolor='k')
        ax.matshow(img, cmap=plt.cm.get_cmap('bone'))
        ax.axis('off')
        plt.show()


if __name__ == "__main__":
    from sif_tests import tests
    tests()
