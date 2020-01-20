"""Tests of Space Image Format functions."""

import env
from lib import sif


def tests():
    img = sif.Sif('123456789012', 3, 2)
    assert img.nb_layers == 2
    assert img.layers[0] == ['123', '456']
    assert img.layers[1] == ['789', '012']

    img = sif.Sif('2201', 1, 1)
    assert img.nb_layers == 4
    assert img.layers == [['2'], ['2'], ['0'], ['1']]
    assert img.image == ['0']

    img = sif.Sif('0222112222120000', 2, 2)
    assert img.image == ['01', '10']

if __name__ == "__main__":
    tests()
