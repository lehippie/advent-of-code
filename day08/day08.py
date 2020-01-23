"""Day 8: Space Image Format."""

from pathlib import Path
from sif import Sif

# Input
input_file = Path(__file__).parent / 'password.sif'
with open(input_file) as f:
    sif_data = f.readline()[:-1]
    pwd_sif = Sif(sif_data, 25, 6)

# Part 1:
amount_of_zeros = []
for l in pwd_sif.layers:
    amount_of_zeros.append(sum(r.count('0') for r in l))
check_layer = pwd_sif.layers[amount_of_zeros.index(min(amount_of_zeros))]
amount_of_ones = sum(r.count('1') for r in check_layer)
amount_of_twos = sum(r.count('2') for r in check_layer)
checksum = amount_of_ones * amount_of_twos
print(f"Checksum of received image: {checksum}")
assert checksum == 1820

# Part 2:
pwd_sif.show()  # ZUKCJ
assert pwd_sif.image == ['1111010010100100110000110',
                         '0001010010101001001000010',
                         '0010010010110001000000010',
                         '0100010010101001000000010',
                         '1000010010101001001010010',
                         '1111001100100100110001100']
