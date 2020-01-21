"""Day 8 script."""

import env
from lib import sif

# Input
with open('inputs/08_rover_bios_password.txt') as f:
    line = f.readline()
    pwd = sif.Sif(line[:-1], 25, 6)

# Part 1:
amount_of_zeros = []
for l in pwd.layers:
    amount_of_zeros.append(sum(r.count('0') for r in l))
check_layer = pwd.layers[amount_of_zeros.index(min(amount_of_zeros))]
amount_of_ones = sum(r.count('1') for r in check_layer)
amount_of_twos = sum(r.count('2') for r in check_layer)
checksum = amount_of_ones * amount_of_twos
print(f"Checksum of received image: {checksum}")
assert checksum == 1820

# Part 2: ZUKCJ
pwd.show()
assert pwd.image == ['1111010010100100110000110',
                     '0001010010101001001000010',
                     '0010010010110001000000010',
                     '0100010010101001000000010',
                     '1000010010101001001010010',
                     '1111001100100100110001100']
